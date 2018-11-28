#include <vector>
#include <boost/lexical_cast.hpp>
#include <iostream>
#include <string>
#include <sstream>
#include <list>
#include <stdexcept>
#include <boost/format.hpp>
#include <fstream>
#include <map>

template<typename T>
class Matrix
{
	std::vector<T> arr;
	size_t cx, cy, max_index;
public:
	void resize(size_t _cx, size_t _cy)
	{
		arr.resize(_cx*_cy);
		cx = _cx;
		cy = _cy;
		max_index = cx*cy;
	}

	inline T & operator()(const size_t & _cx, const size_t & _cy)
	{
		if(_cx >= cx || _cy >= cy)
		{
		throw std::runtime_error("Out of bounds");
		}
		/*size_t idx = _cx+cx*_cy;
		if(idx >= max_index)
		{
			throw std::exception("Out of bounds");
		}*/
		return arr[_cx+cx*_cy];
	};

	inline const T & operator()(const size_t & _cx, const size_t & _cy) const
	{
		if(_cx >= cx || _cy >= cy)
		{
		throw std::runtime_error("Out of bounds");
		}
		/*size_t idx = _cx+cx*_cy;
		if(idx >= max_index)
		{
			throw std::exception("Out of bounds");
		}*/
		return arr[_cx+cx*_cy];
	};

	Matrix() : cx(0), cy(0) {}

	size_t max_cx() const
	{
		return cx;
	}

	size_t max_cy() const
	{
		return cy;
	}
};

typedef std::pair<int, int> flow_t;

struct Node
{
	Node() : basin(0) {};
	int h;
	int x, y;
	char basin;
	flow_t flow_dir;
};

typedef Matrix<Node> map_t;

bool is_sink(map_t & map, int i, int j)
{
	int h = map(i,j).h;

	if(i < map.max_cx()-1)
	{
		if(h >= map(i+1,j).h)
		{
			return false;
		}
	}

	if(j < map.max_cy()-1)
	{
		if(h >= map(i,j+1).h)
		{
			return false;
		}
	}

	if(i > 0)
	{
		if(h >= map(i-1,j).h)
		{
			return false;
		}
	}

	if(j > 0)
	{
		if(h >= map(i,j-1).h)
		{
			return false;
		}
	}

	return true;
}

enum CARD
{
	NORTH,
	WEST,
	EAST,
	SOUTH,
	N_DIR
};

void flow(map_t & map, int i, int j)
{
	int h = map(i,j).h;

	int nh[N_DIR];

	// North
	if(i < map.max_cx()-1)
	{
		nh[NORTH] = map(i+1,j).h;
	}
	else
	{
		nh[NORTH] = h + 1;
	}

	// West
	if(j > 0)
	{
		nh[WEST] =  map(i,j-1).h;
	}
	else
	{
		nh[WEST] = h + 1;
	}

	// SOUTH
	if(i > 0)
	{
		nh[SOUTH] = map(i-1,j).h;
	}
	else
	{
		nh[SOUTH] = h + 1;
	}

	// East
	if(j < map.max_cy()-1)
	{
		nh[EAST] = map(i,j+1).h;
	}
	else
	{
		nh[EAST] = h + 1;
	}

	CARD dir = N_DIR;

	int min_h = h;

	for(int k = 0; k < N_DIR; ++k)
	{
		if(nh[k] < min_h)
		{
			min_h = nh[k];
		}
	}

	if(min_h == h)
	{
		map(i,j).flow_dir = flow_t(i,j);
		return;
	}

	for(int k = 0; k < N_DIR; ++k)
	{
		if(min_h == nh[k])
		{
			dir = CARD(k);
			break;
		}
	}

	switch(dir)
	{
	case NORTH:
		map(i,j).flow_dir = flow_t(i+1,j);
		break;
	case SOUTH:
		map(i,j).flow_dir = flow_t(i-1,j);
		break;
	case EAST:
		map(i,j).flow_dir = flow_t(i,j+1);
		break;
	case WEST:
		map(i,j).flow_dir = flow_t(i,j-1);
		break;
	}

}

void flood(map_t & map, int i, int j);

inline void maybe_descend(map_t & map, Node & cur, Node & neigh, flow_t curp)
{
	if(neigh.basin == 0)
	{
		if(neigh.flow_dir == curp)
		{
			neigh.basin = cur.basin;
			flood(map, neigh.x, neigh.y);
		}
	}
}

void flood(map_t & map, int i, int j)
{
	flow_t curp(i,j);
	Node & cur_node = map(i,j);
	if(i < map.max_cx()-1)
	{
		maybe_descend(map, cur_node, map(i+1,j), curp);
	}

	if(j < map.max_cy()-1)
	{
		maybe_descend(map, cur_node, map(i,j+1), curp);
	}

	if(i > 0)
	{
		maybe_descend(map, cur_node, map(i-1,j), curp);
	}

	if(j > 0)
	{
		maybe_descend(map, cur_node, map(i,j-1), curp);
	}
}


int main(int argc, char *argv)
{
	std::ofstream file("log.txt");
	std::string line;

	std::getline(std::cin, line);

	int T = boost::lexical_cast<int>(line);

	for(int C = 0; C < T; ++C)
	{
		std::getline(std::cin, line);

		std::stringstream buf(line);


		int H, W;

		buf >> H >> W;

		map_t map;
		map.resize(H,W);

		for(int i = H-1; i >= 0; --i)
		{
			std::getline(std::cin, line);
			buf.clear();
			buf.str(line);

			for(int j = 0; j < W; ++j)
			{
				buf >> map(i,j).h;
				map(i,j).x = i;
				map(i,j).y = j;
			}
		}

		char cur_sink = 1;

		typedef std::list<std::pair<int,int> > sinks_t;
		sinks_t sinks;

		for(int i = H-1; i >= 0; --i)
		{
			for(int j = 0; j < W; ++j)
			{
				flow(map, i, j);
				if(map(i,j).flow_dir == std::make_pair(i,j))
				{
					map(i,j).basin = cur_sink++;
					sinks.push_back(map(i,j).flow_dir);
				}
			}
		}

		for(sinks_t::const_iterator i = sinks.begin(); i != sinks.end(); ++i)
		{
			flood(map, i->first, i->second);
		}

		typedef std::map<char, char> trans_t;
		trans_t trans;
		
		cur_sink = 'a';

		for(int i = H-1; i >= 0; --i)
		{
			for(int j = 0; j < W; ++j)
			{
				trans_t::const_iterator conv = trans.find(map(i,j).basin);
				if(conv == trans.end())
				{
					char id = map(i,j).basin;
					map(i,j).basin = cur_sink;
					trans.insert(std::make_pair(id, cur_sink++));
				}
				else
				{
					map(i,j).basin = conv->second;
				}
			}
		}


		buf.clear();
		buf.str("");

		buf << boost::format("Case #%1%:\n") % int(C+1);
		std::cout << buf.str();
		file << buf.str();

		for(int i = map.max_cx()-1; i >= 0; --i)
		{
			buf.clear();
			buf.str("");
			for(int j = 0; j < map.max_cy(); ++j)
			{
				buf << map(i,j).basin;
				if(j < map.max_cy()-1)
				{
					buf << " ";
				}
			}

			buf << std::endl;
			std::cout << buf.str();
			file << buf.str();
		}
	}
}