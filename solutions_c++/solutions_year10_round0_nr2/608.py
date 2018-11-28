#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
#define MAX 1001
long long num[MAX];

bool cmp(long long a, long long b) {
	if (a < b)
		return true;
	return false;
}

long long gcd(long long a, long long b) {
	if (b  == 0)
		return a;
	return gcd(b,a%b);
}
int main() {
	int N,i,M,j,k;
	vector <long long> restos;
	scanf("%d",&N);
	long long ans;
	for (i = 1 ; i <= N ; i++) {
		scanf("%d",&M);
		for (j = 0 ; j < M ; j++)
			scanf("%lld",&num[j]);	
		sort(num,num+M,cmp);
		restos.resize(0);
		ans = 0;	
		for (j = M-1 ; j > 0 ; j--) 
			for (k = j-1 ; k >= 0 ; k--) {
				restos.push_back(num[j]-num[k]);
				//printf("Add = %d\n",num[j]-num[k]);		
			}
		ans = restos[0];
		//printf("Restos[0] = %lld\n",restos[0]);
		for (j = 1 ; j < restos.size() ; j++) {
//printf("Gcd de %lld e %lld\n",ans,restos[j]);			
			ans = gcd(ans,restos[j]);
			
		}
		//printf("ans = %lld\n",ans);
		printf("Case #%d: %lld\n",i,(ans-(num[0]%ans))%ans);	
	
	}
	return 0;
}
