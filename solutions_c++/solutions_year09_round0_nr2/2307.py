#include <iostream>
#include <fstream>

#include <string>

#include <vector>
#include <set>
#include <list>
#include <map>

using namespace std;

#define OFFLIMITS_RESULT 10001

#define NORTH 'N'
#define WEST 'W'
#define EAST 'E'
#define SOUTH 'S'
#define SINK 'K'

#define UNLABELED 0

#define M_NORTH(h, w)  ((h) - 1), (w)
#define M_WEST(h, w)   (h), ((w) - 1)
#define M_EAST(h, w)   (h), ((w) + 1)
#define M_SOUTH(h, w)  ((h) + 1), (w)


#define MAX 110
template<typename data>
class e_matrix
{
public:
	e_matrix()
		: _matrix(MAX, vector<data>(MAX, 0))
		, _H(0)
		, _W(0)
	{}

	~e_matrix()
	{}

	inline int get_H() const
	{
		return this->_H;
	}
	inline void set_H(int h)
	{
		this->_H = h;
	}
	inline int get_W() const
	{
		return this->_W;
	}
	inline void set_W(int w)
	{
		this->_W = w;
	}

	inline data get(int h, int w) const
	{
		if( h >= this->get_H() || w >= this->get_W() || h < 0 || w < 0 )
		{
			//cout << "m(" << h << ", " << w << ") = " << OFFLIMITS_RESULT << endl;
			return OFFLIMITS_RESULT;
		}

		//cout << "m(" << h << ", " << w << ") = " << this->_matrix[h][w] << endl;
		return this->_matrix[h][w];
	}
	inline void set(int h, int w, data d)
	{
		if( h >= this->get_H() || w >= this->get_W() || h < 0 || w < 0 )
			return;
		this->_matrix[h][w] = d;
	}

	inline void calculate_min_neighbor(int h, int w)
	{
		static int& lh = this->_min_n_h;
		static int& lw = this->_min_n_w;
		lh = h - 1;
		lw = w;
		this->_min_n_dir = NORTH;

		if( this->get(h, w - 1) < this->get(lh, lw) )
		{
			lh = h;
			lw = w - 1;
			this->_min_n_dir = WEST;
		}

		if( this->get(h, w + 1) < this->get(lh, lw) )
		{
			lh = h;
			lw = w + 1;
			this->_min_n_dir = EAST;
		}

		if( this->get(h + 1, w) < this->get(lh, lw) )
		{
			lh = h + 1;
			lw = w;
			this->_min_n_dir = SOUTH;
		}
	}

	inline int minnh() const
	{
		return this->_min_n_h;
	}
	inline int minnw() const
	{
		return this->_min_n_w;
	}

	inline int minndir() const
	{
		return this->_min_n_dir;
	}

	inline void set_all(data d)
	{
		this->_matrix.clear();
		this->_matrix.resize(MAX, vector<data>(MAX, d));
	}

private:

private:
	e_matrix(const e_matrix&);
private:
	vector< vector<data> > _matrix;
	int _H;
	int _W;

	mutable int _min_n_h;
	mutable int _min_n_w;
	mutable char _min_n_dir;
};


char browse_for_label(int h, int w, const e_matrix<char>& IN, e_matrix<char>& OUT, char& cl)
{
	if( OUT.get(h, w) == UNLABELED )
	{
		switch(IN.get(h, w))
		{
		case NORTH:
			OUT.set(M_NORTH(h, w), browse_for_label(M_NORTH(h, w), IN, OUT, cl));
			return OUT.get(M_NORTH(h, w));
			break;

		case WEST:
			OUT.set(M_WEST(h, w), browse_for_label(M_WEST(h, w), IN, OUT, cl));
			return OUT.get(M_WEST(h, w));
			break;

		case EAST:
			OUT.set(M_EAST(h, w), browse_for_label(M_EAST(h, w), IN, OUT, cl));
			return OUT.get(M_EAST(h, w));
			break;

		case SOUTH:
			OUT.set(M_SOUTH(h, w), browse_for_label(M_SOUTH(h, w), IN, OUT, cl));
			return OUT.get(M_SOUTH(h, w));
			break;

		case SINK:
			OUT.set(h, w, cl);
			return cl++;
			break;
		}
	}

	return OUT.get(h, w);
}

