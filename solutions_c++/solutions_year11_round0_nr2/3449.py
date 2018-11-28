#include <stdio.h>
#include <string.h>
#include <stdlib.h>
char cc[37][4],dd[29][3],s[105];
int move(int top,int i){
	int j;
	for(j=i;j>top;j--)
		s[j]=s[j-1];
	return top+1;
}
int main(void){
	//freopen("2.in","r",stdin);
	//freopen("2.out","w",stdout);
	int ncase,C,D,N,i,j,k,top,w;
	scanf("%d",&ncase);
	for(w=1;w<=ncase;w++){
		//input
		scanf("%d",&C);
		for(i=0;i<C;i++)
			scanf("%s",cc[i]);
		scanf("%d",&D);
		for(i=0;i<D;i++)
			scanf("%s",dd[i]);
		scanf("%d%s",&N,s);
		//deal
		for(i=top=0;i<N;i++){
			//delete
			for(j=0;j<D;j++)
				for(k=top;k<i;k++)
					if((s[k]==dd[j][0]&&s[i]==dd[j][1])||(s[k]==dd[j][1]&&s[i]==dd[j][0])){
						top=i+1;
						s[i]=' ';
						break;
					}
			if(top>=N)
				break;
			//add
			for(j=0;j<C;j++)
				if(i+1<N)
					if((s[i]==cc[j][0]&&s[i+1]==cc[j][1])||(s[i]==cc[j][1]&&s[i+1]==cc[j][0])){
						s[i+1]=cc[j][2];
						top=move(top,i);
						break;
					}
		}
		//output
		printf("Case #%d: [",w);
		if(top<N)
			printf("%c",s[top]);
		for(i=top+1;i<N;i++)
			printf(", %c",s[i]);
		puts("]");
	}
	return 0;
}