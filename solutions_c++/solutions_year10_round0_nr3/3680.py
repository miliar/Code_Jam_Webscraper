#include <iostream>
#include<queue>
#include<conio.h>
using namespace std;
int main()
{
	__int64 i,n,k,r,x,f,len;
	int t,l=1;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	queue<__int64>q;
	scanf("%d",&t);
	while(t--)
	{
		while(q.size())q.pop();
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		
		for(i=0;i<n;i++)
		{
			scanf("%I64d",&f);
			q.push(f);
		}
		__int64 sum=0;
		while(r--)
		{
			x=k;
			f=q.front();
			len=0;
			while(x>=f&&len<n)
			{
				sum+=f;
				x-=f;
				q.pop();
				q.push(f);
				f=q.front();
				len++;
			}
			
		}
		printf("Case #%d: %I64d\n",l++,sum);
	}
	return 0;
}