char browse_for_label_non_recursive(int h, int w, const e_matrix<char>& IN, e_matrix<char>& OUT, char& cl)
{
	list< pair<int, int> > stack;
	char label;

	while( OUT.get(h, w) == UNLABELED )
	{
		stack.push_back(make_pair(h, w));
		switch(IN.get(h, w))
		{
		case NORTH:
			--h;
			break;

		case WEST:
			--w;
			break;

		case EAST:
			++w;
			break;

		case SOUTH:
			++h;
			break;

		case SINK:
			OUT.set(h, w, cl++);
			break;
		}
	}
	label = OUT.get(h, w);

	while( !stack.empty() )
	{
		OUT.set(stack.back().first, stack.back().second, label);
		stack.pop_back();
	}
	return label;
}

void label_system(const e_matrix<char>& IN, e_matrix<char>& OUT)
{
	char current_label = 'a';
	for(int h = 0; h < IN.get_H(); ++h)
	{
		for(int w = 0; w < IN.get_W(); ++w)
		{
			if( OUT.get(h, w) == UNLABELED )
			{
				if( IN.get(h, w) == SINK )
				{
					OUT.set(h, w, current_label++);
				}
				else
				{
					OUT.set(h, w, browse_for_label_non_recursive(h, w, IN, OUT, current_label));
				}
			}

		}
	}
}

int main(int argc, char** argv)
{
	int T, H, W, d;
	e_matrix<int> M;
	e_matrix<char> R, S;


//#	define __USINGFILE 1
#	if defined( __USINGFILE)
	if( argc < 2 )
	{
		cerr << "error: no input file" << endl;
		return -1;
	}
	ifstream in(argv[1]);
#	else
	istream& in = cin;
#	endif


	in >> T;
	//cout << "T: " << T << endl;
	
	
	
	for(int m = 0; m < T; ++m)
	{
		// read dimensions
		in >> H >> W;
		/*
		cout << "H: " << H << endl
			<< "W: " << W << endl;
			*/

		M.set_H(H);
		M.set_W(W);
		R.set_H(H);
		R.set_W(W);
		S.set_H(H);
		S.set_W(W);

		// read matrix
		for(int h = 0; h < H; ++h)
		{
			for(int w = 0; w < W; ++w)
			{
				in >> d;
				M.set(h, w, d);
			}
		}


		cout << "Case #" << (m+1) << ": " << endl;

		/*
		for(int h = 0; h < H; ++h)
		{
			for(int w = 0; w < W; ++w)
			{
				cout << M.get(h, w) << " ";
			}
			cout << endl;
		}*/

		// solve case
		// find drainage
		for(int h = 0; h < H; ++h)
		{
			for(int w = 0; w < W; ++w)
			{
				M.calculate_min_neighbor(h, w);
				if( M.get(h, w) <= M.get(M.minnh(), M.minnw()) )
					R.set(h, w, SINK);
				else
					R.set(h, w, M.minndir());

			}
		}

		/*
		for(int h = 0; h < H; ++h)
		{
			for(int w = 0; w < W; ++w)
			{
				cout << R.get(h, w) << " ";
			}
			cout << endl;
		}*/

		// label drain
		label_system(R, S);
		// end solving



		for(int h = 0; h < H; ++h)
		{
			cout << S.get(h, 0);
			for(int w = 1; w < W; ++w)
			{
				cout << ' ' << S.get(h, w);
			}
			cout << endl;
		}


		S.set_all(0);
	}

	return 0;
}
