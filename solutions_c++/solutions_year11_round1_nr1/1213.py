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

bool flag;
long long n,p1,p2;
long long gcd (long long a , long long b){
	if( b==0) return a;
	gcd(b,a%b);
}
int main(void){
	int t;
	scanf("%d",&t);
	for(int te=0;te<t;te++){
		printf("Case #%d: ",te+1);

		scanf("%lld %lld %lld",&n,&p1,&p2);
		if( p2 == 100  && p1 != 100){
			if( p1 == 100)
				printf("Possible\n");
			else
				printf("Broken\n");
			continue;
		}
		if(p1==0){
			printf("Possible\n");
			continue;
		}
		else if( p2==0 ){
			printf("Broken\n");
			continue;
		}
		flag=false;
		long long nn = gcd(p1,100);
		long long par = 100/nn, child = p1/nn;
		if( par <= n ){
			flag = true;
		}
		if( flag)
			printf("Possible\n");
		else
			printf("Broken\n");
	}
	return 0;
}