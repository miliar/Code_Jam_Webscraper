#include <stdio.h>

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ntc;
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		int n,l,h,note[200];
		scanf("%d %d %d\n",&n,&l,&h);
		for (int i=0;i<n;i++) scanf("%d",&note[i]);
		printf("Case #%d: ",tc);
		bool solution=false;
		for (int i=l;i<=h;i++){
			bool possible=true;
			for (int j=0;j<n;j++)
				if ((note[j]%i!=0)&&(i%note[j]!=0)){
					possible=false;
					break;
				}
			if (possible){
				printf("%d\n",i);
				solution=true;
				break;
			}
		}
		if (!solution) printf("NO\n");
	}
	fclose(stdin);
	fclose(stdout);
}