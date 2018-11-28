#include <map>
#include <set>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define xx first
#define yy second
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////
string testname="c-small-attempt0";
int n,m,r;
vector<int> g[2000];
vector<int> v[2000];
void rec(vector<int> &vertices){
	int has[2000];
	memset(has,-1,sizeof(has));
	for (int i=0;i<vertices.size();i++)
		has[vertices[i]]=i;
	vector<int> left,right;
//	system("pause");
	for (int i=0;i<n;i++){
		if (has[i]==-1) continue;
		for (int j=0;j<v[i].size();j++){
			if (has[v[i][j]]==-1) continue;
			int x=has[i],y=has[v[i][j]];
			if (x>y) swap(x,y);
			if (x==0&&y==vertices.size()-1||x+1==y) continue;
			int k=x;
			do{
				left.pb(vertices[k]);
				k++;
				if (k==vertices.size()) k=0;		
			}while(k!=y);
			left.pb(vertices[y]);
			k=y;
			do{
				right.pb(vertices[k]);
				k++;
				if (k==vertices.size()) k=0;
			}while(k!=x);
			right.pb(vertices[x]);
/*			printf("SPLITTING ");
			for (int i=0;i<vertices.size();i++)
				printf("%d ",vertices[i]); printf("\n");
			printf("() = %d %d\n",i,v[i][j]);
			for (int i=0;i<left.size();i++)
				printf("%d ",left[i]); printf("\n");
			for (int i=0;i<right.size();i++)
				printf("%d ",right[i]); printf("\n");*/
			rec(left);
			rec(right);
			return;
		}
	}
	g[r]=vertices;
	r++;
}
vector<int> best;
int bestcolor;
int c[2000];
void print(set<int> &s){
	for (set<int>::iterator it=s.begin();it!=s.end();it++)
		printf("%d ",*it); printf("\n");
}
void color(int at,int maxcolor){
	if (at==n){
//		for (int i=0;i<n;i++)
//			printf("%d ",c[i]); printf("\n");
		set<int> used;
		for (int i=0;i<n;i++)
			used.insert(c[i]);
//		printf("USED = "); print(used);
		bool ok=true;
		for (int i=0;i<r;i++){
			set<int> cur;
			for (int j=0;j<g[i].size();j++)
				cur.insert(c[g[i][j]]);
//			printf("CUR = "); print(cur);
			if (cur!=used) ok=false;
		}
		if (ok&&(int)used.size()>bestcolor){
			bestcolor=used.size();
			best.clear();
			for (int i=0;i<n;i++)
				best.pb(c[i]);
		}
		return;
	}
	for (int i=0;i<maxcolor;i++){
		c[at]=i;
		color(at+1,maxcolor);
	}
}
void run_sol(int casenr){
	scanf("%d%d",&n,&m);
	for (int i=0;i<n;i++) v[i].clear(),g[i].clear();
	vector<int> ls,rs;
	for (int i=0;i<m;i++){ int x; scanf("%d",&x); ls.pb(x-1); }
	for (int i=0;i<m;i++){ int x; scanf("%d",&x); rs.pb(x-1); }
	for (int i=0;i<m;i++)
		v[ls[i]].pb(rs[i]);
	vector<int> vertices;
	for (int i=0;i<n;i++) vertices.pb(i);
	r=0;
	rec(vertices);
	printf("Case #%d: ",casenr);
	if (r==1) { printf("%d\n",n); return; }
	int col=n;
	for (int i=0;i<r;i++) col<?=g[i].size();
/*	for (int i=0;i<r;i++){
		for (int j=0;j<g[i].size();j++)
			printf("%d ",g[i][j]);
		printf("\n");
	}*/
	bestcolor=-1;
	color(0,col);
	printf("%d\n",bestcolor);
	for (int i=0;i<best.size();i++){
		printf("%d",best[i]+1);
		if (i+1<best.size()) printf(" ");
		else printf("\n");
	}
}
int main(){
	freopen((testname+".in").c_str(),"r",stdin);
	freopen((testname+".out").c_str(),"w",stdout);
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
		run_sol(t);
//	system("pause");
	return 0;
}
