#include <iostream>
#include <sstream>
#include <math.h>


int main(int argc, char **argv) {
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	//freopen("input.ropeintranet","r",stdin);
	//freopen("out.ropeintranet","w",stdout);
	int t; //Number of test cases
	int n; //Number of wires
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d",&n);
		int left[n];
		int right[n];
		for(int j=0;j<n;j++){
			scanf("%d %d",&left[j],&right[j]);
		}
		/*for(int j=0;j<n;j++){
			printf("%d %d\n",left[j],right[j]);
		}*/
		int intCount=0;
		for(int j=1;j<n;j++){
			int lH=left[j];
			int rH=right[j];
			int k=0;
				for(;k<j;k++){
					if(left[k]<lH && right[k]>rH){
						intCount++;
					}else if(left[k]>lH && right[k]<rH){
						intCount++;
					}
				}
		}
		printf("Case #%d: %d\n",i,intCount);
	}
}

