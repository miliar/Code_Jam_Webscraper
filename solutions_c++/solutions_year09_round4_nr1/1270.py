#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<map>
#define MAX 50
using namespace std;
struct data{
	int s,h,sh;
	char p[MAX];
};
class T{
	public:bool operator()(const data &a,const data &b){
			   return a.sh>b.sh;
		   };
};
char c[MAX][MAX];
char p[MAX],n;
int chk(char p[])
{
	int i,cnt;
	for(i=cnt=0;i<n;i++)
		if(p[i]>i)
			cnt+=p[i]-i;
	return (cnt+1)/2;
}
int calc(char p[])
{
	int i,cnt;
	for(i=cnt=0;i<n;i++)
	{
		cnt<<=3;
		cnt|=p[i];
	}
	return cnt;
}
int main()
{
	int cas,dd,i,j,k,ans;
	priority_queue<data,vector<data>,T> q;
	map<int,int> mp;
	data now,t;
	scanf("%d",&cas);
	for(dd=1;dd<=cas;dd++)
	{
		scanf("%d",&n);
		memset(p,0,sizeof(p));
		mp.clear();
		for(i=0;i<n;i++)
		{
			scanf("%s",c[i]);
			for(j=0;j<n;j++)
				if(c[i][j]=='1')
					p[i]=j;
		}
		while(!q.empty())
			q.pop();
		mp.insert(pair<int,int>(calc(p),1));
		t.s=0;
		t.h=chk(p);
		t.sh=t.s+t.h;
		memcpy(t.p,p,sizeof(p));
		q.push(t);
		while(!q.empty())
		{
			now=q.top();
			q.pop();
			if(now.h==0)
				break;
			for(i=1;i<n;i++)
			{
				//if(t.p[i-1]>t.p[i])
				//	continue;
				t=now;
				swap(t.p[i-1],t.p[i]);
				k=calc(t.p);
				if(mp.find(k)!=mp.end())
					continue;
				mp.insert(pair<int,int>(k,1));
				t.s++;
				t.h=chk(t.p);
				//if(t.h>now.h)
				//	continue;
				//printf("%d ",t.h);
				t.sh=t.s+t.h;
				q.push(t);
			}
		}
		printf("Case #%d: %d\n",dd,now.s);
		/*for(i=0;i<n;i++)
			printf("%d ",now.p[i]);*/
	}
	return 0;
}
