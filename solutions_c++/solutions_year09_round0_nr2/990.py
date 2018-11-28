#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
#include <memory.h> 

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT((c)), (c).erase(unique(ALL((c))), (c).end())
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second

typedef pair<int,int> ii;
typedef vector<int > vi;
typedef vector<vi > vvi;
typedef vector<ii  > vii;
typedef vector<vii  > vvii;
typedef long long ll;

string filename = "test";

int mem[200][200];
int res[200][200];
char out[200][200];

int m, n;
int mx = 100000;
int color = 0;

int dy[] = {0, -1, 1, 0};
int dx[] = {-1, 0, 0, 1};

void go(int r, int c)
{
	res[r][c] = color;
	
	REP(k, 4)
	{
		int nr = r + dx[k],
			nc = c + dy[k];
		if (nr < 0 || nr >= m || nc < 0 || nc >= n || res[nr][nc] != -1)
			continue;

		int mval = mx;
		int mr = -1, mc = -1;

		REP(kk, 4)
		{
			int nrr = nr + dx[kk],
				ncc = nc + dy[kk];
			if (nrr < 0 || nrr >= m || ncc < 0 || ncc >= n || mem[nrr][ncc] >= mem[nr][nc])
				continue;
			if (mval > mem[nrr][ncc])
			{
				mval = mem[nrr][ncc];
				mr = nrr;
				mc = ncc;
			}
		}

		if (mr == r && mc == c)
			go(nr, nc);
	}
}

int main()
{	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	int T;
	cin>>T;

	REP(t, T)
	{
		memset(mem, 0, sizeof(mem));
		cin>>m>>n;
		REP(i,m)REP(j,n)
			cin>>mem[i][j];

		memset(res, -1, sizeof(res));

		color = 0;

		while(1)
		{
			int mr = -1, mc = -1;
			REP(i, m)REP(j, n)
				if (res[i][j] == -1)
				{
					if (mr == -1)
					{
						mr = i; mc = j;
					}
					else
						if (mem[mr][mc] > mem[i][j])
						{
							mr = i; mc = j;
						}
				}

			if (mr == -1)
				break;

			go(mr, mc);
			color++;
		}

		char letter = 'a';
		map<int, char> mapa;

		REP(i, m)REP(j,n)
		{
			if (res[i][j] == -1)
				return 1;
			if (!mapa.count(res[i][j]))
			{
				mapa[res[i][j]] = letter;
				letter = (char)(letter + 1);
			}
			out[i][j] = mapa[res[i][j]];
		}

		cout<<"Case #"<<t+1<<":"<<endl;
		REP(i, m)
		{
			REP(j, n)
			{
				if (j)
					cout<<" ";
				cout<<out[i][j];
			}
			cout<<endl;
		}
	}

	return 0;
}