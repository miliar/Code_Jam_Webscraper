#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cassert>
#include<ctime>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>

#define PB push_back
#define M 100
#define N 100
#define LL long long


using namespace std;


long long gcd(LL a, LL b)
{
	//printf("%d %d\n",a,b);
	if(b==0)
	return a;
	else
	return gcd(b,a%b);
	
}



int main()
{
	
	int tc,ti;
	scanf("%d",&tc);
	for(ti=1;ti<=tc;++ti)
	{
		long long a,b,x,y,t1,t2,pd,pg,n,ob;
		cin>>n>>pd>>pg;
		//cout<<n<<" "<<pg<<" "<<pd<<endl;
		//scanf("%d %d %d",&n,&pd,&pg);
	if(pg==100&&pd!=100)
	{
	printf("Case #%d: Broken\n",ti);
	continue;
	}
	if(pg==0&&pd!=0)
	{
	printf("Case #%d: Broken\n",ti);
	continue;
	}
	if(pg==100&&pd==100)
	{
	printf("Case #%d: Possible\n",ti);
	continue;
	}
	t1=gcd(pd,100);
	a=pd/t1;
	b=100/t1;
	t2=gcd(pg,100);
	x=pg/t2;
	y=100/t2;
	
	
	ob=b;
	
	
	if(ob<=n)
	{
		
		printf("Case #%d: Possible\n",ti);
	} 
	else
	{
	printf("Case #%d: Broken\n",ti);
	}
	}
	
	return 0;
}
