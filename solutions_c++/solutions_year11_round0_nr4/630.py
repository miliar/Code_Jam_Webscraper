#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

void run(int casen) {
	int a[1001];
	int n=0;
	int cost=0;
	int temp=0;
	float costf=0;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d",&a[i]);
	}
	
	for(int i=1;i<=n;i++){
		if(a[i]!=i){
			cost++;
		}
	}
	costf=cost;
	printf("Case #%d: %.6f\n",casen,costf);
}

int main(int argc, char* argv[]) {
	int ncases=0;
	freopen(argv[1], "rt", stdin);
	freopen("A.out", "wt", stdout);
	scanf("%d",&ncases); 
	for(int i=1;i<=ncases;i++) 
	run(i);
	
	return 0;
}
