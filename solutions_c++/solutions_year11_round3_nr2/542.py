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

long long acc[1005];
int arr[1005];

int main()
{
    freopen ("B.in","r",stdin);
    freopen ("B.out","w",stdout);
    
    int i,j,k=0,T;
    long long t;
    int L,N,C;
    
    scanf("%d",&T);
    while(T--)
    {
		k++;
		scanf("%d %lld %d %d",&L,&t,&N,&C);
		fo(i,C)scanf("%d",&arr[i]);
		
		long long ret=0;
		
		if(!L)
		{
			fo(i,N)
			{
				ret+=arr[i%C]*2;
			}
			printf("Case #%d: %lld\n",k,ret);
		}
		if(L==1)
		{
			long long RET=pow(10,18);
			
			acc[0]=arr[0]*2;
			fo(i,N)
			{
				if(i)acc[i]=acc[i-1]+arr[i%C]*2;
			}
			fo(i,N)
			{
				ret=(i==0)?0:acc[i-1];
				if(t<=ret)
				{
					ret+=arr[i%C];
				}
				else
				{
					if(t>=ret+arr[i%C]*2)ret+=arr[i%C]*2;
					else
					{
						ret=ret+(t-ret)+(arr[i%C]-(t-ret)/2);
					}
				}
				ret+=acc[N-1]-acc[i];//printf("%lld **\n",ret);
				RET=min(ret,RET);
			}
			printf("Case #%d: %lld\n",k,RET);
		}
		if(L==2)
		{
			long long RET=pow(10,18);
			
			acc[0]=arr[0]*2;
			fo(i,N)
			{
				if(i)acc[i]=acc[i-1]+arr[i%C]*2;
			}
			fo(i,N)for(j=i+1;j<N;j++)
			{
				ret=(i==0)?0:acc[i-1];
				if(t<=ret)
				{
					ret+=arr[i%C];
				}
				else
				{
					if(t>=ret+arr[i%C]*2)ret+=arr[i%C]*2;
					else
					{
						ret=ret+(t-ret)+(arr[i%C]-(t-ret)/2);
					}
				}
				
				ret+=acc[j-1]-acc[i];
				
				if(t<=ret)
				{
					ret+=arr[j%C];
				}
				else
				{
					if(t>=ret+arr[j%C]*2)ret+=arr[j%C]*2;
					else
					{
						ret=ret+(t-ret)+(arr[j%C]-(t-ret)/2);
					}
				}
				ret+=acc[N-1]-acc[j];
				
				RET=min(ret,RET);
			}
			printf("Case #%d: %lld\n",k,RET);
		}
		
	}
}


































