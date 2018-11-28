#include <iostream>
#include <fstream>
using namespace std;
ofstream fout ("jam2.out");
ifstream fin ("B-large.in");
int mat[110][110];
char st[110][110],nst[110][110];
bool vis[110][110];
struct nod
{
	int hi;
	int x,y;
}high[11000],que[11000];
int cmp( const void *a ,const void *b) 
{ 
	return (*(nod *)a).hi > (*(nod *)b).hi ? 1 : -1; 
} 
int main()
{
	int T,i,j,dimx,dimy,k,cc,temp,xx,yy,nx,ny,nhigh,tx,ty,top,px,py;
	char ncr,cr;
	fin>>T;
	for(i=0;i<T;++i)
	{
		fin>>dimx>>dimy;
		tx=dimx+1;
		ty=dimy+1;
		for(j=0;j<=tx;++j)
			for(k=0;k<=ty;++k)
				mat[j][k]=11000;
		cc=0;
		for(j=1;j<=dimx;++j)
		{
			for(k=1;k<=dimy;++k)
			{
				fin>>mat[j][k];
				high[cc].hi=mat[j][k];
				high[cc].x=j,high[cc].y=k;
				cc++;
			}
		} 		
		temp=dimx*dimy;
		qsort(high,temp,sizeof(high[0]),cmp);
		cr='A';
		memset(st,0,sizeof(st));
		for(j=0;j<temp;++j)
		{
			xx=high[j].x;
			yy=high[j].y;
			nx=xx;
			ny=yy;
			nhigh=high[j].hi;
			if(mat[xx-1][yy]<nhigh)
			{
				nhigh=mat[xx-1][yy];
				nx=xx-1,ny=yy;
			}
			if(mat[xx][yy-1]<nhigh)
			{
				nhigh=mat[xx][yy-1];
				nx=xx,ny=yy-1;
			}
			
			if(mat[xx][yy+1]<nhigh)
			{
				nhigh=mat[xx][yy+1];
				nx=xx,ny=yy+1;
			}
			if(mat[xx+1][yy]<nhigh)
			{
				nhigh=mat[xx+1][yy];
				nx=xx+1,ny=yy;
			}
			if((nx==xx)&&(ny==yy))
			{
				st[xx][yy]=cr++;
			}
			else
			{
				st[xx][yy]=st[nx][ny];
			}
		}
		memset(vis,0,sizeof(vis));
		ncr='a';
		for(j=1;j<=dimx;++j)
		{
			for(k=1;k<=dimy;++k)
			{
				if(vis[j][k]==0)
				{
					
					vis[j][k]=1;
					nst[j][k]=ncr;
					top=0;
					que[top].x=j,que[top].y=k;
					top++;
					while(top)
					{
						--top;
						px=que[top].x,py=que[top].y;
						if((!vis[px+1][py])&&(st[px+1][py]==st[px][py]))
						{
							nst[px+1][py]=ncr;
							vis[px+1][py]=1;
							que[top].x=px+1,que[top].y=py;
							top++;
						}
						if((!vis[px][py+1])&&(st[px][py+1]==st[px][py]))
						{
							nst[px][py+1]=ncr;
							vis[px][py+1]=1;
							que[top].x=px,que[top].y=py+1;
							top++;
						}
						if((!vis[px-1][py])&&(st[px-1][py]==st[px][py]))
						{
							nst[px-1][py]=ncr;
							vis[px-1][py]=1;
							que[top].x=px-1,que[top].y=py;
							top++;
						}
						if((!vis[px][py-1])&&(st[px][py-1]==st[px][py]))
						{
							nst[px][py-1]=ncr;
							vis[px][py-1]=1;
							que[top].x=px,que[top].y=py-1;
							top++;
						}
					}
					ncr++;
				}	
			}
		}
		fout<<"Case #"<<i+1<<": "<<endl;
		for(j=1;j<=dimx;++j)
		{
			for(k=1;k<=dimy;++k)
			{ 
				fout<<nst[j][k]<<' ';
			}
			fout<<endl;
		}
	}
	return 0;
}