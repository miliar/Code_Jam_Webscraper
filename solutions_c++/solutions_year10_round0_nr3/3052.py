#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
#include<queue>
using namespace std;

__int64 n,k,r,ttl,rr,s1,siz,i;
int j;




void qq()
{

	queue<__int64> q;
	

	for(i=0;i<n;i++)
	{
		scanf("%I64d",&rr);
		q.push (rr);

	}


	ttl=0;
	siz=q.size ();
	while(r--)
	{
		rr=0;
		s1=0;
		
		for(i=0;i<siz;i++)
		{
			s1=q.front();
			if(s1+rr<=k)
			{
				rr+=s1;
				q.push(s1);
				q.pop ();
				s1=0;
			}
			else
			{
				break;
			}
		}

		ttl+=rr;
	}




}






int main()
{

	
	int t;


	freopen("A.in","r",stdin);
	freopen("B.in","w",stdout);
	scanf("%d",&t);

	while(t--)
	{
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		ttl=0;
		qq();
		printf("Case #%d: %I64d\n",++j,ttl);
	
	}
		
	
	

	return 0;
}
