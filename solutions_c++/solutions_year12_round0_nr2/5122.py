#include <iostream>
using namespace std;
int main()
{
	   int n,s,p,q,r,i,T,t[31];
	   int sum,cnt = 1;
	   int x;
	   freopen("D:\\download\\B-small-attempt3.in","r",stdin);
	   freopen("D:\\download\\B-small-attempt3.out","w",stdout);
				scanf("%d",&T);
				while(T--)
				{
					   sum = 0;
					   scanf("%d%d%d",&n,&s,&p);
								for(int i = 0; i < n; ++i)
								{
									   scanf("%d",&t[i]);
								}	
								if(!p)
								    sum = n;
								else if(p == 1)
								{
									    for(int i = 0; i < n; ++i)
									    {
														   if(t[i] > 0)
														       ++sum;
													}
								}
								else if(p >= 2)		        
								{
								   	for(int i = 0; i < n; ++i)
								    {
								         x = t[i];
									        if(x < 3 * p - 4)
    									        continue;
									        r = x % 3;
									        q = x / 3;
									        if(q >= p)
									            ++sum;
					            else if(q == p - 1)
					            {
																		   if(!r)
																		   {
																						   if(s > 0)
																									{
																										   ++sum;
																										   --s;
                         }
																					}
																					else
																					{
																						   ++sum;
																					}
																	}
																	else if(q == p - 2 && r == 2)
																	{
																		   if(s > 0)
																		   {
																						   ++sum;
																						   --s;
																					}
																	}
								}
								}
								printf("Case #%d: %d\n",cnt++,sum);
				}
				return 0;
}
												
												 
