#include <cstdio>
#include <cstring>

const int cx[]={-1,0,0,1};
const int cy[]={0,-1,1,0};
int h,w,g[100][100],x,y,xx,yy,t,tmp,qx[10010],qy[10010],front,rear;
char c[100][100],b[100][100],cur;

int main()
{
	int T,N;
	scanf("%d",&N);
	for(T=1;T<=N;T++)
	{
		scanf("%d%d",&h,&w);
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				scanf("%d",&g[i][j]);
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
			{
				t=-1;
				tmp=g[i][j];
				for(int k=0;k<4;k++)
				{
					x=i+cx[k],y=j+cy[k];
					if(x>=0 && x<h && y>=0 && y<w && g[x][y]<tmp)
						tmp=g[x][y],t=k;
				}
				b[i][j]=t;
			}
		memset(c,0,sizeof(c));
		cur='a';
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				if(!c[i][j])
				{
					x=i,y=j;
					while(b[x][y]!=-1)
						t=b[x][y],x+=cx[t],y+=cy[t];
					front=0,rear=1,qx[0]=x,qy[0]=y;
					while(front<rear)
					{
						x=qx[front],y=qy[front++];
						c[x][y]=cur;
						for(int k=0;k<4;k++)
						{
							xx=x+cx[k],yy=y+cy[k];
							if(xx>=0 && xx<h && yy>=0 && yy<w && xx+cx[b[xx][yy]]==x && yy+cy[b[xx][yy]]==y)
								qx[rear]=xx,qy[rear++]=yy;
						}
					}
					cur++;
				}
		printf("Case #%d:\n",T);
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
			{
				putchar(c[i][j]);
				putchar(j<w-1?' ':'\n');
			}
	}
	return 0;
}
