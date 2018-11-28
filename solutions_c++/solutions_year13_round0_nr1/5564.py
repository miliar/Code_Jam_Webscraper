#include <cstdio>
using namespace std;
char M[4][4];
int main(){
	int t,cas,i,j,x,y,acum;
	char win;
	bool end,com;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		for(i=0;i<4;i++)
			scanf("%s",M[i]);
		win='d';
		end=false;
		com=true;
		for(i=0;i<4 && !end;i++){
			for(j=0;j<4 && !end;j++){
				if(M[i][j]!='.'){
					acum=1,x=j-1;
					while(x>=0 && M[i][x--]==M[i][j]) acum++;
					if(x+1>=0 && M[i][x+1]=='T') acum++;
					x=j+1;
					while(x<4 && M[i][x++]==M[i][j]) acum++;
					if(x-1<4 && M[i][x-1]=='T') acum++;
					//printf("-> %d %c\n",acum,M[i][j]);
					if(acum==4){ win=M[i][j]; end=true; }
					
					acum=1,x=i-1;
					while(x>=0 && M[x--][j]==M[i][j]) acum++;
					if(x+1>=0 && M[x+1][j]=='T') acum++;
					x=i+1;
					while(x<4 && M[x++][j]==M[i][j]) acum++;
					if(x-1<4 && M[x-1][j]=='T') acum++;
					//printf("--> %d %c\n",acum,M[i][j]);
					if(acum==4){ win=M[i][j]; end=true; }
					
					acum=1,x=j-1,y=i-1;
					while(x>=0 && y>=0 && M[y--][x--]==M[i][j]) acum++;
					if(x+1>=0 && y+1>=0 && M[y+1][x+1]=='T') acum++;
					y=i+1,x=j+1;
					while(x<4 && y<4 && M[y++][x++]==M[i][j]) acum++;
					if(x-1<4 && y-1<4 && M[y-1][x-1]=='T') acum++;
					//printf("---> %d %c\n",acum,M[i][j]);
					if(acum==4){ win=M[i][j]; end=true; }
					
					acum=1,x=j+1,y=i-1;
					while(x<4 && y>=0 && M[y--][x++]==M[i][j]) acum++;
					if(x-1<4 && y+1>=0 && M[y+1][x-1]=='T') acum++;
					y=i+1,x=j-1;
					while(x>=0 && y<4 && M[y++][x--]==M[i][j]) acum++;
					if(x+1>=0 && y-1<4 && M[y-1][x+1]=='T') acum++;
					//printf("---> %d %c\n",acum,M[i][j]);
					if(acum==4){ win=M[i][j]; end=true; }
				}
				else if(M[i][j]=='.') com=false;
			}
		}
		if(win=='X') printf("Case #%d: X won\n",cas);
		else if(win=='O') printf("Case #%d: O won\n",cas);
		else if(!com) printf("Case #%d: Game has not completed\n",cas);
		else if(win=='d') printf("Case #%d: Draw\n",cas);
	}
	return 0;
}
