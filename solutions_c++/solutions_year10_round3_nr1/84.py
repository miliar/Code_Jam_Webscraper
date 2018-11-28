#include <iostream>
#include <cstdio>
#include <queue>
#include <list>
#include <cstring>
#include <cmath>
#include <cstring>

using namespace std;

long a[1111],b[1111];

int main(){

	long cc,tt;
	long i,j,n;
	scanf("%d",&tt);
	long ans;
	for(cc=0;cc<tt;cc++){
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d%d",&a[i],&b[i]);
		ans=0;
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
				if((a[i]>a[j]&&b[i]<b[j])||(a[i]<a[j]&&b[i]>b[j]))
					ans++;
		printf("Case #%d: %d\n",cc+1,ans);
	}
	return 0;
}
 