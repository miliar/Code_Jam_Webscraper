#include<cstdio>
int h[105][105];
int dr[105][105];
int walk[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int mark[105][105];
int qx[105*105],qy[105*105];
int to[1000];
int main()
{
	int T,cc,H,W,i,j,k,x,y,ch,nx,ny;
	freopen("B-large.in","r",stdin);
	freopen("Blar.out","w",stdout);
	scanf("%d",&T);
	for(cc=1;cc<=T;++cc)
	{
		scanf("%d%d",&H,&W);
		for(i=0;i<H;++i)
			for(j=0;j<W;++j)scanf("%d",&h[i][j]);
		for(i=0;i<H;++i)
			for(j=0;j<W;++j)
			{
				dr[i][j]=-1;ch=h[i][j];
				mark[i][j]=-1;
				for(k=0;k<4;++k)
				{
					x=i+walk[k][0];
					y=j+walk[k][1];
					if(x<0||y<0||x>=H||y>=W)continue;
					if(h[x][y]<ch)
					{
						dr[i][j]=k;
						ch=h[x][y];
					}
				}
			}
		int ct=0,front,rear;
		for(i=0;i<H;++i)
			for(j=0;j<W;++j)
			{
				if(dr[i][j]==-1)
				{
					front=rear=0;
					qx[rear]=i;qy[rear++]=j;mark[i][j]=ct;
					while(front<rear)
					{
						x=qx[front];y=qy[front++];
						for(k=0;k<4;++k)
						{
							nx=x+walk[k][0];
							ny=y+walk[k][1];
							if(nx<0||ny<0||nx>=H||ny>=W)continue;
							if(mark[nx][ny]==-1&&dr[nx][ny]+k==3)
							{
								qx[rear]=nx;qy[rear++]=ny;
								mark[nx][ny]=ct;
							}
						}
					}
					ct++;
				}
			}
		printf("Case #%d:\n",cc);
		for(i=0;i<26;++i)to[i]=-1;
		ct=0;
		for(i=0;i<H;++i)
			{
				for(j=0;j<W;++j)
				{
					if(j>0)printf(" ");
					if(to[mark[i][j]]==-1)to[mark[i][j]]=ct++;
					printf("%c",to[mark[i][j]]+'a');
				}
				printf("\n");
			}
	}
	return 0;
}
