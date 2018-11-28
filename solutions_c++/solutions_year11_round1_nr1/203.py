#include<iostream>
#include<utility>
#include<vector>
#include<cmath>

using namespace std;


int n;

int gcd(int a,int b)
{
 if(a<b)
  return gcd(b,a);
 if(a%b==0)
  return b;
 return gcd(b,a%b);
}


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		long long N;
		int Pd,Pg;

		cin>>N>>Pd>>Pg;

		if (Pd==0)
		{
			if (Pg==0) { printf("Possible\n"); continue; }
			else { printf("Broken\n"); continue; }
		}
		else if (Pd==100)
		{
			if (Pg==100&&N!=0) { printf("Possible\n"); continue; }
			else { printf("Broken\n"); continue; }
		}

		int k = 100/gcd(100,Pd);

		if (N<k||Pg==0||Pg==100) { printf("Broken\n"); continue; }
		printf("Possible\n");


	}
	return 0;
}
