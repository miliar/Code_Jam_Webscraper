// Author : Muhammad Rifayat Samee
// Problem :  A
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>

#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;

struct Node
{
	char c[105];
}N[105];

int n;

double WP(int num,int f,int p)
{
	int i,j;
	double res,r,t;
	r = 0;
	t = 0;
	i =num;
		for(j=0;j<n;j++)
		{
			if(f == 0)
			{
				
					if(N[i].c[j]!='.')
						t++;
					if(N[i].c[j] =='1')
						r++;
		

				
			}
			else
			{
									
					if(N[i].c[j]!='.')
						t++;
					if(N[i].c[j] =='1')
						r++;
		

					
			}
		}
	
	 if(N[i].c[p]!='.'&&f)
		 t--;

	 if(N[i].c[p]=='1' &&f)
		 r--;

	
	res = (double)r/t;
	
	return res;

}

double OWP(int num)
{
	int i;
	double t,r;
	
	t = 0;
	r = 0;

	for(i=0;i<n;i++)
	{
		if(i!=num && N[i].c[num]!='.')
		{
			t = t + WP(i,1,num);
			r++;
		}

	}

	r = t/r;
	return r;


}

double OOWP(int num)
{
	int i;
	double r,t;
	r = 0;
	t = 0;

	for(i=0;i<n;i++)
	{
		if(i!=num && N[i].c[num]!='.')
		{
			t = t + OWP(i);
			r++;
		}
	}

	r = t/r;
	return r;

}


int main()
{
	//freopen("a_l.in","r",stdin);
	//freopen("a_out.txt","w",stdout);
	int cases,i,j,k,ct=1;
	double res;

	scanf("%d",&cases);
	
	while(cases--)
	{
		scanf("%d",&n);

		for(i=0;i<n;i++)
		{
			scanf("%s",N[i].c);

		}
		
		printf("Case #%d:\n",ct++);

		for(i=0;i<n;i++)
		{
			res = 0.25 * WP(i,0,0) + 0.50 * OWP(i) + 0.25 * OOWP(i);

			printf("%.10lf\n",res);


		}
		
	}

	return 0;


}
