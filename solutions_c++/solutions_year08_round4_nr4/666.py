#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

#define mset(a,x) memset(a,x,sizeof(a))
typedef long long i64;
const int INF=INT_MAX/2;
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
template <class T>void dbgarr(const T* a,int n){for(int i=0;i<n;i++)cerr<<a[i]<<" ";cerr<<endl;}
#define dbg(x) cerr<<#x<<" : "x<<endl

int S,K;

char buf[50005];

int per[16];

void init(){
}
int main()
{
	int T,kcase(0);
	scanf("%d",&T);
	while(T--){
		init();
		scanf("%d",&K);
		getchar();
		gets(buf);
		S=strlen(buf);
		for(int i=0;i<K;i++){
			per[i]=i;
		}
		int res=INF;
		do{
			int sum=0;
			char prev=0;
			for(int i=0;i<S;i+=K){
				for(int j=0;j<K;j++){
					if(buf[i+per[j]]!=prev){
						prev=buf[i+per[j]];
						sum++;
					}
				}
			}
			res<?=sum;
		}while(next_permutation(per,per+K));
		printf("Case #%d: %d\n",++kcase,res);
	}
}
