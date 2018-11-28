#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <sstream>
#include <set>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <bitset>

#define f(i, n)             for(int i = 0; i < n; i++)
#define s(n)				scanf("%d",&n)
#define sl(n) 				scanf("%lld",&n)
#define sf(n) 				scanf("%lf",&n)
#define sc(n)               scanf("%s", &n)    
#define fill(a,v) 			memset(a, v, sizeof a)
#define ull 				unsigned long long
#define ll 					long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb          		push_back
#define gcd					__gcd
#define inf (int)1e9
#define gc getchar
#define maxn (int)1e6
using namespace std;

inline void ss(int &n)
{
     n = 0;
     char c = gc();
     while(c < 48 || c > 57) c = gc();
     while(c >= 48 && c <= 57) n = (n << 1) + (n << 3) + c - 48, c = gc();
}

struct state
{
	int com, x, y, t;
	state(){}
	state(int C, int X, int Y, int T)
	{
		com = C;
		x = X;
		y = Y;
		t = T;
	}
	
	bool operator < (const state &s) const
	{
		return t < s.t;
	}
};

const int mxn = 110;
int vis[mxn][mxn][mxn], but[mxn], n;
char col[mxn];
int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1}, dy[] = {-1, 1, 0, -1, 1, -1, 1, 0};

int main()
{
	//freopen("in.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t;
	s(t);
	for(int test = 1; test <= t; test++)
	{
		s(n);
		f(i, n) cin >> col[i] >> but[i];
		//scanf("%c %d", &col[i], &but[i]);
		
		queue <state> q;
		q.push( state(0, 1, 1, 0) );
		
		while(!q.empty())
		{
			state cur = q.front(); q.pop();
			
			//printf("Pop (%d %d %d : %d)\n", cur.com, cur.x, cur.y, cur.t);
			if(cur.com == n)
			{
				printf("Case #%d: %d\n", test, cur.t);
				break;
			}
			
			if(vis[cur.com][cur.x][cur.y] == test) continue;
			vis[cur.com][cur.x][cur.y] = test;
			
			f(i, 8)
			{
				int c = cur.com;
				int cx = cur.x + dx[i];
				int cy = cur.y + dy[i];
				if(cx < 1 || cy < 1 || cx > 100 || cy > 100 || vis[c][cx][cy] == test) continue;
				if( (!dx[i] && col[c] == 'O' && but[c] == cx) || (!dy[i] && col[c] == 'B' && but[c] == cy) )
					if(vis[c + 1][cx][cy] != test)
					{
						//printf("Push2: (%d %d %d : %d)\n", c + 1, cx, cy, cur.t + 1);
						q.push( state(c + 1, cx, cy, cur.t + 1) );
					}
				
				q.push( state(c, cx, cy, cur.t + 1) );
				//printf("Push (%d %d %d : %d)\n", c, cx, cy, cur.t + 1);
			}
			
			int c = cur.com;
			if(col[c] == 'O' && but[c] == cur.x) c++;
			else if(col[c] == 'B' && but[c] == cur.y) c++;
			if(vis[c][cur.x][cur.y] != test)
			{
				q.push( state(c, cur.x, cur.y, cur.t + 1) );
				//printf("Push (%d %d %d : %d)\n", c, cur.x, cur.y, cur.t + 1);
			}
			//puts("");
		}
		
	}
}
