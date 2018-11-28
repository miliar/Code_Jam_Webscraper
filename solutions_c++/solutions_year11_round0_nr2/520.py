#include<stdio.h>
#include<stdlib.h>
char c[5],s[200],ans[200],com[50][50],o[50][50];
int k;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B2.out","w",stdout);
	int T,C,D,N,i,j,t;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		for(i=0;i<50;i++){
			for(j=0;j<50;j++){
				com[i][j]=0;
				o[i][j]=0;
			}
		}
		scanf("%d",&C);
		for(i=0;i<C;i++){
			scanf("%s",c);
			com[c[0]-'A'][c[1]-'A']=c[2];
			com[c[1]-'A'][c[0]-'A']=c[2];
		}
		scanf("%d",&D);
		for(i=0;i<D;i++){
			scanf("%s",c);
			o[c[0]-'A'][c[1]-'A']=1;
			o[c[1]-'A'][c[0]-'A']=1;
		}
		scanf("%d%s",&N,s);
		k=0;
		for(i=0;i<N;i++){
			ans[k]=s[i];
			if(k>0&&com[ans[k]-'A'][ans[k-1]-'A']!=0){
				k--;
				ans[k]=com[ans[k]-'A'][ans[k+1]-'A'];
			}
			for(j=0;j<k;j++){
				if(o[ans[j]-'A'][ans[k]-'A'])break;
			}
			if(j!=k)k=0;
			else k++;
		}
		printf("Case #%d: [",t);
		if(k!=0)printf("%c",ans[0]);
		for(i=1;i<k;i++){
			printf(", %c",ans[i]);
		}
		puts("]");
	}
} 
