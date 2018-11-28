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
long long n,l,h;

long long arr[100000];
long long gcdi,lcm;
int main(void){
	int t;
	scanf("%d",&t);
	for(int te=0;te<t;te++){
		scanf("%lld %lld %lld",&n,&l,&h);

		for(int i = 0 ;i < n;i++){
			scanf("%lld",&arr[i]);
		}
		gcdi = arr[0];
		for(int i = 0 ;i < n;i++){
			gcdi = gcd(gcdi,arr[i]);
		}
		lcm = 1; 
		for(int i = 0 ;i < n;i++){
			lcm*=arr[i];
			if( i == n/2)
				lcm/=gcdi;
		}
		bool flag = false;

		long long print=1;
		for(int k = l;k<=h;k++){
			int i;
			for(i = 0 ;i < n;i++){
				if( arr[i] % k != 0 && k%arr[i] != 0 )
					break;
			}
			if( i == n ){
				flag = true;
				print = k;
				break;
			}
		}
		printf("Case #%d: ",te+1);
		if(flag)
			printf("%lld\n",print);
		else
			printf("NO\n");

	}
	return 0;
}