#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int CaseNo,k=0;
	freopen("A-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	scanf("%d",&CaseNo);
	while(k++<CaseNo){
		int n,i;
		char oper[120];
		int pos[120];
		int opos=1,bpos=1;
		int ofin=0,bfin=0;
		scanf("%d",&n);
		oper[0]='A';
		for(i=1;i<=n;i++)
			scanf(" %c%d",&oper[i],&pos[i]);
		for(i=1;i<=n;i++){
			if(oper[i]=='O'){
				ofin=ofin + ((pos[i]>opos)?(pos[i]-opos):(opos-pos[i]));				
				opos=pos[i];
				if(!(i==1||oper[i-1]=='O'))
					ofin= (ofin>bfin)?ofin:bfin;
				ofin++;
			}
			if(oper[i]=='B'){
				bfin=bfin+ ((pos[i]>bpos)?(pos[i]-bpos):(bpos-pos[i]));				
				bpos=pos[i];
				if(!(i==1||oper[i-1]=='B'))
					bfin= (bfin>ofin)?bfin:ofin;
				bfin++;
			}
		}
		printf("Case #%d: %d\n",k,(bfin>ofin)?bfin:ofin);
	}
	return 0;
}

