#include<stdio.h>
char str[4][5];
int main(){
	int a;
	scanf("%d",&a);
	int t=0;
	while(a--){
		t++;
		for(int i=0;i<4;i++)scanf("%s",str[i]);
		bool x=false;
		bool o=false;
		bool dot=false;
		for(int i=0;i<4;i++){
			int X=0;
			int O=0;
			int T=0;
			for(int j=0;j<4;j++){
				if(str[i][j]=='X')X++;
				if(str[i][j]=='O')O++;
				if(str[i][j]=='T')T++;
				if(str[i][j]=='.')dot=true;
			}
			if(X==4||(X==3&&T==1))x=true;
			if(O==4||(O==3&&T==1))o=true;
		}
		for(int i=0;i<4;i++){
			int X=0;
			int O=0;
			int T=0;
			for(int j=0;j<4;j++){
				if(str[j][i]=='X')X++;
				if(str[j][i]=='O')O++;
				if(str[j][i]=='T')T++;
				if(str[j][i]=='.')dot=true;
			}
			if(X==4||(X==3&&T==1))x=true;
			if(O==4||(O==3&&T==1))o=true;
		}
		int X=0;
		int O=0;
		int T=0;
		for(int j=0;j<4;j++){
			if(str[j][j]=='X')X++;
			if(str[j][j]=='O')O++;
			if(str[j][j]=='T')T++;
			if(str[j][j]=='.')dot=true;
		}
		if(X==4||(X==3&&T==1))x=true;
		if(O==4||(O==3&&T==1))o=true;
		X=0;
		O=0;
		T=0;
		for(int j=0;j<4;j++){
			if(str[j][3-j]=='X')X++;
			if(str[j][3-j]=='O')O++;
			if(str[j][3-j]=='T')T++;
			if(str[j][3-j]=='.')dot=true;
		}
		if(X==4||(X==3&&T==1))x=true;
		if(O==4||(O==3&&T==1))o=true;
		printf("Case #%d: ",t);
		if(x)printf("X won\n");
		else if(o)printf("O won\n");
		else if(dot)printf("Game has not completed\n");
		else printf("Draw\n");
	}
}