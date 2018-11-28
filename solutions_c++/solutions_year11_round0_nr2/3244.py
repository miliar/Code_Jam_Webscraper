#include <stdio.h>

int T,c,d,n;
char tc[100][5],td[100][5],s[1000];
char buf[1000];
int k;

int main(){
	int i,j,l,f;
	scanf("%d",&T);
	for(int lT=1;lT<=T;lT++){
		scanf("%d",&c);
		for(i=0;i<c;i++)
			scanf("%s",tc[i]);
		scanf("%d",&d);
		for(i=0;i<d;i++)
			scanf("%s",td[i]);
		scanf("%d%s",&n,s);
		k=0;
		for(i=0;i<n;i++){
			buf[k++]=s[i];
			f=1;
			while(k>=2&&f){
				f=0;
				for(j=0;j<c;j++){
					if(tc[j][0]==buf[k-1] && tc[j][1]==buf[k-2]
					|| tc[j][1]==buf[k-1] && tc[j][0]==buf[k-2]){
						k -= 2;
						buf[k++]=tc[j][2];
						f=1;
						break;
					}
				}
			}
			for(l=0;l<k-1;l++){
				for(j=0;j<d;j++){
					if(td[j][0]==buf[k-1] && td[j][1]==buf[l]
					|| td[j][1]==buf[k-1] && td[j][0]==buf[l]){
						k=0;
						break;
					}
				}
			}
		}
		printf("Case #%d: [",lT);
		for(i=0;i<k;i++){
			if(i)printf(", ");
			printf("%c",buf[i]);
		}
		printf("]\n");
	}
	return 0;
}
