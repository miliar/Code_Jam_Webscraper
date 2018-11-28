#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cmath>


using namespace std;
#define ps system("PAUSE")


int t,n;
long long int k,p2n;

inline long long int pow2(int n) {
	long long int p = 1;
	while(n--) {
		p*=(long long int) 2;
	}
	return p;
}


int main() {
	freopen("C:/TestData/A-large.in","r",stdin);freopen("C:/TestData/A.out","w",stdout);
	long long int temp;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++) {
		scanf("%lld%lld",&n,&k);
		p2n = pow2(n);
		temp = k%p2n;
		if( temp == p2n -1 ) 
			printf("Case #%d: %s\n",ti,"ON");
		else 
			printf("Case #%d: %s\n",ti,"OFF");
	}
	
}

