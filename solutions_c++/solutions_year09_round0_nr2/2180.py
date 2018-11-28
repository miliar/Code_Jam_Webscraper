#include <cstdio>
#include <utility>
#define MAX 105
#define INF int(1e9)
using namespace std;

int H,W;
int alt[MAX][MAX];
char ans[MAX][MAX];
char ch;

void init()
{
	int i,j;
	for(i=0;i<MAX;i++)
	{
		for(j=0;j<MAX;j++)
		{
			alt[i][j]=INF;
			ans[i][j]=0;
		}
	}
}

void get_input()
{
	int i,j;
	scanf("%d %d",&H,&W);
	for(i=1;i<=H;i++)
		for(j=1;j<=W;j++)
			scanf("%d",&alt[i][j]);
}

pair<int,int> get_coordinates(int i,int j)
{
	pair<int,int>ans;
	int x=-1,y=-1,min=alt[i][j];
	
	if(alt[i-1][j]<min) { min=alt[i-1][j];x=i-1;y=j;}
	if(alt[i][j-1]<min) { min=alt[i][j-1];x=i;y=j-1;}
	if(alt[i][j+1]<min) { min=alt[i][j+1];x=i;y=j+1;}
	if(alt[i+1][j]<min) { min=alt[i+1][j];x=i+1;y=j;}
	
	ans.first=x;
	ans.second=y;
//	printf("returing (%d %d) for (%d %d)\n",x,y,i,j);
	return ans;
}

char insert(int i,int j)
{	
	if(ans[i][j]!=0) return ans[i][j];
	pair<int,int>co=get_coordinates(i,j);
	int x=co.first;
	
	int y=co.second;
	
	if(x==-1 && y==-1)
	{
		ans[i][j]=ch;
		return ch++;
	}
	ans[i][j]=insert(x,y);
	return ans[i][j];
}	

void solve()
{
	int i,j;
	char te;
	ch='a';
	for(i=1;i<=H;i++)
		for(j=1;j<=W;j++)
			ans[i][j]=insert(i,j);
}

int main()
{
	int i,j,k,cases;

	scanf("%d",&cases);
	
	for(k=1;k<=cases;k++)
	{
		init();
		get_input();
		solve();
		printf("Case #%d:\n",k);
		for(i=1;i<=H;i++)
		{
			for(j=1;j<=W;j++) printf("%c ",ans[i][j]);
			printf("\n");
		}
	}		
return 0;
}	
	
