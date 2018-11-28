#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int N = 5;
char s[N][N];
int row[N][3];
int col[N][3];
int main(){
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		bool isend=1;
		for(int i=0;i<4;i++)scanf("%s",s[i]);
		bool flagx=0,flago=0;
		memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(s[i][j]=='X')row[i][0]++,col[j][0]++;
				else if(s[i][j]=='O')row[i][1]++,col[j][1]++;
				else if(s[i][j]=='T')row[i][2]++,col[j][2]++;
				else if(s[i][j]=='.')isend=0;
		for(int i=0;i<4;i++){
			if(row[i][0]==4||(row[i][0]==3&&row[i][2]==1))flagx=1;
			if(col[i][0]==4||(col[i][0]==3&&col[i][2]==1))flagx=1;
			if(row[i][1]==4||row[i][1]==3&&row[i][2]==1)flago=1;
			if(col[i][1]==4||(col[i][1]==3&&col[i][2]==1))flago=1;
		}
		int x=0,t=0,o=0;
		for(int i=0;i<4;i++)
			if(s[i][i]=='X')x++;
			else if(s[i][i]=='T')t++;
			else if(s[i][i]=='O')o++;
		if(x==4||x==3&&t==1)flagx=1;
		if(o==4||o==3&&t==1)flago=1;
		x=0,t=0,o=0;
		for(int i=0;i<4;i++)
			if(s[i][3-i]=='X')x++;
			else if(s[i][3-i]=='T')t++;
			else if(s[i][3-i]=='O')o++;
		if(x==4||(x==3&&t==1))flagx=1;
		if(o==4||(o==3&&t==1))flago=1;
		printf("Case #%d: ",cas);
		if(flagx)puts("X won");
		else if(flago)puts("O won");
		else if(!flagx&&!flago){
			if(isend)puts("Draw");
			else puts("Game has not completed");
		}
	}
	return 0;
}
