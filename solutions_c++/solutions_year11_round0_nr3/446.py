#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int minv,sum;

long long tot;

int n;
int main(){
	int T;
	cin>>T;
	for(int tc = 1;tc<=T;tc++){
		minv = 1000001;
		tot = sum = 0;
		int x;
		cin>>n;
		for(int i=0;i<n;i++){
			scanf("%d",&x);
			tot += x;
			sum ^= x;
			minv = min(minv,x);
		}
		printf("Case #%d: ",tc);
		if(sum) puts("NO");
		else printf("%lld\n",tot - minv);
	}
	return 0;
}
