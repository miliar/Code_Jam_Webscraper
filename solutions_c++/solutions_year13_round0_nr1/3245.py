#include<stdio.h>
#include<string.h>

char boa[4][5];
int bx[4][4],bo[4][4];
int win;

void check(){
	win=4;
	int i,j;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++){
			if(boa[i][j]=='X'||boa[i][j]=='T')bx[i][j]=1;
			else bx[i][j]=0;
			if(boa[i][j]=='O'||boa[i][j]=='T')bo[i][j]=1;
			else bo[i][j]=0;
		}	

	/*for(i=0;i<4;i++){
		for(j=0;j<4;j++)
			printf("%d ",bx[i][j]);
		printf("\n");
	}
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++)
			printf("%d ",bo[i][j]);
		printf("\n");
	}*/
	
	for(i=0;i<4;i++){
		int ans1=0,ans2=0;
		for(j=0;j<4;j++)
			ans1+=bx[i][j],ans2+=bx[j][i];
		if(ans1==4||ans2==4){
			win=1;
			return;
		}
	}
	if(bx[0][0]+bx[1][1]+bx[2][2]+bx[3][3]==4||bx[0][3]+bx[1][2]+bx[2][1]+bx[3][0]==4){
		win=1;
		return;
	}
	
	for(i=0;i<4;i++){
		int ans1=0,ans2=0;
		for(j=0;j<4;j++)
			ans1+=bo[i][j],ans2+=bo[j][i];
		if(ans1==4||ans2==4){
			win=2;
			return;
		}
	}
	if(bo[0][0]+bo[1][1]+bo[2][2]+bo[3][3]==4||bo[0][3]+bo[1][2]+bo[2][1]+bo[3][0]==4){
		win=2;
		return;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,ti=1;
	scanf("%d",&t);
	while(t--){
		int i,j;
		for(i=0;i<4;i++)
			scanf("%s",boa[i]);
		check();
		if(win==4){
			int f=0;
			for(i=0;i<4;i++){
				for(j=0;j<4;j++)
					if(boa[i][j]=='.'){
						f=1;
						break;
					}
				if(f)break;
			}
			if(!f)win=3;
		}
		printf("Case #%d: ",ti++);
		switch(win){
			case 1:printf("X won\n");break;
			case 2:printf("O won\n");break;
			case 3:printf("Draw\n");break;
			case 4:printf("Game has not completed\n");break;
			default:break;
		}
	}
	return 0;
}