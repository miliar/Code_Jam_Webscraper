#include <stdio.h>
char chess[4][5];
const int OWIN=0;
const int XWIN=1;
const int DRAW=2;
const int NC=3;

int check_stat(int i, int j, int di,int dj)
{
	bool has_dot=false;
	int score=0;
	for(int step=0;step<4;++step){		
		if(chess[i][j]=='O' )
			score+=1;
		if(chess[i][j]=='X')
			score+=-1;
		if(chess[i][j]=='.'){
			score=0;
			has_dot=true;
			break;
		}
		if(chess[i][j]=='T'){
			score+=0;
		}
		i+=di;j+=dj;
	}	
	if(score>=3){
		return OWIN;
	}
	if(score<=-3){
		return XWIN;
	}
	if(has_dot){
		return NC;
	}
	return DRAW;
}
int check()
{
	bool not_draw=false;
	int ret=-1;
	for(int i=0;i<4;++i){
		ret=check_stat(i,0,0,1);
		if(ret<DRAW)
			return ret;
		if(ret==NC)
			not_draw=true;
			
		ret=check_stat(0,i,1,0);
		if(ret<DRAW)
			return ret;
		if(ret==NC)
			not_draw=true;
	}
	ret=check_stat(0,0,1,1);
		if(ret<DRAW)
			return ret;
		if(ret==NC)
			not_draw=true;
	ret=check_stat(3,0,-1,1);
		if(ret<DRAW)
			return ret;
		if(ret==NC)
			not_draw=true;
	if(not_draw)
		return NC;
	else
		return DRAW;
}
int main(int argc, char **argv)
{
	int tc=0;
	scanf("%d",&tc);
	for (int c = 1; c <= tc; ++c)
	{
		for(int i=0;i<4;i++){
			scanf("%s", chess[i]);
		}
		int ret=check();
		switch(ret){
			case OWIN:
				printf("Case #%d: O won\n",c);
				break;
			case XWIN:
				printf("Case #%d: X won\n",c);
				break;
			case DRAW:
				printf("Case #%d: Draw\n",c);
				break;
			case NC:
				printf("Case #%d: Game has not completed\n",c);
				break;
		}
	}
	return 0;
}
