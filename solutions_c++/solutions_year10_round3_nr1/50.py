#include <cstdio>
using namespace std;

int a[1000], b[1000];

int jeden(){
	int n; scanf("%d", &n);
	for(int i = 0; i<n; i++)
		scanf("%d%d", a+i, b+i);
	int total = 0;
	for(int i = 0; i<n; i++){
		for(int j = 0; j<i; j++)
			if((a[i]<a[j])!=(b[i]<b[j]))
				total++;
	}
	return total;
}

main(){
	int c; scanf("%d", &c);
	for(int i = 1; i<=c; i++) printf("Case #%d: %d\n", i, jeden());
}
