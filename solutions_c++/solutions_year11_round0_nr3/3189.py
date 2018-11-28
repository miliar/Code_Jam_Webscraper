#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
typedef long long int64;
typedef long double ld;

const int inf=2000000000;
const ld eps=1e-07;

int n;
int a[2000];

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int t;
	scanf("%d",&t);
	for (int z=1;z<=t;++z){
		scanf("%d",&n);
		for (int i=0;i<n;++i)
			scanf("%d",&a[i]);
		int ans=-inf;

		for (int i=1;i<(1<<n);++i){
			int k1=0;
			int k2=0;
			int sum1=0;
			int sum2=0;
			int xor1=0;
			int xor2=0;
			for (int j=0;j<n;++j){
				if ( i & (1<<j) ){
					++k1;
					sum1+=a[j];
					xor1=xor1^a[j];
				}
				else {
					++k2;
					sum2+=a[j];
					xor2=xor2^a[j];
				}
			}
			if (xor1==xor2 && k1 && k2)
				ans=max(ans,sum1);
		}
		if (ans>=0)
			printf("Case #%d: %d\n",z,ans);
		else printf("Case #%d: NO\n",z);
	}
	return 0;
}