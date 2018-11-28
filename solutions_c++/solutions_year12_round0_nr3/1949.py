#include <iostream>
#include <cstdio>
#include <set>
#include <cstring>
#include <string>
using namespace std;

int snum[10],n;
void retoate(int s)
{
	int tt[10];
    	n = 0;
	while(s)
	{
		tt[n++] = s%10;
		s = s/10;
	}
    	for(int i=0; i<n; i++)
    	{
        	snum[i] = tt[n-i-1];
    	}
}

int main()
{
    	int T;

   	freopen("in.in","r",stdin);
   	freopen("out.out","w",stdout);
    
    	scanf("%d",&T);
    	int A,B,ans,sum;
    	
	for(int cas=1; cas<=T; cas++)
    	{
		int temp[10];
		set<string>myset;
        	scanf("%d%d",&A,&B);
        	ans = 0;
        	for(int i=A; i<=B; i++)
        	{
            		retoate(i);
            		for(int j=1; j<n; j++)
            		{
        	        	for(int k=0; k<n; k++) 
					temp[k] = snum[(k+j)%n];
                		
				sum = 0;
                		for(int k=0; k<n; k++) 
					sum = sum*10+temp[k];
                		
				if(sum>i&&sum<=B)
                		{
                			char tt[20];
                    			sprintf(tt,"%d$%d",i,sum);
					string lin = tt;
					if(myset.find(lin)==myset.end())
					{
						ans++;
						myset.insert(lin);
					}
                		}
            		}
        	}
        	printf("Case #%d: %d\n",cas,ans);
    	}

}

