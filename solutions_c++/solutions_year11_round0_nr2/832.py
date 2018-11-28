#include <cstdio>
int TC,C,D,n,x,ok;
char s[1005],com[100][5],opp[100][5],t[1005],F;
int main(){
	scanf("%d",&TC);
	for (int T=1;T<=TC;T++){
		
		scanf("%d",&C);
		for (int i=1;i<=C;i++) scanf("%s",com[i]);
		scanf("%d",&D);
		for (int i=1;i<=D;i++) scanf("%s",opp[i]);
		scanf("%d",&n);
		scanf("%s",s);
		
		x=0;
		
		for (int i=0;i<n;i++){
			
			t[x++]=s[i];
			
			F=0;

			for (int j=1;j<=C;j++){
				if (x<=1) break;
				if ((t[x-1]==com[j][0] && t[x-2]==com[j][1])
					|| (t[x-2]==com[j][0] && t[x-1]==com[j][1])){
						F=1;
						t[x-2]=com[j][2];
						x--;
				}	
			}

		
			if (!F){
				for (int j=1;j<=D;j++)
					for (int k=0;k<x-1;k++)
					if ((t[x-1]==opp[j][0] && t[k]==opp[j][1])
						|| (t[x-1]==opp[j][1] && t[k]==opp[j][0]))
							x=0;
			}
				
		}
		
		t[x]=0;
		printf("Case #%d: [",T);
		if (x==0) printf("]\n");
		else 
			for (int i=0;i<x;i++)
				printf("%c%s",t[i],i==x-1?"]\n":", ");
	}
	scanf("\n");
	return 0;
}
