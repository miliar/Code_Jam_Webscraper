#include <cstdio>
#include <cstring>
#include <cstdlib>

const int dx[]	=	{0,1,1,1};
const int dy[]	=	{1,1,0,-1};
char s[10][10];

inline bool range(int x,int y)
{
	return x>=0 && y>=0 && x<4 && y<4;
}

int main()
{
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test){
		for (int i=0;i<4;++i){
			scanf("%s",s[i]);
		}
		bool wino=false,winx=false;
		bool empty=false;
		for (int i=0;i<4;++i){
			for (int j=0;j<4;++j){
				empty|=s[i][j]=='.';
				if (s[i][j]=='O' || s[i][j]=='X'){
					for (int k=0;k<4;++k){
						int x=i,y=j,cnt=-1,c=0;
						while (range(x,y) && (s[x][y]==s[i][j] || s[x][y]=='T')){
							c+=s[x][y]=='T';
							++cnt;
							x+=dx[k];
							y+=dy[k];
						}
						x=i,y=j;
						while (range(x,y) && (s[x][y]==s[i][j] || s[x][y]=='T')){
							c+=s[x][y]=='T';
							++cnt;
							x-=dx[k];
							y-=dy[k];
						}
						if (cnt==4 && c<=1){
							if (s[i][j]=='O') wino=true;
							else winx=true;
						}
					}
				}
			}
		}
		printf("Case #%d: ",test);
		if (wino && winx) {
			puts("Draw");
		}else if (wino) {
			puts("O won");
		}else if (winx) {
			puts("X won");
		}else{
			if (empty){
				puts("Game has not completed");
			}else{
				puts("Draw");
			}
		}
	}
	return 0;
}
