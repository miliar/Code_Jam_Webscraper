#include<stdio.h>
char s[5][5];
main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,i,j;
	int flg,end;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		flg=true;
		end=false;
		for(i=0;i<4;i++){
			scanf("%s",s[i]);
			for(j=0;j<4;j++){
				if(s[i][j]=='.') flg=false;
			}
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(s[i][j]!='O'&&s[i][j]!='T') break;
			}
			if(j==4){
				printf("Case #%d: O won\n",t);
				end=true;
				break;
			}
		}
		if(end) continue;
		for(j=0;j<4;j++){
			for(i=0;i<4;i++){
				if(s[i][j]!='O'&&s[i][j]!='T') break;
			}
			if(i==4){
				printf("Case #%d: O won\n",t);
				end=true;
				break;
			}
		}
		if(end) continue;
		for(i=0;i<4;i++){
			if(s[i][i]!='O'&&s[i][i]!='T') break;
		}
		if(i==4){
			printf("Case #%d: O won\n",t);
			continue;
		}
		for(i=0;i<4;i++){
			if(s[i][3-i]!='O'&&s[i][3-i]!='T') break;
		}
		if(i==4){
			printf("Case #%d: O won\n",t);
			continue;
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(s[i][j]!='X'&&s[i][j]!='T') break;
			}
			if(j==4){
				printf("Case #%d: X won\n",t);
				end=true;
				break;
			}
		}
		if(end) continue;
		for(j=0;j<4;j++){
			for(i=0;i<4;i++){
				if(s[i][j]!='X'&&s[i][j]!='T') break;
			}
			if(i==4){
				printf("Case #%d: X won\n",t);
				end=true;
				break;
			}
		}
		if(end) continue;
		for(i=0;i<4;i++){
			if(s[i][i]!='X'&&s[i][i]!='T') break;
		}
		if(i==4){
			printf("Case #%d: X won\n",t);
			continue;
		}
		for(i=0;i<4;i++){
			if(s[i][3-i]!='X'&&s[i][3-i]!='T') break;
		}
		if(i==4){
			printf("Case #%d: X won\n",t);
			continue;
		}
		if(flg) printf("Case #%d: Draw\n",t);
		else printf("Case #%d: Game has not completed\n",t);
	}
}
