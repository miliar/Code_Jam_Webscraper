#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <list>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define rep2(i,x,m) for(int i=x;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
int oo = (int) 1e9;

#define SMALL
//#define LARGE

int N,X;
string maze[40];
int x[40];
int bfs(){
	queue<vi> q;
	set<vi> vis;
	vi t;
	rep(i,X)
		t.pb(i);
	q.push(t);
	vis.insert(t);
	int ret=0;
	while(!q.empty()){
		int size=q.sz;
		while(size--){
			t=q.front();
			q.pop();
			rep(i,X)
				if(x[t[i]]>i)
					goto END;
			return ret;
			END:;
			rep(i,X-1){
				vi nt=t;
				swap(nt[i],nt[i+1]);
				if(vis.insert(nt).second)
					q.push(nt);
			}
		}
		ret++;
	}
	return -1;
}
int main() {
	freopen("a.txt","rt",stdin);
	#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	#endif
	#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	#endif

	cin>>N;
	rep(nn,N){
		cin>>X;
		rep(i,X){
			cin>>maze[i];
			x[i]=-1;
			rep(j,X)
				if(maze[i][j]=='1')
					x[i]=j;
		}
		cout<<"Case #"<<nn+1<<": "<<bfs()<<endl;
	}

	return 0;
}
