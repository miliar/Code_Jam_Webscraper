#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<numeric>
#include<vector>
#include<set>
#include<sstream>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<map>
using namespace std;
#define eps 1e-8
#define inf (1<<30)
#define pi (2*acos(0.0))
#define all(a) a.begin(),a.end()
#define mem(a,v) memset(a,v,sizeof(a))
#define rep(i,b,e) for((i)=(b);(i)<(e);(i)++)
#define rev(i,b,e) for((i)=(e-1);(i)>=(b);(i)--)
#define fi(b,e) for((i)=(b);(i)<(e);(i)++)
#define fj(b,e) for((j)=(b);(j)<(e);(j)++)
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
template<typename T>inline void extended_euclid(T a,T b,T &x,T &y){if(a%b==0)x=0,y=1;else{extended_euclid(b,a%b,x,y);T temp=x;x=y;y=-y*(a/b)+temp;}}
template<typename T>inline T bigmod(T b,T p,T m){if(!p)return 1;else if(!(p%2)){T x=bigmod(b,p/2,m);return x*x;}else return ((b%m)*bigmod(b,p-1,m))%m;}
#define PS 5
int prime[PS/32+1];
void setbit(int i){int p=i>>5,q=i&31;prime[p]|=(1<<q);}
bool checkbit(int i){int p=i>>5,q=i&31;return prime[p]&(1<<q)?true:false;}
void buildprime(int n){int i,j,k=sqrt(double(n));prime[0]=3;for(i=4;i<n;i+=2)setbit(i);for(i=3;i<=k;i+=2){if(!checkbit(i)){int ii=i+i;for(j=i*i;j<n;j+=ii)setbit(j);}}}

int sum,r,n,N,R,C,t,txt;
#define S 55
char F[S][S];
bool possible(int x,int y){
    int xx=x,yy=y;
    F[x][y]='/';
    yy+=1;
    if(yy<0||yy>=C)return false;
    if(F[xx][yy]!='#')return false;
    F[xx][yy]='\\';
    xx+=1;
    if(xx<0||xx>=R)return false;
    if(F[xx][yy]!='#')return false;
    F[xx][yy]='/';

    yy-=1;
    if(yy<0||yy>=C)return false;
    if(F[xx][yy]!='#')return false;
    F[xx][yy]='\\';
    return true;
}
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,j,k;
	scanf("%d",&t);
	while(t--){
	    scanf("%d%d",&R,&C);
	    for(i=0;i<R;i++)scanf("%s",F[i]);
	    bool flag = true;
	    for(i=0;i<R;i++)for(j=0;j<C;j++)if(F[i][j]=='#'){
	        flag=possible(i,j);
	        if(flag==false)break;
	    }
	    printf("Case #%d:\n",++txt);
	    if(flag==false)printf("Impossible\n");
	    else{
	        //trans
	        for(i=0;i<R;i++)puts(F[i]);
	    }
	}
	return 0;
}
