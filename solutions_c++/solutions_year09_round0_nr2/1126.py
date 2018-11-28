/*	SURENDRA KUMAR MEENA	*/
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
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<int,int> PI;
#define MP(x,y) make_pair(x,y)
#define f first
#define s second
#define VP vector<PI>
#define S(t)	scanf("%d",&t)

int a[102][102],mem[102][102],pos[30][2],tot;
char val[102][102];
int h,w;
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
bool Valid(int i,int j){
	return (i>=0 && j>=0 && i<h && j<w);
}

int fn(int i,int j){
	int &ret=mem[i][j];
	if(ret!=-1)	return ret;
	int mn=a[i][j],fq=0,dr,dc;
	F(k,4){
		int ii=i+dx[k];
		int jj=j+dy[k];
		if(Valid(ii,jj)){
			if(a[ii][jj]<mn){
				mn=a[ii][jj];fq=1;
				dr=ii;dc=jj;
			}
			else if(a[ii][jj]==mn)	fq++;
		}
	}
	if(mn==a[i][j]){
		pos[tot][0]=i;
		pos[tot][1]=j;
		return ret=tot++;
	}
	return ret=fn(dr,dc);
}

int main(){
	int t;
	cin>>t;
	FF(cas,1,t+1){
		cin>>h>>w;
		F(i,h)F(j,w)	cin>>a[i][j];
		memset(mem,-1,sizeof(mem));
		memset(val,'0',sizeof(val));
		char ch='a';
		tot=0;
		F(i,h)F(j,w){
			if(mem[i][j]==-1)	mem[i][j]=fn(i,j);
			if(val[pos[mem[i][j]][0]][pos[mem[i][j]][1]]=='0')	val[pos[mem[i][j]][0]][pos[mem[i][j]][1]]=ch++;
			val[i][j]=val[pos[mem[i][j]][0]][pos[mem[i][j]][1]];
		}
		cout<<"Case #"<<cas<<":\n";
		F(i,h){
			F(j,w){
				if(j)	cout<<" ";
				cout<<val[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}
