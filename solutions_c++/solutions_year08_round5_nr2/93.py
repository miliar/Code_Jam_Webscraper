/*
 * Util defines and templates written by me before the GCJ2008 contest started
 * Andre Susano Pinto <andresusanopinto@gmail.com>
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cfloat>
#include <queue>
#include <climits>
#include <cassert>
#include <string.h>
#define join(a,b) a##b
#define EP (1e-9)

typedef unsigned int uint32;
typedef unsigned long long uint64;

using namespace std;

template<typename T> typename T::iterator IterBegin(T &t) { return t.begin(); }
template<typename T> typename T::iterator IterEnd  (T &t) { return t.end(); }
template<typename T,int S> T* IterBegin(T (&t)[S]) { return t+0; }
template<typename T,int S> T* IterEnd  (T (&t)[S]) { return t+S; }

template<typename T> typename T::const_iterator IterBegin(const T &t) { return t.begin(); }
template<typename T> typename T::const_iterator IterEnd  (const T &t) { return t.end(); }
template<typename T,int S> const T* IterBegin(const T (&t)[S]) { return t+0; }
template<typename T,int S> const T* IterEnd  (const T (&t)[S]) { return t+S; }

template<typename T> int size(const T &t) { return t.size(); }
template<typename T, int S> int size(const T (&t) [S]) { return S; }

#define FOREACH(col, iter, end) for(__typeof( IterBegin(col) ) iter = IterBegin(col), end=IterEnd(col); iter != end; iter++)
#define foreach(col, iter) FOREACH(col, iter, join(iter, __end))
#define all(col)    IterBegin(col), IterEnd(col)

#define x first
#define y second

template<typename T> T read()
{
	T t;
	cin >> t;
//	cerr << "read: " << t << endl;
	return t;
}

int readtime()
{
	int a, b;
	char t;
	cin >> 	a >> t >> b;
	return a*60 + b;
}

string readline()
{
	string line;
	getline(cin, line);
	return line;
}

template <typename T> inline void reset(T &t, const T &val) { t = val; }
template <typename T, int S> void reset(T (&t) [S], const T &val)
{
	for(int i=0; i<S; i++) reset(t[i], val);
}

vector<string> parse_strings(const string &s)
{
	istringstream is( s);
	string t;
	vector<string> vs;
	while(is >> t) vs.push_back(t);
	return vs;
}

void solve();

int main()
{
	int cases;
	cin >> cases; cin.ignore();
	for(int i=1; i<=cases; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}


/*
 * Code itself
 */
struct State
{
	int x, y;
	int px, py;	

	State(int _x, int _y, int _px, int _py)
	{
		x = _x;
		y = _y;
		px = _px;
		py = _py;
	}

	State()
	{
	}

};
const int delta[][2] = { { 0, 1}, {-1, 0}, {0, -1}, {1, 0} };

#define MS 100
char field[MS][MS];
queue< State > q;

int seen[MS][MS][MS][MS];
int time_to_wall[MS][MS][4];
State cake, start;



void process(const State &s, int t, bool loop = true)
{
//	cout << t << "===> " << s.x << ", " << s.y << ": " << s.px << " " << s.py << endl;
	if(s.x == cake.x && s.y == cake.y)
	{
		cout << t << endl;
		throw 0;
	}

	if( field[s.y][s.x] != '.')
	{
		cout << int(field[s.y][s.x]) << endl;
		assert(field[s.y][s.x] == '#');
		return;
	}

	if(seen[s.x][s.y][s.px][s.py] != -1) return;

//	cout << t << "===> " << s.x << ", " << s.y << ": " << s.px << " " << s.py << endl;
	q.push(s);
	
	seen[s.x][s.y][s.px][s.py] = t;

	if(loop)
	{
		for(int i=0; i<4; i++)
		{
			process( State( s.x, s.y,
					s.x + delta[i][0]*time_to_wall[s.x][s.y][i],
					s.y + delta[i][1]*time_to_wall[s.x][s.y][i]
					),
					t,
					false
				);
		}
	}
}

void solve()
{
	int lines, width;

	cin >> lines >> width;

	q = queue<State>();

	memset(field, '#', sizeof(field));
	memset(seen, -1, sizeof(seen));
//int time_to_wall[50][50][4];
//State cake;

	for(int i=1; i<=lines; i++)
	{
		cin >> (field[i]+1);
	}
	
//	cerr << endl;
	for(int i=0; i<=lines+1; i++)
	{
		field[i][width+1] = '#';
		field[i][width+2] = 0;
//		cerr << field[i] << endl;

		for(int j=1; j<=width; j++)
		if(field[i][j] == 'O')
		{
			field[i][j] = '.';
			start.y = i;
			start.x = j;
			start.px = j;
			start.py = i;
		}
		else if(field[i][j] == 'X')
		{
//			printf("here\n");
			field[i][j] = '.';
			cake.y = i;
			cake.x = j;
		}
		else
		{
//			cerr << int(field[i][j]) << endl;
			assert( field[i][j] == '.'|| field[i][j] == '#' );
		}
	}

/*
	cerr << endl;
	for(int i=0; i<=lines+1; i++)
	{
		cerr << field[i] << endl;
	}
*/
	for(int i=1; i<=lines; i++)
	for(int j=1; j<=width; j++)
	for(int k=0; k<4; k++)
	{
		for(int t = 0; ; t++)
		{
			int nx = j+t*delta[k][0];
			int ny = i+t*delta[k][1];

			if(field[ny][nx] == '#')
			{
				time_to_wall[j][i][k] = t-1;
				break;
			}
		}
	}

/*
	for(int k=0; k<4; k++)
	{
		cerr << endl;
		for(int i=1; i<=lines; i++)
		{
			for(int j=1; j<=width; j++)
				cerr << time_to_wall[j][i][k];
		cerr << endl;

		}
	}
*/

	process( start, 0);

//	cerr << "-------------------\n---------------\n---------------\n" << endl;
	try
	{

		while(!q.empty())
		{
			State s = q.front();
			q.pop();

			int t = seen[s.x][s.y][s.px][s.py];
//			cout << t << ":  " << s.x << ", " << s.y << ": " << s.px << " " << s.py << endl;

			for(int i=0; i<4; i++)
			{
				int nx =  s.x + delta[i][0], ny =  s.y + delta[i][1];
				if(field[ny][nx] == '#')
					process( State( s.px, s.py, s.px, s.py ), t +1 );
				else
					process( State( nx, ny, s.px, s.py ), t + 1);
			}
		}

	}
	catch(int i)
	{
		return;
	}

	cout << "THE CAKE IS A LIE" << endl;
}

