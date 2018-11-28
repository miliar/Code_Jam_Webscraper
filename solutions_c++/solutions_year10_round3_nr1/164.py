#include <stdio.h>
#include <string.h>

#define MAX 1024

int wires[MAX][2];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%d%d",&wires[i][0],&wires[i][1]);
		int res=0;
		for(int i=0;i<n;++i)
			for(int j=i+1;j<n;++j)
				res+=(wires[i][0]>wires[j][0] && wires[i][1]<wires[j][1]) ||
						 (wires[i][0]<wires[j][0] && wires[i][1]>wires[j][1]);
		printf("Case #%d: %d\n",test,res);
	}
	return 0;
}
