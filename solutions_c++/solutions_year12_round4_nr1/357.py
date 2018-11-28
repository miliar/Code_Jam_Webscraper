#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

long long d[10100];
long long l[10100];
long long b[10100];

int main(){
	int tc, tcn, n;
	long long D;
	scanf("%d", &tcn);
	for(tc=0; tc<tcn; ++tc){
		scanf("%d", &n);
		for(int i=0; i<n; ++i){
			scanf("%lld %lld", &d[i], &l[i]);
		}
		scanf("%lld", &D);
		l[n] = D*D;
		d[n] = D;
		memset(b, -1, sizeof(b));
		
		b[0] = d[0];
		for(int i=0; i<n; ++i){
			for(int j=i+1; j<=n; ++j){
				if(d[j] - d[i] <= b[i]){
					b[j] = max(b[j], min(l[j], d[j] - d[i]));
				}
			}
		}
		printf("Case #%d: %s\n", tc+1, b[n] == -1 ? "NO" : "YES");
	}
}
