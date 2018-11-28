#pragma warning(disable: 4786)
#include<stdio.h>
#include<string>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<set>
#include<math.h>
#include<queue>
#include<queue>
using namespace std;
		


deque < int > d;
queue<int> v;



void ini()
{
	while(!d.empty())d.pop_back();
	while(!v.empty())v.pop();
}
int main()	
{			
	int  T,cs,R,K,N,ans,i,a,k,t;
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0.out","w",stdout);
	
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{

		ini();
		ans=0;
		scanf("%d %d %d",&R,&K,&N);
		for(i=0;i<N;i++)
		{
			scanf("%d",&a);
			d.push_back(a);
		}
		


		for(i=0;i<R;i++)
		{
			k=0;
			while(!d.empty())
			{
				t=d.front();d.pop_front();
				if((k+t)<=K)
				{
					k+=t;
					v.push(t);
				}
				else
				{
					d.push_front(t);
					break;
				}
			}
			while(!v.empty())
			{
				t=v.front();v.pop();
				d.push_back(t);
			}
			ans+=k;
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	
  	return 0;
}			