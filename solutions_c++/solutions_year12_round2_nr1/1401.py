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
int val[300];
int done[300];
double A[300];
int main(){
	freopen("1.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k;
	scanf("%d",&t);
	while(t--){
	    scanf("%d",&n);
	    fi(0,n)scanf("%d",&val[i]);
	    mem(done,0);
	    mem(A,0.);
	    int sum = 0;
	    fi(0,n)sum += val[i];
	    int tot = sum + sum;
        printf("Case #%d:",++txt);
        double one = double(tot) / double(n);
        N = n;
        fi(0,n){
            if(double(val[i]) >= one){
                done[i] = 1;
                tot -= val[i];
                N--;
                A[i] = 0.;
            }
        }
        if(tot)one = double(tot) / double(N);
        else{
            fi(0,n)if(done[i] == 0){
                done[i] = 1;
                A[i] = 100. / double(N);
            }
        }
        fi(0,n){
            if(done[i] == 0){
                double baki = one - double(val[i]);
                double ans = baki / double(sum);
                A[i] = ans * 100.;
            }
            printf(" %lf",A[i]);
        }
        printf("\n");
	}
	return 0;
}
