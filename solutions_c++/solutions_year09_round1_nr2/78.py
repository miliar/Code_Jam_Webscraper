#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cmath>

using namespace std;

#define RP(i,j,k) for(int i=j; i<k; ++i)
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;
#define MP make_pair

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a.first<<"," << a.second;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

ll s[50][50], w[50][50], t[50][50], a[50][50];
int N,M;

//check
int dx[][2]={
	{-1,0},
	{0,1},
	{1,0},
	{0,-1}
};

int dy[][2]={
	{0,1},
	{1,0},
	{0,-1},
	{-1,0}
};

int cb(pair<int,int> p)
{
	return (p.first >=0 && p.first <N && p.second >=0 && p.second < M);
}

int main()
{
	int C;
	cin >> C;
	for(int cs=1; cs<=C; ++cs)
	{
		ll res=-1;
		cin >> N >> M;
		RP(i,0,N) RP(j,0,M) {
			cin >> s[i][j] >> w[i][j] >> t[i][j];
			a[i][j]=s[i][j]+w[i][j];
			t[i][j]%=a[i][j];
			t[i][j]-=a[i][j];
		}
		
		priority_queue<pair<ll, pair<int, pair<int,int > > > > q;
		set<pair<int, pair<int,int > > > v;
		q.push(MP((ll)0, MP(0,MP(N-1,0))));
		//P(N) P(M)
		while(!q.empty())
		{
			if(v.count(q.top().second)) {q.pop(); continue;}
			v.insert(q.top().second);
			ll dist=-q.top().first;
			int dir=q.top().second.first;
			int x=q.top().second.second.first;
			int y=q.top().second.second.second;
			int nd;
			
			//P(q.top());
			q.pop();
			
			if(x==0 && y==M-1 && dir ==2) { res=dist; break;}
			
			pair<ll, pair<int, pair<int,int > > > p;
			//walk between
			nd=(dir+3)%4;
			p=MP(-dist-2, MP(nd, MP(x+dx[nd][0],y+dy[nd][0])));
			if(cb(p.second.second))
			q.push(p);
			
			nd=(dir+1)%4;
			p=MP(-dist-2, MP(nd, MP(x+dx[nd][1],y+dy[nd][1])));
			if(cb(p.second.second))
			q.push(p);
			
			//Cross road
			ll nextn, nextw;
			if((dist-t[x][y])%a[x][y] <s[x][y]) {
				nextn=dist;
				nextw=dist-(dist-t[x][y])%a[x][y]+s[x][y];
			}
			else
			{
				nextn=dist-(dist-t[x][y])%a[x][y]+a[x][y];
				nextw=dist;
			}
			
			if(dir%2) swap(nextn,nextw);
			nd=(dir+3)%4;
			p=MP(-nextw-1, MP(nd, MP(x,y)));
			q.push(p);
			
			nd=(dir+1)%4;
			p=MP(-nextn-1, MP(nd, MP(x,y)));
			q.push(p);
			
		}
		
		cout << "Case #" << cs << ": " << res;
		
		cout << endl;
	}
	
	return 0;
}
