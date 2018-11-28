#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>

using namespace std;

//BEIGINTEMPLATE
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(
typedef long long int64;//NOTES:int64
const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps
template <class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template <class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
typedef pair<int,int> ipair;//NOTES:ipair
//ENDTMPLATE

const int inf=1000000;
const int maxn=105;
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};

struct Tqueue{int x,y;};

int alt[maxn][maxn];
char label[maxn][maxn];
int H,W;
Tqueue queue[maxn*maxn];

void init()
{
	int i,j;
	scanf("%d%d",&H,&W);
	for(i=1;i<=H;i++)
		for(j=1;j<=W;j++)scanf("%d",&alt[i][j]);
	memset(label,0,sizeof(label));
}

bool flow(int x1,int y1,int x2,int y2)//(x1,y2)->(x2,y2)?
{
	//if(x1<1 || x1>H || y1<1 || y1>W || x2<1 || x2>H || y2<1 || y2>W)return false;
	int i,j,newx,newy,minalt=inf,minalti;
	for(i=0;i<4;i++)
	{
		newx=x1+dx[i];
		newy=y1+dy[i];
		if(newx<1 || newx >H || newy<1 || newy>W)continue;
		if(alt[x1][y1]<=alt[newx][newy])continue;
		if(alt[newx][newy]<minalt)
		{
			minalt=alt[newx][newy];
			minalti=i;
		}
	}
	if(minalt==inf)return false;
	newx=x1+dx[minalti];
	newy=y1+dy[minalti];
	if(x2==newx && y2==newy)return true;else return false;
}

void bfs()
{
	int i,head=0,top=1;
	Tqueue now;
	int newx,newy;
	while(head<top)
	{
		head++;
		now=queue[head];
		for(i=0;i<4;i++)
		{
			newx=now.x+dx[i];
			newy=now.y+dy[i];
			if(newx<1 || newx >H || newy<1 || newy>W || label[newx][newy]!=0)continue;
			if(flow(now.x,now.y,newx,newy) || flow(newx,newy,now.x,now.y))
			{
				label[newx][newy]=label[now.x][now.y];
				queue[++top].x=newx;
				queue[top].y=newy;
			}
		}
	}
}

void showlabel()
{
	int i,j;
	for(i=1;i<=H;i++){for(j=1;j<=W;j++)printf("%c ",label[i][j]);puts("");}
}

void solve()
{
	int i,j;
	char nowlabel='a';
	bool flag;
	while(1)
	{
		flag=false;
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
				if(label[i][j]==0)
				{
					flag=true;
					label[i][j]=nowlabel++;
					memset(queue,0,sizeof(queue));
					queue[1].x=i;
					queue[1].y=j;
					bfs();
				}
		if(!flag)break;
	}
	showlabel();
}

int main()
{
	int i,testcase;
	//freopen("B-test.in","r",stdin);
	//freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-test.out","w",stdout);
	//freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&testcase);
	for(i=1;i<=testcase;i++)
	{
		init();
		printf("Case #%d:\n",i);
		solve();
	}
	fclose(stdout);
//	freopen("CON","r",stdin);
//	system("PAUSE");
	return 0;
}