#include <stdio.h>
#include <string>
using namespace std;

typedef long long LL;

int dokad[1002];
LL ile[1002];
int grupy[1002];
int r,k,n;


int main() {
	int d;scanf("%d\n",&d);
	for(int s=1;s<=d;s++) {
		scanf("%d%d%d",&r,&k,&n);
		LL suma=0;
		for(int i=0;i<n;i++) {
			scanf("%d",&grupy[i]);
			suma+=grupy[i];
		}
		LL wyn=0;
		if(k>=suma) {
			wyn=(LL)r*suma;
		}
		else {
			for(int i=0;i<n;i++) {
				LL sumka=grupy[i];
				int i2=(i+1)%n;
				while(sumka+grupy[i2]<=k) {
					sumka+=grupy[i2];
					i2=(i2+1)%n;
				}
				dokad[i]=i2;
				ile[i]=sumka;
			}
			int tmp=0;
			for(int i=0;i<r;i++) {
				//printf("%d %d %d \n",ile[tmp],tmp,dokad[tmp]);
				wyn+=ile[tmp];
				tmp=dokad[tmp];
			}
		}
		printf("Case #%d: %I64d\n",s,wyn);
	}
	return 0;
}
