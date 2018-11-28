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
#include<stdio.h>
#include<cmath>
#include<cstdlib>
#include<map>
using namespace std;
#define eps 1e-8
#define inf (1<<30)
#define pi (2*acos(0.0))
#define all(a) a.begin(),a.end()
#define mem(a,v) memset(a,v,sizeof(a))
#define rep(i,b,e) for((i)=b;(i)<(e);(i)++)
#define rev(i,b,e) for((i)=e-1;(i)>=(b);(i)--)
#define fi(b,e) for((i)=b;(i)<(e);(i)++)
#define fj(b,e) for((j)=b;(j)<(e);(j)++)
#define fk(b,e) for (k)=b;(k)<(e);(k)++)
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
#define S 1005
int prime[PS/32+1];
void setbit(int i){int p=i>>5,q=i&31;prime[p]|=(1<<q);}
bool checkbit(int i){int p=i>>5,q=i&31;return prime[p]&(1<<q)?true:false;}
void buildprime(int n){int i,j,k=sqrt(double(n));prime[0]=3;for(i=4;i<n;i+=2)setbit(i);for(i=3;i<=k;i+=2){if(!checkbit(i)){int ii=i+i;for(j=i*i;j<n;j+=ii)setbit(j);}}}


int sum,r,n,N,R,C,t,txt;
int val[25];
map<int,int>mp;
vi V[2000005];
int main(){
	freopen("1.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k;
	scanf("%d",&t);
	while(t--){
	    scanf("%d",&n);
	    fi(0,2000005)V[i].clear();
	    fi(0,n)scanf("%d",&val[i]);
	    int tot = 0;
	    printf("Case #%d:\n",++txt);
	    for(i = 1; i < (1 << n); ++i){
	        int sum = 0;
	        fj(0,n)if(1 & (i >> j)){
	            sum += val[j];
	        }
	        V[sum].push_back(i);
        }
        /*bool flag = false;
        fj(0,n)if(1 &(ii >> j)){
            if(flag)printf(" ");
            printf("%d",val[j]);
            flag = true;
        }
        printf("\n");*/
        fi(1,2000005)if(V[i].size() > 1){
            int cur = 0;
            fj(0,V[i].size()){
                for(k = j + 1; k < V[i].size(); ++k)if(!(V[i][j] & V[i][k])){
                //fk(j+1,V[i].size())if(!(V[i][j] & V[i][k])){
                    tot++;
                    cur++;
                    bool flag = false;
                    for(int jj = 0; jj < n; ++jj)if(1 & (V[i][j] >> jj)){
                        if(flag)printf(" ");
                        printf("%d",val[jj]);
                        flag = true;
                    }
                    printf("\n");
                    flag = false;
                    for(int jj = 0; jj < n; ++jj)if(1 & (V[i][k] >> jj)){
                        if(flag)printf(" ");
                        printf("%d",val[jj]);
                        flag = true;
                    }
                    printf("\n");
                    break;
                }
                if(tot)break;
            }
            if(tot)break;
        }
	    if(!tot)printf("Impossible\n");
    }
	return 0;
}
