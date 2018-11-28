#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
char map[5][5];
int main()
{
	int nocm,i,j,co=0,t;
	int x[5][2],o[5][2];
	scanf("%d",&t);getchar();
	while(t--)
	{
		memset(x,0,sizeof(x));memset(o,0,sizeof(o));
		nocm=0;co++;
		
		for(i=0;i<4;i++)
			gets(map[i]);
		getchar();
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			{
			//	cout<<map[i][j];
				if(map[i][j]=='.') nocm++;//cout<<nocm<<endl;
				if(i==j && (map[i][j]=='X'||map[i][j]=='T')) 
					x[4][0]++;
				if(i==j && (map[i][j]=='O'||map[i][j]=='T')) 
					o[4][0]++;
				if(i+j==3 && (map[i][j]=='O'||map[i][j]=='T'))
					o[4][1]++;
				if(i+j==3 && (map[i][j]=='X'||map[i][j]=='T'))
					x[4][1]++;	
				if(map[i][j]=='X'||map[i][j]=='T') {
					x[i][0]++;x[j][1]++;}
				if(map[i][j]=='O'||map[i][j]=='T') {
					o[i][0]++;o[j][1]++;}
			

			}..puts("");
		}
		printf("Case #%d: ",co);
		int flag=0;
		for(i=0;i<5;i++){
			if(x[i][0]==4||x[i][1]==4) {flag=1;break;}
			if(o[i][0]==4||o[i][1]==4) {flag=2;break;}}
		if(flag==0){
			if(nocm==0) printf("Draw\n");
			else printf("Game has not completed\n");
		}else if(flag==1) printf("X won\n");
		else printf("O won\n");
	}

	return 0;
}
