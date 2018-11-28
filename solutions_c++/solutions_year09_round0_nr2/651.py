#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int h,w;

int a[128][128];
char mymap[128][128];

struct In
{
	int x;
	int y;
	int hh;
	bool operator < (const In t) const
	{
		if(hh!=t.hh) return hh<t.hh;
		if(x!=t.x) return x<t.x;
		return y<t.y;
	}
};

int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};

char tmp;
vector<In> my;

void fun(int x,int y,char c1,char c2)
{
	mymap[x][y]=c1;
	int tx,ty;
	for (int i=0;i<4;i++)
	{
		tx=x+dx[i];
		ty=y+dy[i];
		if(tx<0 || tx>=h || ty<0 || ty>=w) continue;
		if(mymap[tx][ty]==c2) fun(tx,ty,c1,c2);
	}
}

void process(int nCase)
{
	scanf("%d %d",&h,&w);
	my.clear();
	for (int i=0;i<h;i++)
	{
		for (int j=0;j<w;j++)
		{
			scanf("%d",&a[i][j]);
			In tt;
			tt.x=i;
			tt.y=j;
			tt.hh=a[i][j];
			my.push_back(tt);
		}
	}
	sort(my.begin(),my.end());
	memset(mymap,0,sizeof(mymap));
	int tx,ty;
	tmp='A';
	for (int i=0;i<h;i++)
	{
		for(int j=0;j<w;j++)
		{
			int sum=0;
			for (int k=0;k<4;k++)
			{
				tx=i+dx[k];
				ty=j+dy[k];
				if(tx<0 || tx>=h || ty<0 || ty>=w) continue;
				if(a[tx][ty]<a[i][j]) sum++;
			}
			if (sum==0)
			{
				mymap[i][j]=tmp;
				tmp++;
			}
		}
	}
	for(int i=0;i<my.size();i++)
	{
		int min=my[i].hh;
		if(mymap[my[i].x][my[i].y]!=0) continue;
		for (int k=0;k<4;k++)
		{
			tx=my[i].x+dx[k];
			ty=my[i].y+dy[k];
			if(tx<0 || tx>=h || ty<0 || ty>=w) continue;
			if(a[tx][ty]<min) min=a[tx][ty];
		}
		for (int k=0;k<4;k++)
		{
			tx=my[i].x+dx[k];
			ty=my[i].y+dy[k];
			if(tx<0 || tx>=h || ty<0 || ty>=w) continue;
			if(a[tx][ty]==min)
			{
				mymap[my[i].x][my[i].y]=mymap[tx][ty];
				break;
			}
		}
	}
	tmp='a';
	for(int i=0;i<h;i++)
	{
		for(int j=0;j<w;j++){
			if(mymap[i][j]>='A' && mymap[i][j]<='Z')
			{
				fun(i,j,tmp,mymap[i][j]);
				tmp++;
			}
		}
	}
	printf("Case #%d:\n",nCase);
	for (int i=0;i<h;i++)
	{
		for (int j=0;j<w;j++)
		{
			printf("%c ",mymap[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&n);
	for (int i=1;i<=n;i++)
	{
		process(i);
	}
	return 0;
}