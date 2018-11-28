#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
#include <deque>
#include <set>
#include <algorithm>

using namespace std;

#define FOR(a,start,end) for(int a = int(start); a < int(end); a++)
#define INF INT_MAX
#define MSG(a) cout << #a << " = " << a << endl;
#define ITOA(a) char c[500];  sprintf(c,"%d",a);  string s(c);
#define PB push_back
#define SORT(a) sort(a.begin(),a.end())
#define REV(a) reverse(a.begin(),a.end())
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

const double EPS = 1e-10;
const double PI = 3.14159265358979323846264338328;

struct state
{
	vector<int> x;
	vector<int> y;
	  bool operator==(const state &a) const
   {      return (x == a.x && y == a.y);    }
   bool operator<(const state &a) const
   {      return (x < a.x || (x == a.x && y < a.y));     }

	
};

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

map<state, int> memo;

char G[12][12];

int main()
{
	ofstream fout("A-large.out");
	ifstream fin("A-large.in");

	
	int T;
	fin >> T;
	for(int tt = 0; tt < T; tt++)
	{
		cout << tt << endl;
		
		memo.clear();
		
		int N, M;
		fin >> N >> M;
		for(int p = 0; p < N; p++)
		for(int q = 0; q < M; q++)
			fin >> G[p][q];
		
		state start;
		state end;
		
		for(int p = 0; p < N; p++)
		for(int q = 0; q < M; q++)
		{
			if(G[p][q] == 'x' || G[p][q] == 'w')
				end.x.PB(p), end.y.PB(q);
			if(G[p][q] == 'o' || G[p][q] == 'w')
				start.x.PB(p), start.y.PB(q);
			if(G[p][q] != '#')
				G[p][q] = '.';
		}
		
		
		
	//		FOR(u,0,end.x.size())
		//		fout << end.x[u] << " " << end.y[u] << endl;
		//	fout << endl;
			
		
		int ans = -1;
		
		memo[start] = 0;
		
		deque<state> Q;
		Q.PB(start);
		while(Q.empty() == 0)
		{
			state k = Q[0];
			Q.pop_front();
			
			if(k.x == end.x && k.y == end.y)
			{
				ans = memo[k];
				break;
			}
			
//			FOR(u,0,k.x.size())
//				fout << k.x[u] << " " << k.y[u] << endl;
//			fout << endl;
			
			
			int nextstable = 0;
			
			bool mark[5] = {0,0,0,0,0};
			mark[0] = 1;
			deque<int> Q2;
			Q2.PB(0);
			while(Q2.empty() == 0)
			{
				int n = Q2[0];
				Q2.pop_front();
				FOR(p,0,k.x.size())
				if(mark[p] == 0)
				{
					if(abs(k.x[p]-k.x[n]) + abs(k.y[p]-k.y[n]) == 1)
					{
						Q2.PB(p);
						mark[p] = 1;
					}
				}
			}
			
			
			int BAD = 0;
			FOR(t,0,k.x.size())
				if(mark[t] == 0)
					BAD = 1;
			if(BAD == 1)
				nextstable = 1;
			
//			fout << nextstable << endl;
			
			FOR(t,0,k.x.size())
			FOR(p,0,4)
			{
				//move box t in direction p

				int prevx = k.x[t]-dx[p];
				int prevy = k.y[t]-dy[p];
				int nextx = k.x[t]+dx[p];
				int nexty = k.y[t]+dy[p];
				
				if(prevx < 0 || prevx >= N || prevy < 0 || prevy >= M ||
				nextx < 0 || nextx >= N || nexty < 0 || nexty >= M ||
				G[prevx][prevy] != '.' || G[nextx][nexty] != '.') continue;
				
				int bad = 0;
				FOR(u,0,k.x.size())
					if(u != t)
					{
						if(k.x[u] == prevx && k.y[u] == prevy)
						{
							bad = 1; break;
						}
						if(k.x[u] == nextx && k.y[u] == nexty)
						{
							bad = 1; break;
						}
					}
					
				if(bad == 1) continue;
						
				state target = k;
				target.x[t] += dx[p], target.y[t] += dy[p];
				
				
				
				FOR(u,0,target.x.size())
				FOR(v,0,u)
					if(target.x[u] < target.x[v] || 
					(target.x[u] == target.x[v] && target.y[u] < target.y[v]))
					{
						swap(target.x[u],target.x[v]);
						swap(target.y[u],target.y[v]);
						
					}						
				
				
				
				if(memo.find(target) != memo.end()) continue;
			
				int BADD = 0;
				
			
				if(nextstable == 1)
				{
					//check if target is stable
				
					bool MARK[5] = {0,0,0,0,0};
					MARK[0] = 1;
					deque<int> Q3;
					Q3.PB(0);
					while(Q3.empty() == 0)
					{
						int nn = Q3[0];
						Q3.pop_front();
						FOR(p,0,k.x.size())
						if(MARK[p] == 0)
						{
							if(abs(target.x[p]-target.x[nn]) + abs(target.y[p]-target.y[nn]) == 1)
							{
								Q3.PB(p);
								MARK[p] = 1;
							}
						}
					}
					
					FOR(t,0,k.x.size())
						if(MARK[t] == 0)
							BADD = 1;
				}
				
				if(BADD == 0)
				{
					Q.PB(target);
					memo[target] = memo[k] + 1;
				}
			}
			
		}
				
		fout << "Case #" << tt+1 << ": " << ans << endl;					
			






	}
		
	return 0;
}
		
