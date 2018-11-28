#include<stdio.h>
char p[5][6];
bool ck1(int x,int y){
	return p[x][y]!='O'&&p[x][y]!='T';
}
bool ck2(int x,int y){
	return p[x][y]!='X'&&p[x][y]!='T';
}
int main()
{
	int T=0,i,TC,j;
	bool c1,c2,ck;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&TC);
	while(T<TC){
		printf("Case #%d: ",++T);
		for(i=0;i<4;i++){
			scanf("%s",p[i]);
		}
		c1=c2=true;
		for(i=0;i<4;i++){
			if(ck1(i,3-i))c1=false;
			if(ck2(i,3-i))c2=false;
		}
		if(c1){printf("O won\n");continue;}
		if(c2){printf("X won\n");continue;}
		c1=c2=true;
		for(i=0;i<4;i++){
			if(ck1(i,i))c1=false;
			if(ck2(i,i))c2=false;
		}
		if(c1){printf("O won\n");continue;}
		if(c2){printf("X won\n");continue;}
		ck=false;
		for(i=0;i<4;i++){
			c1=c2=true;
			for(j=0;j<4;j++){
				if(ck1(i,j))c1=false;
				if(ck2(i,j))c2=false;
				if(ck1(i,j) && ck2(i,j))ck=true;
			}
			if(c1){printf("O won\n");break;}
			if(c2){printf("X won\n");break;}
			c1=c2=true;
			for(j=0;j<4;j++){
				if(ck1(j,i))c1=false;
				if(ck2(j,i))c2=false;
			}
			if(c1){printf("O won\n");break;}
			if(c2){printf("X won\n");break;}
		}
		if(i==4){
			if(ck)printf("Game has not completed\n");
			else printf("Draw\n");
		}
	}
}