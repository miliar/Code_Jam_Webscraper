#include<cstdio>
#include<cstring>
int t,d,n,c,b[105],opp[105][105],com[105][105],tl;
char s[10000],ss[10000];
int main(){
	scanf("%d",&t);
	for (int z=1; z<=t; z++){
		for (int i=1; i<=100; i++)
			for (int j=1; j<=100; j++)
				com[i][j]=opp[i][j]=0;
		scanf("%d",&c);
		for (int i=1; i<=c; i++){
			scanf("%s",s);
			com[s[0]][s[1]]=com[s[1]][s[0]]=s[2];
		}
		scanf("%d",&d);
		for (int i=1; i<=d; i++){
			scanf("%s",s);
			opp[s[0]][s[1]]=opp[s[1]][s[0]]=1;	
		}
		scanf("%d",&n);
		scanf("%s",s);
		tl=-1;
		for (int i=0; i<n ; i++){
			ss[++tl]=s[i];
			if (!i) continue;
			if (com[ss[tl]][ss[tl-1]]){
				ss[tl-1]=com[ss[tl]][ss[tl-1]];
				--tl;
				continue;
			}
			for (int k=0; k<tl; k++){
				if (opp[ss[k]][ss[tl]]) tl=-1;
			}
		}
		printf("Case #%d: [",z);
		for (int i=0; i<tl; i++) printf("%c, ",ss[i]);
		if (tl>-1)
			printf("%c",ss[tl]);
		printf("]\n");
	}
	return 0;	
}
