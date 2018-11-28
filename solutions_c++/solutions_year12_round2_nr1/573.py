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

int arr[202];

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	
	int T,k=0;
	
	scanf("%d",&T);
	
	while(T--)
	{
		k++;
		int N;
		scanf("%d",&N);
		int X=0;
		
		for(int i=0;i<N;i++)
		{
			scanf("%d",&arr[i]);
			X+=arr[i];
		}
		
		int l;
		
		printf("Case #%d:",k);
		
		for(int i=0;i<N;i++)
		{
			l=0;
			double s=0,e=1.0;
			while(l++<400)
			{
				double mid=(s+e)/2.0;
				
				double S=1-mid;
				
				for(int j=0;j<N;j++)
				{
					if(j==i)continue;
					
					double d=((arr[i]+X*mid)-arr[j])/(double)X;
					//printf("%d %lf %lf\n",X,arr[i]+X*mid,d);
					if(d>0)S-=d;
				}
				//printf("%lf %lf %lf\n",s,e,S);
				
				if(S>0 && !(fabs(S)<=1e-12))
				{
					s=mid;
				}
				else e=mid;
			}
			
			printf(" %lf",s*100.0);
		}
		printf("\n");
		
	}
	
}



































