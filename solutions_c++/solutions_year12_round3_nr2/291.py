

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))
#define ABS(a) ((a)>(0))?(a):(a)




class BB
{
public:
	int N;
	int A;
	double D;
	double* ti;
	double* xi;
	double* ai;
	
	 BB()
	{	
	 };
	bool  virtual ReadData()
	{ 
		
		 scanf("%lf", &D);
		 scanf("%d", &N);
		 scanf("%d", &A);
		 ti=new double[N];
		xi=new double[N];
		ai=new double[A];
		
		 char endofline;

		  scanf("%c", &endofline);
		   rep(i,N)	
		   {
			   scanf("%lf", &ti[i]);
			     scanf("%lf", &xi[i]);
		   }
		    scanf("%c", &endofline);
		 
		  rep(i,A)	 
			{
				scanf("%lf", &ai[i]);
			
		  			
		  }
		     scanf("%c", &endofline);
		 
		  
		  return true;
		//reading data
	};
	void   Solve()
	{	
		ReadData();
		double time;
		double xme;
		double vme;
		double xmax;
		double dt;
		double ocspeed;
		rep(ia,A)
		{
			//time=0;
			xme=0;
			vme=0;
			if ((N==1 ) || (xi[0]>=D))
			{
				time=sqrt(2*D/ai[ia]);
			}
			else {
			rep(it,N-1)
			{
				ocspeed=(xi[it+1]-xi[it])/(ti[it+1]-ti[it]);
				if (xi[it+1]<D)
				{
					dt=ti[it+1]-ti[it];
					xmax=xme+vme*dt+0.5*ai[ia]*(dt*dt);
					if (xmax>=xi[it+1])
					{
						
						dt=(-vme+sqrt(vme*vme-2*ai[ia]*(xme-xi[it+1])))/ai[ia];
						xme=xi[it+1];
						vme=ai[ia]*dt+vme;
						time=ti[it+1];
					}
					else
					{
						xme=xmax;
						vme=vme+ai[ia]*dt;
					
						time=ti[it]+dt;
					}
	
				}
				else if (xi[it+1]==D)
				{
					dt=ti[it+1]-ti[it];
					xmax=xme+vme*dt+0.5*ai[ia]*(dt*dt);
						if (xmax>=D)
						{
							time=ti[it+1];
						}
						else
						{
							dt=(-vme+sqrt(vme*vme-2*ai[ia]*(xme-D)))/ai[ia];
							time=ti[it]+dt;
						}
				}
				else
				{//xi[it+1]>D
					dt=(D-xi[it])/ocspeed;
					xmax=xme+vme*dt+0.5*ai[ia]*(dt*dt);
					if (xmax>=D)
						{
							time=ti[it]+dt;
					}
					else
					{
						dt=(-vme+sqrt(vme*vme-2*ai[ia]*(xme-D)))/ai[ia];
						time=ti[it]+dt;
					}
				}
			}
			
			}
			printf("%lf\n",time);
		}
	};		
};


int main(int argc, char ** argv) {
   int t;
    
    char c;
	BB solver;
   char endofline;
   scanf("%d", &t);
   scanf("%c", &endofline);
   rep (i, t) {
       printf("Case #%d:\n ", i+1);
	 
	   
	    solver.Solve();
	//	scanf("%c", &endofline);
     //  printf("\n");
   }
   return 0;
}
