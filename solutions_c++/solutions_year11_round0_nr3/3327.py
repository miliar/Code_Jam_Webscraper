#include <stdio.h>

using namespace std;

int main(){
	FILE *fp= fopen("c:\\treci2.out", "w+");

	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int n;
		scanf("%d",&n);
		int sum=0, xxor=0,min=10000000;
		for(int j=0;j<n;j++){
			int pom;
			scanf("%d",&pom);
			sum+=pom;
			xxor = xxor ^ pom;
			if(min>pom)
				min=pom;
		}
		
		if(xxor!=0){
			fprintf(fp,"Case #%d: NO\n",(i+1));
			printf("Case #%d: NO\n",(i+1));
		}else{
			fprintf(fp,"Case #%d: %d\n",(i+1),(sum-min));
			printf("Case #%d: %d\n",(i+1),(sum-min));
		}
	}	
}