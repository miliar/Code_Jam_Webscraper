#pragma warning(disable:4996)
#pragma warning(disable:4010)//×¢ÊÍ
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <cmath>
#include <cstring>
#include <map>
#include <string>
#define PLMM return 0;
using namespace std;



const int sup=1010;
bool maze[sup][sup];
bool ma[sup][sup];
inline int Max(int a,int b)
{
	if(a>b)
		return a;
	return b;
}
int main()
{
	int T;
	int r;
	int x1,x2,y1,y2;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	int X,Y;
	int ans;
	for(int pz=1;pz<=T;++pz)
	{
		ans=0;
		X=-1;
		Y=-1;
		memset(maze,0,sizeof(maze));
		memset(ma,0,sizeof(maze));
		scanf("%d",&r);
		for(int i=0;i<r;++i)
		{
			scanf("%d %d %d %d",&y1,&x1,&y2,&x2);
			X=Max(x2,X);
			Y=Max(y2,Y);
			for(int ii=x1;ii<=x2;++ii)
				for(int jj=y1;jj<=y2;++jj)
					ma[ii][jj]=maze[ii][jj]=1;
		}
		bool out=false;
		while(1)
		{
			/*for(int i=0;i<=X+1;++i)
			{
				for(int j=0;j<=Y;++j)
					cout<<maze[i][j] <<" ";
				cout<<endl;
			}*/
			out=false;
			for(int i=1;i<=X+1;++i)
				for(int j=1;j<=Y+1;++j)
				{
					if(maze[i][j] && !maze[i-1][j] && !maze[i][j-1])
						ma[i][j]=0;
					else if(!maze[i][j] && (maze[i-1][j] && maze[i][j-1]))
						ma[i][j]=1;
					//ok|=maze[i][j];
				}
				++ans;
				for(int i=0;i<=X;++i)
				{
					for(int j=0;j<=Y;++j)
						if(maze[i][j])
						{
							out=true;
							break;
						}
					if(out)
						break;
				}

			if(!out)
				break;
				for(int i=0;i<=X;++i)
					for(int j=0;j<=Y;++j)
						maze[i][j]=ma[i][j];
		}
			printf("Case #%d: %d\n",pz,ans-1);
	}
	return 0;
}