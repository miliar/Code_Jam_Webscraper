#include<iostream>
using namespace std;
int h,w;
int hei[110][110];
int dy[4]={0,-1,1,0};
int dx[4]={-1,0,0,1};
bool used[110][110];
int group[110][110];
struct Point
{
	int x,y;
	Point (int a=0,int b=0)
	{
		x=a;
		y=b;
	}
	bool operator ==(const Point &b)const
	{
		if (x==b.x&&y==b.y) return true;
		else return false;
	}
}father[110][110];
const Point zero(0,0);
Point findfa(Point a)
{
	if (father[a.x][a.y]==a)
		return a;
	else
		father[a.x][a.y]=findfa(father[a.x][a.y]);
	return father[a.x][a.y];
}
void unite(Point a,Point b)
{
	father[b.x][b.y]=a;
}
int main()
{
	int t;
	cin>>t;
//	freopen("outsmall.txt","w",stdout);
	for (int i=1;i<=t;i++)
	{
		memset(hei,0,sizeof(hei));
		memset(used,0,sizeof(used));
		memset(group,0,sizeof(group));
		memset(father,0,sizeof(father));
		cin>>h>>w;
		for (int j=1;j<=h;j++)
			for (int k=1;k<=w;k++)
			{
				cin>>hei[j][k];
				father[j][k].x=j;
				father[j][k].y=k;
			}
			for (int j=1;j<=h;j++)
				for (int k=1;k<=w;k++)
				{
					if (used[j][k]==0)
					{
						bool flag=1;
						int nowx,nowy;
						nowx=j;
						nowy=k;
						while(flag)
						{
							flag=0;
							if (used[nowx][nowy]) break;
							used[nowx][nowy]=1;
							int mini=hei[nowx][nowy];
							int minx,miny;
							for (int l=0;l<4;l++)
							{
								int tx=nowx+dx[l];
								int ty=nowy+dy[l];
								if (tx>h||tx<1||ty<1||ty>w)
									continue;
								if (hei[tx][ty]<mini)
								{
									mini=hei[tx][ty];
									minx=tx;
									miny=ty;
								}
							}
							if (mini!=hei[j][k])
							{
								flag=1;
								Point now,to;
								now.x=nowx;
								now.y=nowy;
								to.x=minx;
								to.y=miny;
								Point f1=findfa(now);
								Point f2=findfa(to);
								if (f1==f2)
									;
								else
								{
									unite(f1,f2);
									nowx=minx;
									nowy=miny;
								}
							}
						}
					}
				}
				int ind=1;
				for (int j=1;j<=h;j++)
					for (int k=1;k<=w;k++)
					{
						Point tmp;
						tmp.x=j;
						tmp.y=k;
						Point f=findfa(tmp);
						if (group[f.x][f.y]==0)
						{
							group[f.x][f.y]=ind++;
							group[j][k]=group[f.x][f.y];
						}
						else
							group[j][k]=group[f.x][f.y];
					}
					cout<<"Case #"<<i<<":"<<endl;
					for (int j=1;j<=h;j++)
					{
						for (int k=1;k<=w;k++)
						{
							cout<<(char)('a'+group[j][k]-1);
							if (k==w)
								;
							else
								cout<<' ';
						}
						cout<<endl;
					}
	}
	return 0;
}





