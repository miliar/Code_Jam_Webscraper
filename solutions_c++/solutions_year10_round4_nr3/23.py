// zero.lin`s google_codejam.cpp 
//

/*
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>
#include <cctype>
#include <cmath>
*/

#include "google_codejam\stdafx.h"
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef long long ll;

#define rep(i,n) for(int i=0;i<n;++i)
#define all(n) n.begin(),n.end()
#define sz(o) (int)(o.size())
#define mset(o,v) memset(o,v,sizeof(o))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define mk(first,second) make_pair(first,second)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end())

const int inf=1<<28;
const double eps=1e-11;
int data[1003][4];
bool add[1003];
bool connect[1003][1003];
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	rep(caseID,testcase)
	{
		int R;
		scanf("%d",&R);
		rep(i,R)
		{
			rep(j,4)
			{
				scanf("%d",&data[i][j]);
			}
		}
		mset(add,0);
		mset(connect,0);
		rep(i,R)
		{
			for(int j=i+1;j<R;++j)
			{
				int x1=max(data[i][0],data[j][0]);
				int y1=max(data[i][1],data[j][1]);
				int x2=min(data[i][2],data[j][2]);
				int y2=min(data[i][3],data[j][3]);
				if(x2-x1>=-1 && y2-y1>=-1 && !((data[i][0]>data[j][2] && data[i][1]>data[j][3]) ||(data[j][0]>data[i][2] && data[j][1]>data[i][3])))
					connect[i][j]=connect[j][i]=true;
			}
		}
		int ans=0;
		rep(i,R)
		{
			if(add[i])
				continue;
			add[i]=true;
			queue<int> q;
			q.push(i);
			int left=inf;
			int x=0,y=0;
			while(!q.empty())
			{
				int now=q.front();
				left=min(left,abs(data[now][0]+data[now][1]));
				x=max(x,data[now][2]);
				y=max(y,data[now][3]);
				q.pop();
				rep(j,R)
					if(connect[now][j] && !add[j])
					{
						add[j]=true;
						q.push(j);
					}
			}
			ans=max(ans,abs(x+y)-left+1);
		}
		printf("Case #%d: %d\n",caseID+1,ans);		
	}
	
	return 0;
}

