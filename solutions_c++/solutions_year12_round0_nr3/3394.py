#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
using namespace std;
int nod(int n)
{
	int i;
	for(i=0;n>0;i++)
		n/=10;
	return i;
}
int main()
{
	int t,i,j,k,n,a,b,cunt,l,r,pp,pre;
	//freopen("example.txt","r",stdin);
	//freopen("aaa.txt","w",stdout);
	scanf("%d",&t);
	int zz=1;
	while(t--)
	{
		scanf("%d%d",&a,&b);
		//cout<<a<<" "<<b<<endl;
		cunt=0;
		pre=0;
		if(a<10)
			i=10;
		for(i=a;i<=b;i++)
		{
			//cout<<"beep"<<endl;
			n=i;
			l=nod(n);
			//cout<<l<<endl;
			if(pre!=l)
			{
				pp=pow(10,l-1);
				pre=l;
			}
			for(j=1;j<l;j++)
			{
				r=n%10;
				n=n/10;
				n=n+pp*r;
				//cout<<n<<endl;
				if(r==0)
					continue;
				if(n<=b&&n>i)
				{
					//cout<<i<<" "<<n<<endl;
					cunt++;
				}
			}
		}
		printf("Case #%d: %d\n",zz,cunt);
		zz++;
		
	}
	return 0;
}