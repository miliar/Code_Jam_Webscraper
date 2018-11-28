#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <string>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef unsigned long long uint64;
typedef long long int64;
#define eps 1e-9
#define pi 3.1415926535897932384626433832795
#define MAX 55

int R,C;
vector<string> Map;
vector<int> cnt[MAX]; 
int row[MAX],column[MAX];
bool visit[MAX][MAX];


bool isok(int r,int c)
{
	if((r+1>=R) || (c+1)>=C)return false;
	if(visit[r][c] || visit[r][c+1] || visit[r+1][c] || visit[r+1][c+1])
		return false;
	return true;
}
bool in(int r,int c)
{
	if((r+1>=R) || (c+1)>=C)return false;
	else
		return true;

}
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("A-large.in","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,testcase=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: \n",testcase++);
		scanf("%d%d",&R,&C);
		string str;
		memset(visit,0,sizeof(visit));
		Map.clear();
		for(int i=1;i<=R;i++)
		{
			cin>>str;
			Map.push_back(str);
// 			cnt[i].clear();
// // 			for(int j=0;j<str.size();j++)
// // 				if(str[j]=='#')
// // 				{
// // 					cnt[i].push_back(j+1);
// // 					row[i]++;
// // 				}
		}
		bool flag=true;
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				if(in(i,j) && visit[i][j]==0 &&
					Map[i][j]=='#'&& Map[i][j+1]=='#' && 
					Map[i+1][j]=='#' && Map[i+1][j+1]=='#')
				{
					
						Map[i][j]='/';Map[i][j+1]='\\';Map[i+1][j]='\\';Map[i+1][j+1]='/';
						visit[i][j]=1,visit[i][j+1]=1,visit[i+1][j]=1,visit[i+1][j+1]=1;
				
					
				}
			}
		}
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
				if(Map[i][j]=='#')
				{
					flag=false;break;
				}
			if(!flag)break;
		}
		if(!flag)
			cout<<"Impossible"<<endl;
		else
		{
			for(int i=0;i<R;i++)
				cout<<Map[i]<<endl;
		}

	}
	return 0;
}