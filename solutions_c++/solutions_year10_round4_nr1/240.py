#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <complex>
using namespace std;

#define ME(s) memset((s), 0, sizeof((s)))
#define MM(s,a) memset((s),(a),sizeof((s)))
#define MCP(s,a) memcpy((s), (a), sizeof(s))
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PDD pair<double, double>
#define mkp(a,b) make_pair((a),(b))
#define y first
#define x second
#define sqr(a) ((a)*(a))
#define lowbit(x) ((x)&(-(x)))
#define two(x) (1<<(x))
#define contain(mask,x) (((mask)&two(x))!=0)

#define OFFLINEJUDGE

#ifdef OFFLINEJUDGE
FILE *fin=freopen("A.in","r",stdin);
FILE *fout=freopen("A.out","w",stdout);
#else
FILE *fin=stdin;
FILE *fout=stdout;
#endif
int T,N,K,a[133][133],buf[133][133],ans;

int check(){
	vector<vector<int> > g;
	g.resize(2*K-1);
	for(int i=0;i<K;i++)
		for(int j=0;j<K;j++)
			g[i+j].push_back(a[i][j]);
/*
	for(int i=0;i<g.size();i++){
		for(int j=0;j<g[i].size();j++){
			cout << g[i][j] << "  ";
		}
		cout << endl;
	}cout << endl;
*/	

	for(int i=0;i<g.size();i++)
		for(int j=0;j<=(int)g[i].size()-1-j;j++){
			int a=g[i][j];
			int b=g[i][(int)g[i].size()-1-j];
			if(a!=-1&&b!=-1){
				if(a!=b){
				//	cout << a << "  " << b << endl;
				//	cout << j << "  " << g[i].size()-1-j << endl; 
					return 0;
				}
				else
					continue;
			}
			else if(a==-1&&b==-1)
				continue;
			else if(b==-1)
				g[i][(int)g[i].size()-1-j]=a;
			else
				g[i][j]=b;
		}
	
//	cout << "!!" << endl;
	
	vector<vector<int> > x;
	x.resize(2*K-1);
	for(int i=0;i<g.size();i++)
		for(int j=0;j<(int)g[i].size();j++)
			x[2*j+abs(K-1-i)].push_back(g[i][j]);
	
	for(int i=0;i<x.size();i++)
		for(int j=0;j<=(int)x[i].size()-1-j;j++){
			int a=x[i][j];
			int b=x[i][(int)x[i].size()-1-j];
			if(a!=-1&&b!=-1){
				if(a!=b)
					return 0;
				else
					continue;
			}
			else if(a==-1&&b==-1)
				continue;
			else if(b==-1)
				x[i][(int)x[i].size()-1-j]=a;
			else
				x[i][j]=b;
		}
	
//	cout << "!!" << endl;
	
	for(int i=0;i<(int)x.size();i++)
		for(int j=0;j<(int)x[i].size();j++)
			if(x[i][j]==-1)
				x[i][j]=1;
	
	int tot=0;
	for(int i=0;i<K;i++)
		for(int j=0;j<K;j++)
			if(a[i][j]!=-1)
				tot-=a[i][j];
	
	for(int i=0;i<x.size();i++)
		for(int j=0;j<x[i].size();j++)
			tot+=x[i][j];
	/*
	for(int i=0;i<x.size();i++){
		for(int j=0;j<x[i].size();j++){
			cout << x[i][j] << "  ";
		}
		cout << endl;
	}cout << endl;
	*/
	return 1;
}

int work(){
	for(int i=0;i+N<=K;i++)
		for(int j=0;j+N<=K;j++){
			memset(a,-1,sizeof(a));
			for(int y=0;y<N;y++)
				for(int x=0;x<N;x++)
					a[i+y][j+x]=buf[y][x];
			if(check())
				return 1;
		}
	return 0;
}

int main(){
	cin >> T;
	for(int c=0;c<T;c++){
		cin >> N;
		vector< vector<int> > g;
		for(int i=1;i<=N;i++){
			vector<int> tmp(i,0);
			for(int j=0;j<i;j++)
				cin >> tmp[j];
			g.push_back(tmp);
		}
		for(int i=N-1;i>=1;i--){
			vector<int> tmp(i,0);
			for(int j=0;j<i;j++)
				cin >> tmp[j];
			g.push_back(tmp);
		}
		/*
		for(int i=0;i<g.size();i++){
			for(int j=0;j<g[i].size();j++)
				cout << g[i][j];
			cout << endl;
		}cout << endl;
		*/
		int x=0;
		for(int i=0;i<N;i++){
			int y=0;
			for(int k=0;k<N;k++){
				buf[x][y]=g[i+k].back();
				g[i+k].pop_back();
				y++;
			}
			x++;
		}
/*		
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++)
				cout << buf[i][j];
			cout<<endl;
		}
	*/
		ans=1000000000;
		for(K=N;;K++){
			if(work()){
				ans=K*K-N*N;
				break;
			}
		}
		fprintf(fout,"Case #%d: %d\n",c+1,ans);
	}
	return 0;
}
