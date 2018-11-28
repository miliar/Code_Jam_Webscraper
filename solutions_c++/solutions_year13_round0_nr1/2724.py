#include <cstdio>
int T,TC=1,x,o,t,cnt,re;
char s[4][5];
int main(void){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while(T--){
		for(int i=0; i<4; i++){
			scanf("%s",s[i]);
		}
		re=cnt=x=o=t=0;
		for(int i=0; i<4; i++){
			if(s[i][i]=='X')
				x++;
			else if(s[i][i]=='O')
				o++;
			else if(s[i][i]=='T')
				t++;
		}
		if((x==3 && t==1) || x==4)
			re=1;
		else if((o==3 && t==1) || o==4)
			re=2;
		x=o=t=0;
		for(int i=0; i<4; i++){
			if(s[i][3-i]=='X')
				x++;
			else if(s[i][3-i]=='O')
				o++;
			else if(s[i][3-i]=='T')
				t++;
		}
		if((x==3 && t==1) || x==4)
			re=1;
		else if((o==3 && t==1) || o==4)
			re=2;
		for(int i=0; i<4; i++){
			x=o=t=0;
			for(int j=0; j<4; j++){
				if(s[i][j]=='X')
					x++;
				else if(s[i][j]=='O')
					o++;
				else if(s[i][j]=='T')
					t++;
				else if(s[i][j]=='.')
					cnt--;
				cnt++;
			}
			if((x==3 && t==1) || x==4){
				re=1;
				break;
			}
			else if((o==3 && t==1) || o==4){
				re=2;
				break;
			}
		}
		if(!re){
			cnt=0;
			for(int i=0; i<4; i++){
				x=o=t=0;
				for(int j=0; j<4; j++){
					if(s[j][i]=='X')
						x++;
					else if(s[j][i]=='O')
						o++;
					else if(s[j][i]=='T')
						t++;
					else if(s[j][i]=='.')
						cnt--;
					cnt++;
				}
				if((x==3 && t==1) || x==4){
					re=1;
					break;
				}
				else if((o==3 && t==1) || o==4){
					re=2;
					break;
				}
			}

		}
		printf("Case #%d: ",TC);
		if(re==1)
			puts("X won");
		else if(re==2)
			puts("O won");
		else{
			if(cnt==16)
				puts("Draw");
			else puts("Game has not completed");
		}
		TC++;
	}

	return 0;
}