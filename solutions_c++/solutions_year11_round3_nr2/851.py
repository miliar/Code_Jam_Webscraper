#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

#define coutfpre(n,f) (setiosflags(ios::fixed)<<setprecision(n)<<f) 
#define zero(n) memset(n,0,sizeof(n))
#define m1set(n) memset(n,-1,sizeof(n))
#define p1set(n) memset(n,1,sizeof(n))

#define min(m,n) ((m<n)?m:n)
#define max(m,n) ((m>n)?m:n)

int a[10000];
int b[10000];
int main()
{
	int T;
    freopen("A.in" , "r" , stdin);
    freopen("A.out" , "w" , stdout);
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
		long long L,T,N,C;
		long long  out =0;
		cin>>L>>T>>N>>C;
		for(int i =0; i<C;i++)
		{
			cin>>a[i];
		}

		if(0 == L)
		{
			for(int i=0; i<N;i++)
			{
				out += (2* a[i%C]);
			}
		}
		else if(1 == L)
		{	
			int isbig = 0;
			long long b=0;
			for(int i=0; i<N;i++)
			{
				out += 2* a[i%C];
				if(isbig == 0)
				{
					if(out>=T)
					{
						b= (out-T)/2;
						isbig=1;
					}
				}
				else
				{
					b = max(b,a[i%C]);
				}
			}
			if(0!=b)
			{
				out -= b;
			}
		}
		else if(2 == L)
		{	
			int isbig = 0;
			long long b=0,c=0;
			for(int i=0; i<N;i++)
			{
				out += 2* a[i%C];
				if(isbig == 0)
				{
					if(out>=T)
					{
						c= (out-T)/2;
						isbig=1;
					}
				}
				else
				{
					if(a[i%C]>c)
					{b = c;
						c = a[i%C];
						
					}
					else if(a[i%C]>b)
					{
						b = a[i%C];
					}
					
				}
			}

			if(0!=b)
			{
				out -= b;
			}
			if(0!=c)
			{
				out -= c;
			}
		}
		cout<<"Case #"<<caseID<<": "<<out<<endl;
    }
    return 0;
}
