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
#include<stdio.h>
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

int sum,r,n,N,R,C,t,txt;
#define S 1005
int grid[50][50];
char ch[100];
int nisi[50];
void fill(int r,int c,int sz){
	for(int i=0;i<sz;i++)for(int j=0;j<sz;j++){
		grid[i+r][j+c]=2;
	}
}
int ok(int r,int c,int sz){
	int sst=grid[r][c];
	int st;
	int i,j,k;
	int tot=0;
	for(i=0;i<sz&&(i+r)<R;i++){
		
		st=grid[r+i][c];
		for(j=0;j<sz&&(j+c)<C;j++){
			if(grid[r+i][c+j]==2||grid[r+i][c+j]!=st)return 0;
			tot++;
			st=1-st;
		}
	}
	if(tot!=sz*sz)return 0;
	tot=0;
	st=grid[r][c];
	for(i=0;i<sz&&(i+r)<R;i++){
		if(grid[r+i][c]==2||grid[r+i][c]!=st)return 0;
		st=1-st;
		tot++;
	}
	if(tot!=sz)return 0;
	return 1;
}
int pari(int c){
	int tot=0;
	int i,j,k;
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			if(grid[i][j]!=2){
				if(ok(i,j,c)==0)continue;
				fill(i,j,c);
				tot++;
			}
		}
	}
	nisi[c]=tot;
	return tot;
}
int main(){
	freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int i,j,k,m;
	while(t--){
		printf("Case #%d: ",++txt);
		scanf("%d%d",&R,&C);
		for(i=0;i<R;i++){
			scanf("%s",ch);
			for(j=0,k=0;k<strlen(ch);k++){
				int val=ch[k];
				if(val>='A'&&val<='Z')val-=55;
				else val-='0';
				for(m=3;m>=0;m--){
					if(((1<<m)&val))grid[i][j++]=1;
					else grid[i][j++]=0;
				}
			}
		}
		/*for(i=0;i<R;i++){
			for(j=0;j<C;j++)printf("%d",grid[i][j]);
			printf("\n");
		}*/
		int ans=0;
		mem(nisi,0);
		for(i=min(R,C);i>=1;i--){
			if(pari(i))ans++;
		}
		printf("%d\n",ans);
		for(i=min(R,C);i>=1;i--){
			if(nisi[i]==0)continue;
			printf("%d %d\n",i,nisi[i]);
		}
	}
	return 0;
}