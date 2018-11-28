#include<iostream> 
#include<algorithm>
#include<queue>
#include<stack>
#include<numeric>
#include<vector>
#include<sstream>
#include<string>
#include<string.h>
#include<cmath>
#include<cstdlib>
#include<map>
using namespace std;
#define eps 1e-8
#define inf (1<<30)
#define pi (2*acos(0.0))
#define all(a) a.begin(),a.end()
#define mem(a,v) memset(a,v,sizeof(a))
#define fl(a,v) fill(a.begin(),a.end(),v)
#define flo(a,begin,end,value) fill(a+begin,a+end,value)
#define flt(a,begin,end,value) fill(a[begin],a[end],value)
typedef long long LL;
//typedef __int64   LL;
typedef vector<int>vi;
typedef vector<string>vs;
typedef pair<int,int>pri;
typedef map<string,int>msi;
typedef map<vector<int>,int>mvi;
inline bool iseq(double x,double y){if(fabs(x-y)<eps)return true;return false;} 
template<typename T>inline T hpt(T x1,T y1,T x2,T y2){return hypot(x1-x2,y1-y2);}
template<typename T>inline T gcd(T a,T b){if(!b)return a;else return gcd(b,a%b);}
template<typename T>inline T bigmod(T b,T p,T m){if(!p)return 1;else if(!(p%2)){T x=bigmod(b,p/2,m);return x*x;}else return ((b%m)*bigmod(b,p-1,m))%m;}
#define PS 15
int prime[PS/32+1];
void setbit(int i){int p=i>>5,q=i&31;prime[p]|=(1<<q);}
bool checkbit(int i){int p=i>>5,q=i&31;return prime[p]&(1<<q)?true:false;}
void buildprime(int n){int i,j,k=sqrt(double(n));prime[0]=3;for(i=4;i<n;i+=2)setbit(i);for(i=3;i<=k;i+=2){if(!checkbit(i)){int ii=i+i;for(j=i*i;j<n;j+=ii)setbit(j);}}}

int sum,r,n,N,R,C,t,k,m,txt;
#define S 55
char ch[S][S],c[S][S];
bool ok(char cc,int val){
	int i,j,jj,toti=0,totj=0;
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++)if(c[i][j]==cc){
			totj=0;
			for(jj=j;jj<=n;jj++,totj++)if(c[i][jj]!=cc)break;
			if(totj>=val)return true;
		}
		for(j=1;j<=n;j++)if(c[j][i]==cc){
			toti=0;
			for(jj=j;jj<=n;jj++,toti++)if(c[jj][i]!=cc)break;
			if(toti>=val)return true;
		}
		for(j=1;j<=n;j++)if(c[i][j]==cc){
			toti=0;
			int row=i,col=j;
			for(;row<=n&&col<=n;row++,col++,toti++)if(c[row][col]!=cc)break;
			if(toti>=val)return true;
		}
		for(j=1;j<=n;j++)if(c[i][j]==cc){
			toti=0;
			int row=i,col=j;
			for(;row<=n&&col<=n;row++,col--,toti++)if(c[row][col]!=cc)break;
			if(toti>=val)return true;
		}
	}
	return false;
}
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,j;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&n,&k);
		for(i=1;i<=n;i++)scanf("%s",ch[i]+1);
		//for(i=1;i<=n;i++)puts(ch[i]+1);
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++){
			int nc=n-i+1;
			int nr=j;
			c[nr][nc]=ch[i][j];
		}
		//for(i=1;i<=n;i++)puts(c[i]+1);
		for(i=n-1;i>=1;i--)for(j=1;j<=n;j++){
			if(c[i][j]=='.')continue;
			for(m=i+1;m<=n;m++)if(c[m][j]!='.')break;
			m--;
			if(m<=n&&c[m][j]=='.')swap(c[i][j],c[m][j]);
		}
		//for(i=1;i<=n;i++)puts(c[i]+1);
		//printf("\n");
		bool fa=ok('B',k);
		bool fb=ok('R',k);
		if(fa&&fb)printf("Case #%d: Both\n",++txt);
		else if(fa)printf("Case #%d: Blue\n",++txt);
		else if(fb)printf("Case #%d: Red\n",++txt);
		else printf("Case #%d: Neither\n",++txt);
	}
	return 0;
}