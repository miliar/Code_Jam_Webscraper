#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

class watershed
{
	public:
		vector<vector<int> > map;
};

class basin_t
{
	public:
		basin_t(watershed & source)
		{
			map.resize(source.map.size());
			for(int j=0;j<source.map.size();j++)
			{
				map[j].resize(source.map[j].size());
			}
		}
		vector<vector<char> > map;
		bool isnext()
		{
			for(int i=0;i<map.size();i++)
			{
				for(int j=0;j<map[i].size();j++)
				{
					if(isupper(map[i][j]))
					{
						return true;
					}
				}
			}
			return false;
		}
		pair<int,int> findnext()
		{
			for(int i=0;i<map.size();i++)
			{
				for(int j=0;j<map[i].size();j++)
				{
					if(isupper(map[i][j]))
					{
						return make_pair(i,j);
					}
				}
			}
			return make_pair(-1,-1);
		}
};

ostream & operator << (ostream & out, const watershed & rhs)
{
	for(int i=0;i<rhs.map.size();i++)
	{
		for(int j=0;j<rhs.map[i].size();j++)
		{
			out << rhs.map[i][j] << " ";
		}
		out << endl;
	}
	return out;
}

ostream & operator << (ostream & out, const basin_t & rhs)
{
	for(int i=0;i<rhs.map.size();i++)
	{
		for(int j=0;j<rhs.map[i].size();j++)
		{
			out << rhs.map[i][j];
			if((j+1)<rhs.map[i].size())
			{
				out << " ";
			}
		}
		out << endl;
	}
	return out;
}

int main()
{
	int T, H, W;
	cin >> T;

	vector<watershed> maps(T);

	for(int i=0;i<T;i++)
	{
		cin >> H >> W;
		maps[i].map.resize(H);
		for(int j=0;j<H;j++)
		{
			maps[i].map[j].resize(W);
			for(int k=0;k<W;k++)
			{
				cin >> maps[i].map[j][k];
			}
		}
	}

	for(int i=0;i<T;i++)
	{
		basin_t basin(maps[i]);

		vector<vector<int> > cur(maps[i].map);

		//pair<row, column>
		vector<pair<int, int> > sinks;
		for(int r=0;r<cur.size();r++)
		{
			for(int c=0;c<cur[r].size();c++)
			{
				int val = cur[r][c];
				bool sink = true;
				if(r>0)
				{
					sink &= !(cur[r-1][c] < val);
				}
				if(c>0)
				{
					sink &= !(cur[r][c-1] < val);
				}
				if(r<(cur.size()-1))
				{
					sink &= !(cur[r+1][c] < val);
				}
				if(c<(cur[r].size()-1))
				{
					sink &= !(cur[r][c+1] < val);
				}
				if(sink)
				{
					sinks.push_back(make_pair(r,c));
				}	
			}
		}

		for(int j=0;j<sinks.size();j++)
		{
//			cout << sinks[j].first << ", " << sinks[j].second << endl;
			basin.map[sinks[j].first][sinks[j].second] = 'S';
		}

		for(int r=0;r<cur.size();r++)
		{
			for(int c=0;c<cur[r].size();c++)
			{
				if(basin.map[r][c] == 'S')
				{
					continue;
				}
				// {N, W, S, E}
				vector<int> neighbors;
				neighbors.push_back(15000);
				neighbors.push_back(15000);
				neighbors.push_back(15000);
				neighbors.push_back(15000);
				if(r>0)
				{
					neighbors[0] = cur[r-1][c];
				}
				if(c>0)
				{
					neighbors[1] = cur[r][c-1];
				}
				if(r<(cur.size()-1))
				{
					neighbors[2] = cur[r+1][c];
				}
				if(c<(cur[r].size()-1))
				{
					neighbors[3] = cur[r][c+1];
				}

				int val = cur[r][c];
				int min_el = (*(min_element(neighbors.begin(),neighbors.end())));
				if(neighbors[0] == min_el)
				{
					basin.map[r][c] = 'U';
				}
				else if(neighbors[1] == min_el)
				{
					basin.map[r][c] = 'L';
				}
				else if(neighbors[3] == min_el)
				{
					basin.map[r][c] = 'R';
				}
				else
				{
					basin.map[r][c] = 'D';
				}
			}
		}

		char at = 'a';
		vector<pair<int,int> > thepath;
		pair<int,int> start;
		while(basin.isnext())
		{
			int r,c;
			pair<int,int> next = basin.findnext();
			r = next.first;
			c = next.second;

			while(isupper(basin.map[r][c]))
			{
				thepath.push_back(make_pair(r,c));
				if(basin.map[r][c] == 'U')
				{
					r--;
				}
				else if(basin.map[r][c] == 'D')
				{
					r++;
				}
				else if(basin.map[r][c] == 'L')
				{
					c--;
				}
				else if(basin.map[r][c] == 'R')
				{
					c++;
				}
				else
				{
					//is a sink
					break;
				}
			}

			if(islower(basin.map[r][c]))
			{
				for(int j=0;j<thepath.size();j++)
				{
					basin.map[thepath[j].first][thepath[j].second] = basin.map[r][c];
				}
			}
			else
			{
				for(int j=0;j<thepath.size();j++)
				{
					basin.map[thepath[j].first][thepath[j].second] = at;
				}
				at++;
			}
			thepath.clear();
		}

		cout << "Case #" << i+1 << ":" << endl;
		cout << basin;
	}
	return 0;
}
