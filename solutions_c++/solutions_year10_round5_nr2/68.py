#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>

using namespace std;

long long d[101000];
long long l,n;
long long b[200];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);

	for (int tt=1; tt<=t; tt++){
		printf("Case #%d: ",tt);

		scanf("%I64d%I64d",&l,&n);
		for (int i=1; i<=n; i++)
			scanf("%I64d",&b[i]);

		memset(d,0,sizeof(d));

		d[0]=1;
		for (int i=1; i<=15000; i++){
			d[i]=1000000000LL;
			for (int j=1; j<=n; j++){
				if (i-b[j]>=0){
					if (d[i-b[j]]!=1000000000LL)
						d[i]=min(d[i],d[i-b[j]]+1);
				}
			}
		}

		long long res=1000000000000000001LL;
		for (long long i=1; i<=15000; i++)
			if (d[i]!=1000000000LL){
				long long x=d[i]-1;
				for (long long j=1; j<=n; j++)
					if ((l-i)%b[j]==0){
						long long tres=x+(l-i)/b[j];
						if (tres<res) res=tres;
					}
			}

		if (res==1000000000000000001LL) printf("IMPOSSIBLE\n"); else
			cout<<res<<endl;
	}

	return 0;
}