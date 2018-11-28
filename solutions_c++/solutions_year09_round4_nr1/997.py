#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>

//#define dprintf(...) printf(__VA_ARGS__)
#define dprintf(...)

using namespace std;

typedef vector<int> matrix;

int main(void) {
	int cases,n,i,j,k,l,temp,counter;
	bool changed,ok;
	matrix tmp;
	scanf("%d\n",&cases);
	dprintf("%d cases to proceed\n",cases);
	for(i=1;i<=cases;i++) {
		scanf("%d\n",&n);
		tmp.clear();
		dprintf("Case %d has n=%d\n",n);
		for(j=0;j<n;j++) {
			tmp.push_back(0);
			for(k=1;k<=n;k++) {
				if(getchar()!='0') {
					tmp[j]=k;
				}
			}
			getchar();
		}
		for(j=0;j<n;j++)
			dprintf("Case %d, line %d: %d\n",i,j,tmp[j]);
		changed=true;
		counter=0;
		for(j=1;j<=n;j++) {
			for(k=j-1;(k<n)&&(tmp[k]>j);k++);
			if(k>=j) {
				for(l=k;(l>=j);l--) {
					temp=tmp[l-1];
					tmp[l-1]=tmp[l];
					tmp[l]=temp;
					counter++;
				}
			}
		}
		printf("Case #%d: %d\n",i,counter);
	}
	return 0;
}
