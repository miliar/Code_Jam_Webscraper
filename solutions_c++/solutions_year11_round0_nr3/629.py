#include <stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

void run(int casen) {
	int n=0;
	int total=0;
	int bi=0;
	int min=1000000;
	int x=0;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&x);
		bi=bi^x;
		total=total+x;
		if(x<min){
			min=x;
		}
	}
	if(bi==0)
	printf("Case #%d: %d\n",casen,total-min);
	else
	printf("Case #%d: NO\n",casen);
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
