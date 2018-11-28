#include <stdio.h>
#include <queue>
#include <vector>
using namespace std;
int xp[9]={-1,1,0,0,-1,-1,1,1,0};
int yp[9]={0,0,-1,1,-1,1,-1,1,0};
int V[10000];
int Dis[10000];
int R,C;
char D[15][15];
int isGoal(int y,int x)
{
		return D[y][x]=='x' || D[y][x]=='w';
}
int isGoodMove(int y,int x,int dir,vector<int> &pos)
{
		for (int q=0;q<=1;++q)
		{
				int yy=y+yp[dir^q];
				int xx=x+xp[dir^q];
				if (yy<0 || yy>=R || xx<0 || xx>=C) return 0;
				if (D[yy][xx]=='#') return 0;
				for (int w=0;w<pos.size();++w) if (pos[w]==yy*15+xx) return 0;
		}
		return 1;
}
int encode(vector<int> &pos,int &is_stable)
{
		int y=pos[0]/15;
		int x=pos[0]%15;
		int move;
		is_stable = 0;
		if (pos.size()==1)
		{
				move=8;
				is_stable=1;
				return move + x*10 + y*150;
		}
		for (int q=0;q<8;++q) if (y+yp[q]==pos[1]/15 && x+xp[q]==pos[1]%15)
		{
				move=q;
				is_stable=(q<4)?1:0;
				break;
		}
		return move + x*10 + y*150;
}
int main()
{
		int T;
		scanf("%d",&T);
		for (int kase=1;kase<=T;++kase)
		{
				fprintf(stderr,"%d\n",kase);
				scanf("%d %d",&R,&C);
				for (int q=0;q<R;++q) scanf("%s",D[q]);
				vector<int> pos;
				for (int q=0;q<R;++q) for (int w=0;w<C;++w)
						if (D[q][w]=='w' || D[q][w]=='o')
								pos.push_back(q*15+w);
				int top;
				int reg = encode(pos,top);
				V[reg]=kase;
				Dis[reg]=0;
				queue<int> Q;
				Q.push(reg);
				int ret=-1;
				while (!Q.empty())
				{
						int dec = Q.front(); Q.pop();
						int backup = dec;
						int move = dec % 10; dec/=10;
						int x = dec % 15; dec/=15;
						int y = dec;
						//fprintf(stderr,".%d %d %d [%d]\n",y,x,move,Dis[backup]);
						//end Check
						if (isGoal(y,x) && isGoal(y+yp[move],x+xp[move])) { ret=Dis[backup]; break; }
						int was_stable = ( move < 4) || (move == 8 );
						vector<int>pos;
						pos.push_back(y*15+x);
						if (move<8)	pos.push_back((y+yp[move])*15+(x+xp[move]));
						for (int q=0;q<pos.size();++q)
						{
								int yy=pos[q]/15,xx=pos[q]%15;
								//move
								for (int w=0;w<4;++w)
								{
										if (isGoodMove(yy,xx,w,pos)) 
										{
												pos[q]=(yy+yp[w])*15 + (xx+xp[w]);
												int is_stable;
												int enc = encode(pos,is_stable);
												pos[q]=yy*15+xx;
												if (!was_stable && !is_stable) continue;
												if (V[enc]!=kase)
												{
														V[enc]=kase;
														Dis[enc]=Dis[backup]+1;
														Q.push(enc);
												}
										}
								}
						}
				}
				printf("Case #%d: %d\n",kase,ret);
		}
		return 0;
}
