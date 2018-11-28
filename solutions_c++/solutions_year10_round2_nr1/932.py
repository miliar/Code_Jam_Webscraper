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

int sum,r,N,R,C,t,txt,n,m;
#define S 1005
map<string,int>mp;
string a,b,c,d;
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int i,j,k;
	while(t--){
		scanf("%d%d",&n,&m);
		mp.clear();
		for(i=1;i<=n;i++){
			cin>>a;
			mp[a]++;
			for(j=a.size()-1;j>=0;j--){
				if(a[j]=='/'){
					b=a.substr(0,j);
					mp[b]++;
				}
			}
		}
		int ans=0;
		for(i=1;i<=m;i++){
			cin>>a;
			if(mp[a])continue;
			mp[a]++;
			if(a!="")ans++;
			for(j=a.size()-1;j>=0;j--){
				if(a[j]=='/'){
					b=a.substr(0,j);
					if(mp[b])continue;
					mp[b]++;
					if(b!="")ans++;
				}
			}
		}
		printf("Case #%d: %d\n",++txt,ans);

	}
	return 0;
}