#include <string>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <numeric>
#define powu(a) (a)*(a)

using namespace std;

long long gcd (long long a , long long b){
	if( b==0) return a;
	gcd(b,a%b);
}

long long arr[100000];
long long tarr[100000];
long long gcdi,lcm;
long long l,t,n,c;
int main(void){
	int T;
	scanf("%d",&T);
	for(int te=0;te<T;te++){
		scanf("%lld %lld %lld %lld",&l,&t,&n,&c);
		long long sum = 0;
		for(int i = 0 ;i < c;i++){
			scanf("%lld",&arr[i]);
		}
		long double dist= 0.5 * t;
		long double print = 0 ;
		for(int i = 0 ;i < n;i++){
			sum += arr[i%c];
			tarr[i] = arr[i%c];
		}
		printf("Case #%d: ",te+1);
		if( l == 0 ){
			long long dap = sum * 2;
			printf("%lld\n",dap);
		}
		else{
			if( dist+1e-9 < sum){
				int i;
				int j=0;
				long long ar[100000];
				for(i= 0 ;i < n;i++){
					if( dist+1e-9 >= tarr[i]){
						dist -= tarr[i];
					}
					else{
						tarr[i] -= dist;
						dist = 0;
						ar[j++] = tarr[i];
					}
				}
				sort(ar,ar+j);
				if( l == 1 || j == 1){
					long long dap = (sum-ar[j-1])*2+ ar[j-1];
					printf("%lld\n",dap);
				}
				else if ( j >= 2 ){
					long long dap = (sum-ar[j-1]-ar[j-2])*2 + ar[j-1]+ar[j-2];
					printf("%lld\n",dap);
				}
			}
			else{
				long long dap = sum*2;
				printf("%lld\n",dap);
			}
		}
	}
	return 0;
}