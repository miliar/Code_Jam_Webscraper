#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>

using namespace std;

int find(int n,int sp)
{
	if(n<2)
		return n;
	if(n<=28)
	{
		int a=n/3,b=n%3;
		switch(b)
		{
			case 0:	if(sp)
						return a+1;
					return a;
		
			case 1:	if(a>0)
					return a+1;
		
			case 2:	if(sp)
						return a+2;
					return a+1;
		}
	}
	return 10;
}
int main()
{
	int i,j,n,t,s,p,a,b,ans,Case;
	cin>>t;
	for(Case=1;Case<=t;Case++)
	{
		cin>>n>>s>>p;
		ans=0;
		for(i=0;i<n;i++)
		{
			cin>>j;
			a=find(j,1);
			b=find(j,0);
			if(b>=p)
				ans++;
			else	if(a>=p && s>0)
			{
				ans++;
				s--;
			}
		}
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}
