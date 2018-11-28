#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<limits.h>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<complex>
#define EPS (1e-10)
#define PI (3.141592653589793238)
#define MP make_pair
typedef long long ll;
using namespace std;

#define MAX 1000000

vector<int> prime;
char sosuu[MAX+10000];

void prime_make(int n){
	int i,j;
	for(i=0;i<=n;i++)sosuu[i]=1;
	sosuu[0]=sosuu[1]=0;
	for(i=2;i*i<=n;i++){
		if(sosuu[i]==0)continue;
		for(j=i;i*j<=n;j++)sosuu[i*j]=0;
	}
	for(i=2;i<=n;i++)if(sosuu[i]==1)prime.push_back(i);
	return;
}

int main(void){
	int T;
	scanf("%d",&T);
	prime_make(MAX+100);
	for(int casenum=1;casenum<=T;casenum++){
		int i,j,k;
		ll n;
		scanf("%lld",&n);
		ll ans=1;
		for(i=2;i<=min((ll)MAX+10,n);i++){
			if(sosuu[i]==0)continue;
			ll a=0,now=i;
			while(now<=n){
				a++;
				now*=i;
			}
			ans+=max((ll)0,a-1);
		}
		if(n==1)ans=0;
		printf("Case #%d: %lld\n",casenum,ans);
	}
	return 0;
}
