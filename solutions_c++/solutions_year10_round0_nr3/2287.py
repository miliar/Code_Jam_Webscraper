#include<stdio.h>
#include<string>
#include<vector>
#include<string.h>
#include<algorithm>
#include<map>
#include<stack>
#include<set>
#include<math.h>
#include<iostream>
#include<queue>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("outc.txt","w",stdout);
	int i,j,r,n,k,test,team=0,temp;
	scanf("%d",&test);
	while(test--)
	{
		team++;
		scanf("%d%d%d",&r,&k,&n);
		queue<int> myin;
		queue<int> myout;
		for(i=0;i<n;i++)
		{
			scanf("%d",&temp);
			myin.push(temp);
		}
		int count=0;
		for(i=0;i<r;i++)
		{
			int now=0;
			while(!myin.empty())
			{
				temp=myin.front();
				if(now+temp<=k)
				{
					now+=temp;
					myin.pop();
					myout.push(temp);
				}
				else
					break;
			}
			count+=now;
			while(!myout.empty())
			{
				temp=myout.front();
				myout.pop();
				myin.push(temp);
			}
		}
		printf("Case #%d: %d\n",team,count);
	}
	return 0;
}