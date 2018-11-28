#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

int P[202],V[202];
int N,D;

int solve(int ind,int j,double last,double T)
{
	if(ind==N)return 1;
	if(V[ind]==j)
	{
		return solve(ind+1,0,last,T);
	}
	double NP=max(P[ind]-T,last+(double)D);
	if(NP-last<(double)D && !(fabs((NP-last)-(double)D)<1e-9))
	{
		return 0;
	}
	
	if(NP-(double)P[ind]<T || fabs(NP-(double)P[ind])<1e-9)
	{//printf("%lf\n",NP);
		return solve(ind,j+1,NP,T);
	}
	else
	{
		return 0;
	}
}

int main()
{
    freopen ("B.in","r",stdin);
    freopen ("B.out","w",stdout);
    
    int i,k=0,T;
    
    scanf("%d",&T);
    
    while(T--)
    {
		k++;
		
		scanf("%d %d",&N,&D);
		
		fo(i,N)
		{
			scanf("%d %d",&P[i],&V[i]);
			P[i]+=100000;
		}
		double s1=0,e1=1000002;
		int k1=0;
		while(k1++<100)
		{
			double mid=(s1+e1)/2;
				int f;
				
				f=solve(0,0,-1000001.0,mid);
				//printf("%lf **\n",mid);
				if(!f)
				{
					s1=mid;
				}
				else
				{
					e1=mid;
				}
		}
		printf("Case #%d: %lf\n",k,s1);
	}
}


































