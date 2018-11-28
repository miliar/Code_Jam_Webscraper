#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;
int tes,n,p1,p2,q1,q2,ans;


int gcd(int a,int b)
{
	if (a==0) return b;
	if (b==0) return a;
	return gcd(b,a%b);
}

int main()
{
	freopen("a0.out","w",stdout);
	scanf("%d",&tes);
	for (int ttt=1;ttt<=tes;ttt++)
	{
		scanf("%d%d%d",&n,&p1,&p2);
		ans=0;
		int g=gcd(p1,100);
		p1/=g; q1=100/g;
		g=gcd(p2,100);
		p2/=g; q2=100/g;
	//	cout <<p1<<" "<<q1<<" "<<p2<<" "<<q2<<endl;
		for (int D=1;D<=n;D++)
		{
			if (D*p1%q1!=0) continue;
			int wd=D*p1/q1;
			if (p2==q2) 
			{
				if (wd==D) ans=1;
			}
			else
			{
				int c=D*p2-wd*q2;
				for (int d=0;d<=1000000;d++)
				{
					if (c+d*p2<0) continue;
					if ((c+d*p2)%(q2-p2)==0) {ans=1; break; }
				}
			}
			if (ans) break;
		}
		printf("Case #%d: ",ttt);
		if (ans) printf("Possible\n");
		else printf("Broken\n");
	}
	return 0;
}
