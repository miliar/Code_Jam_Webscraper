#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

#define coutfpre(n,f) (setiosflags(ios::fixed)<<setprecision(n)<<f) 
#define zero(n) memset(n,0,sizeof(n))
#define m1set(n) memset(n,-1,sizeof(n))
#define min(m,n) ((m<n)?m:n)
#define max(m,n) ((m>n)?m:n)

int main()
{
	int T;
    freopen("A.in" , "r" , stdin);
    freopen("A.out" , "w" , stdout);
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
		int N,pd,pg,i100;
		int possible;
		cin>>N;
		cin>>pd;
		cin>>pg;
		i100 = 100;
		possible = 0;

		if(0 == pg)
		{
			if(0 == pd)
			{
				possible = 1;
			}
			else
			{
				possible = 0;
			}
		}
		else if(100 == pg)
		{
			if(100 == pd)
			{
				possible = 1;
			}
			else
			{
				possible = 0;
			}
		}
		else
		{
				if(0 == pd%2)
				{
					pd/=2;
					i100/=2;
					if(0 == pd%2)
					{
						pd/=2;
						i100/=2;
					}
				}
				if(0 == pd%5)
				{
					pd/=5;
					i100/=5;
					if(0 == pd%5)
					{
						pd/=5;
						i100/=5;
					}
				}

				if(i100<=N)
				{
					possible = 1;
				}
				else
				{
					possible = 0;
				}
		}

        cout<<"Case #"<<caseID<<": ";
		if(possible)
		{
			cout<<"Possible"<<endl;
		}
		else
		{
			cout<<"Broken"<<endl;
		}
    }
    return 0;
}
