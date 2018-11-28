#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int num[105];

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);

	int T,cas;
	scanf("%d",&T);
	
	int n,s,p;
	for(cas=1;cas<=T;cas++)
	{
		int ans = 0,cot = 0,tt = 0;
		scanf("%d%d%d",&n,&s,&p);
	        for(int i=0; i<n; i++)
	        {
	            	scanf("%d",&num[i]);
	            	if(num[i]>=3*p-2)
				cot++;
			else if(num[i]<3*p-4)
			{}
	        	else if(num[i]>=2) 
			    	tt++;
	        }
	        ans = cot + (s>tt?tt:s);
	        printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
