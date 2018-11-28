#include<iostream>
#include<string>

using namespace std;
const int maxsize=101;
bool map[2][maxsize][maxsize];
int r,x1,y1,x2,y2;
int minx,miny,maxx,maxy;
int result;
int remain;
int cnt;
void run()
{
	cnt=0;
	while(remain)
	{
		remain=0;
		int cur=cnt%2;
		memcpy(map[1-cur],map[cur],sizeof(map[cur]));
		for (int j=minx-1;j<=maxx+1;j++)
			for (int k=miny-1;k<=maxy+1;k++)
			{

				if (map[cur][j][k]&&(map[cur][j-1][k]==0)&&(map[cur][j][k-1]==0))
					map[1-cur][j][k]=0;
				if ((map[cur][j][k]==0)&&(map[cur][j-1][k]==1)&&(map[cur][j][k-1]==1))
					map[1-cur][j][k]=1;
				if (map[1-cur][j][k])
					remain++;
			}
		cnt++;
	}
}
int main()
{
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		result=0;
		remain=1;
		minx=miny=INT_MAX;
		maxx=maxy=-1;
		memset(map,0,sizeof(map));
		scanf("%d",&r);
		for (int k=0;k<r;k++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if (x1<minx) minx=x1;
			if (x2>maxx) maxx=x2;
			if (y1<miny) miny=y1;
			if (y2>maxy) maxy=y2;
			for (int j=x1;j<=x2;j++)
			{
				for (int l=y1;l<=y2;l++)
					map[0][j][l]=map[1][j][l]=1;
			}
		}

		run();
		printf("Case #%d: %d\n",i,cnt);
	}
	return 0;
}