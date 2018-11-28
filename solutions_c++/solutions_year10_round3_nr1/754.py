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
bool nisi[S];
struct str{int x,y;}var[S];
bool comp(const str &p,const str &q){
	if(p.x!=q.x)return p.x<q.x;
	return p.y<q.y;
}
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int i,j,k;
	while(t--){
		printf("Case #%d: ",++txt);
		scanf("%d",&n);
		for(i=1;i<=n;i++){
			scanf("%d%d",&var[i].x,&var[i].y);
		}
		sort(var+1,var+n+1,comp);
		int ans=0;
		mem(nisi,0);
		for(i=1;i<=n;i++){
			nisi[i]=true;
			for(j=1;j<=n;j++){
				if(i==j)continue;
				if(nisi[j])continue;
				int mx=max(var[i].x,var[i].y);
				int mn=min(var[i].x,var[i].y);
				int a=var[j].x;
				int b=var[j].y;
				if(var[i].x<=var[i].y){
					if(b<=mx&&a>=mn){
						nisi[j]=true;
						ans++;
					}
					else if(b>mx&&a<mn){
						nisi[j]=true;
						ans++;
					}
				}
				else{
					if(b>=mx&&a<=mx){
						nisi[j]=true;
						ans++;
					}
					else if(b<=mn&&a>=mx){
						nisi[j]=true;
						ans++;
					}
				}
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}