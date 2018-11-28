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

int a[200][200];
int r[200][100];
int n,k;
VI v;
int vsz;
bool CHK(int i,int j){
	if(i==j)	return false;
	F(l,k)	if(r[i][l]==r[j][l])	return false;
	if(r[i][0]>r[j][0]){
		F(l,k)	if(r[i][l]<r[j][l])	return false;
	}
	else{
		F(l,k)	if(r[i][l]>r[j][l])	return false;
	}
	return true;
}
int b[200];
int fin;
int mem[1<<16][16];
const int INF=300;
int used[300];
int fn(int mask,int pos){
	if(mask==fin)	return 1;
	if(pos>n)	return INF;
	int &ret=mem[mask][pos-1];
	if(ret!=-1)	return ret;
	ret=INF;
	FF(i,pos,n){
		if(!used[i] && a[pos-1][i]){
			used[i]=1;
			ret=min(ret,fn(mask|(1<<i),i+1));
			used[i]=0;
		}
	}
	F(i,n){
		if(!used[i]){
			used[i]=1;
			ret=min(ret,1+fn(mask|(1<<i),i+1));
			used[i]=0;
		}
	}
	return ret;
}
void _swap(int i,int j){
	F(l,k)	swap(r[i][l],r[j][l]);
}
int main(){
	int t;
	cin>>t;
	int cas=1;
	while(t--){
		cout<<"Case #"<<cas++<<": ";
		cin>>n>>k;
		F(i,n)F(j,k)	cin>>r[i][j];
		CLR(a,0);
		F(i,n)FF(j,i+1,n)	if(r[i][0]>r[j][0])	_swap(i,j);
		F(i,n)F(j,n)		if(CHK(i,j))	a[i][j]=1;
		v.clear();
		int mx=(1<<n);
		fin=mx-1;
		FF(i,1,1){
			CLR(b,0);
			int j=i,l=0;
			while(j){
				if(j&1)	b[l]=1;
				l++;
				j>>=1;
			}
			bool ok=true;
			F(ii,n){
				if(!b[ii])	continue;
				FF(jj,ii+1,n){
					if(!b[jj])	continue;
					if(!a[ii][jj]){
						ok=false;
						break;
					}
				}
				if(!ok)	break;
			}
			if(ok)	v.PB(i);
		}
		vsz=v.size();
		CLR(used,0);
		CLR(mem,-1);
		used[0]=1;
		cout<<fn(1,1)<<endl;
	}
	return 0;
}
