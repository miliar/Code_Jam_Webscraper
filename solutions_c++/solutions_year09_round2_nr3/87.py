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
struct st{
	int i,j,sum;
	char c;
	st(){}
	st(int ii,int jj,int s2){
		i=ii;
		j=jj;
		sum=s2;
	}
	bool operator <(const st &s2)const{
		return mp(sum,mp(i,j))<mp(s2.sum,mp(s2.i,s2.j));
	}
};
bool comp(const st &a,const st &b){
	return a.c<b.c;
}
map<st,string> path;
bool comp2(const st &a,const st &b){
	return path[a]<path[b];
}
set<st> vis;
map<st,st> p;
queue<st> q;
int n,N,Q,qq;
string s[20];
int di[]={1,-1,0,0};
int dj[]={0,0,1,-1};
st bfs(int need){
	vis.clear();
	p.clear();
	path.clear();
	q=queue<st>();
	vector<st> v;
	rep(i,n)
		rep(j,n)
			if(isdigit(s[i][j])){
				st tt=st(i,j,s[i][j]-'0');
				tt.c=s[i][j];
				v.pb(tt);
			}
	sort(all(v),comp);
	rep(i,v.sz){
		q.push(v[i]);
		string s2="";
		s2+=v[i].c;
		path[v[i]]=s2;
		vis.insert(v[i]);
	}
	while(!q.empty()){
		int size=q.sz;
		vector<st> v2;
		rep(xx,size){
			st t=q.front();
			q.pop();
			if(t.sum==need)
				return t;
			rep(k,4){
				int ni=t.i+di[k];
				int nj=t.j+dj[k];
				if(ni>=0 && nj>=0 && ni<n && nj<n){
					st nt(ni,nj,t.sum);
					nt.c=s[ni][nj];
					if(isdigit(nt.c)){
						if(t.c=='+')
							nt.sum+=nt.c-'0';
						else
							nt.sum-=nt.c-'0';
					}
					if(vis.insert(nt).second){
						p[nt]=t;
						string s22=path[t];
						s22+=s[ni][nj];
						path[nt]=s22;
						v2.pb(nt);
					}
				}
			}
		}
		sort(all(v2),comp2);
		rep(i,v2.sz)
			q.push(v2[i]);
	}
	return st();
}
void get(const st &t){
	map<st,st>::iterator it=p.find(t);
	if(it!=p.end())
		get(it->second);
	cout<<s[t.i][t.j];
}
int main() {
//#define SAMPLE
#ifndef SAMPLE
	freopen("C-small-attempt4.in","rt",stdin);
	freopen("C-small-attempt4.out","wt",stdout);
#endif
#ifdef SAMPLE
	freopen("a.txt", "rt", stdin);
#endif
	cin>>N;
	rep(nn,N){
		cout<<"Case #"<<nn+1<<":"<<endl;
		cin>>n>>Q;
		rep(i,n)
			cin>>s[i];
		rep(i,Q){
			cin>>qq;
			cout<<path[bfs(qq)];
			cout<<endl;
		}
	}
	return 0;
}
