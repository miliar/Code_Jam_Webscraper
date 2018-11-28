#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int pat[20][600];
char dic[5000][20];

int main()
{
	int c, i, k;
	int L, D, N, l;
	char p;
	int ans, ok;
	c=1;
	scanf("%d%d%d\n",&L,&D,&N);
	
	
	for(i=0;i<D;i++) { scanf("%s\n",dic[i]); }
	
	for(i=0;i<N;i++){
		memset(pat,0,sizeof(pat));
		k=0;
		while(1){
			p=getc(stdin);
			if(p=='('){
				while(1){
					p=getc(stdin);
					if(p==')'){ k++; break; }
					else if(isalpha(p)){ pat[k][p]=1;}
				}
			}else if(isalpha(p)){
				pat[k][p]=1; k++;
			}else if(p=='\n') break;
		}
		ans=0;
		for(k=0;k<D;k++){
			ok=1;
			for(l=0;l<L;l++)
				if(!pat[l][dic[k][l]]){ok=0; break;}
			if(ok) ans++;
		}
		
		printf("Case #%d: %d\n",c, ans);
		c++;
	}
	return 0;
}
