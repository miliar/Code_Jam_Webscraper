#include<iostream>
#include<cstdio>
using namespace std;

int gcd(int a,int b)
{
	if (a == 0) return b;
	return gcd(b % a,a);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int task,cases(0);
	scanf("%d",&task);
	while (task--)
	{
		cases++;
		long long n;
		int PD,PG;
		scanf("%I64d %d %d",&n,&PD,&PG);
		int p1,p2,q1,q2,t2,g;
		g = gcd(PD,100);
		if (g == 0) g = 100;
		p1 = PD / g; q1 = 100 / g;
		/*
		g = gcd(PG,100);
		if (g == 0) g = 100;
		p2 = PG / g; q2 = 100 / g;
		*/
		bool flag(false);
		//if (PD == PG) flag = true; 
			//else
			{
				if ((PG == 0 && PD !=0)|| (PG == 100 && PD !=100)) flag = false;
					else
					{
						if (q1<=n) flag = true;
							else flag = false;
					}
			}
		if (!flag) printf("Case #%d: Broken\n",cases);
			else printf("Case #%d: Possible\n",cases);
			
	}
	return 0;
}
