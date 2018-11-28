#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	freopen("lin.in","r",stdin);
	freopen("lans.out","w",stdout);
    int _,cas=0,n;
    scanf("%d",&_);
    while(_--)
    {
    	scanf("%d",&n);
    	int pos[2]={1,1};
    	int preTime[2]={0,0};
    	int ans=0;
    	for(int i=0;i<n;i++)
    	{
    		char s[2];
    		int to,flag;
    		scanf("%s%d",s,&to);
    		if(s[0]=='O') flag=0;
    		else flag=1;
    		if(preTime[flag^1]>=abs(to-pos[flag]))
    		{
    			ans++;
    			preTime[flag]++;
    		}
    		else
    		{
    			ans+=abs(to-pos[flag])+1-preTime[flag^1];
    			preTime[flag]+=abs(to-pos[flag])+1-preTime[flag^1];
    		}
    		preTime[flag^1]=0;
    		pos[flag]=to;
    	}
    	printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
