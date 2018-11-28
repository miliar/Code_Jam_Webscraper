#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

#define VI vector<int>
#define VS vector<string>
#define SZ(x) ((int)(x).size())
#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define MS(a,b) memset((a),b,sizeof(a))
#define EC(tp,it,a) for(tp::iterator it=(a).begin();it!=(a).end();++it)
#define SE(x) cout<<#x<<" = "<<x<<endl
#define PB push_back

template<class T> void inc(T& a, const T& b) {
	if (a < b) a = b;
}
template<class T> void dec(T& a, const T& b) {
	if (a > b) a = b;
}

const int INF=~0u>>1;
const int N=100+3;

int D,I;
int n,m;
int a[N];
int f[N][256];

int run(){
	if(n==1)return 0;
	MS(f,0);
	FR(k,0,256)f[0][k]=abs(k-a[0]);
	FR(i,1,n){
		FR(k,0,256){
			f[i][k]=D*i+abs(k-a[i]);
			
			int low=max(0,k-m);
			int high=min(255,k+m);
			FR(j,0,i){
				FR(t,0,256){
					if(t>=low && t<=high){
						dec(f[i][k],
							f[j][t]
							+ (i-1-j)*D
							+ abs(k-a[i])
						);
					}
					else if(m>0){
						dec(f[i][k],
							f[j][t]
							+ ((abs(k-t)-1)/m)*I
							+ (i-1-j)*D
							+ abs(k-a[i])
						);
					}
				}
			}
//			if(k<4)printf("%d,%d : %d\n",i,k,f[i][k]);
		}
	}
	int ans=INF;
	FR(i,0,n){
		FR(k,0,256){
			dec(ans,f[i][k]+D*(n-1-i));
		}
	}
//	FR(i,0,n){
//		FR(k,0,10)printf("%d ",f[i][k]);
//		putchar(10);
//	}
	return ans;
}

int main() {
	freopen("b1.in","r",stdin);
	freopen("b1.out","w",stdout);
	
	int ts;
	scanf("%d",&ts);
	FR(cas,0,ts){
		scanf("%d%d%d%d",&D,&I,&m,&n);
		FR(i,0,n)scanf("%d",a+i);
		printf("Case #%d: %d\n",cas+1,run());
	}
	return 0;
}
