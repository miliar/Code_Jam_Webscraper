#include <stdio.h>
#include <stdlib.h>

#define MX 1020

int T,N;
char inp[MX][MX];

int main()
{
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

	scanf("%d",&T);
	while(T) {

		int i,j;
		int flag=0, flag2=0, flag3=0, flag4=0, Flag=0, Full=0;

		for(i=0;i<4;i++) scanf("%s",&inp[i]);

		for(i=0;i<4;i++) {
			for(j=0;j<4;j++) {
				if(inp[i][j]=='.') {
					Full=1; break;
				}
			}
		}
		//sero
		for(i=0;i<4;i++) {
			flag=0, flag2=0, flag3=0, flag4=0;
			for(j=0;j<4;j++) {
				if(inp[i][j]!='X' && inp[i][j]!='T') flag=1;
				if(inp[i][j]!='O' && inp[i][j]!='T') flag2=1;
				if(inp[j][i]!='X' && inp[j][i]!='T') flag3=1;
				if(inp[j][i]!='O' && inp[j][i]!='T') flag4=1;
			}
			if(flag==0 || flag3==0) {
				Flag=1;
				printf("Case #%d: X won\n",N+1); break;
			}
			else if(flag2==0 || flag4==0) {
				Flag=1;
				printf("Case #%d: O won\n",N+1); break;
			}
		}
		flag=flag2=flag3=flag4=0;
		for(i=0;i<4;i++) {
			if(inp[i][i]!='X' && inp[i][j]!='T') flag=1;
			if(inp[3-i][i]!='X' && inp[3-i][i]!='T') flag2=1;
			if(inp[i][i]!='O' && inp[i][j]!='T') flag3=1;
			if(inp[3-i][i]!='O' && inp[3-i][i]!='T') flag4=1;
		}
		if(flag==0 || flag2==0) {
			Flag=1;
			printf("Case #%d: X won\n",N+1);			
		} else if(flag3==0 || flag4==0) {
			Flag=1;
			printf("Case #%d: O won\n",N+1);
		}

		if(Flag==0) {
			if(Full==0) printf("Case #%d: Draw\n",N+1);
			else printf("Case #%d: Game has not completed\n",N+1);
		}

		N++; T--;
	}
	
}