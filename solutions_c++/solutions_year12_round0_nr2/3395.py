#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int main()
{
    int t,n,s,p,i,j;
    int count;
    int a[100];
    scanf("%d", &t);
    j=1;
    while(t--)
    {
    	count=0;
    	scanf("%d%d%d", &n, &s, &p);
    	for(i=0;i<n;i++) scanf("%d", &a[i]);
    	for(i=0;i<n;i++)
    	{
    		if(a[i]>0||p==0)
    		{
				if((a[i]+2)/3 >= p)
				{
						count++;
				}
				else if((a[i]+4)/3 >= p)
					{
					if(s!=0)
					{
						count++;
						s--;
					}
				else;
				}
			}
		}
    	printf("Case #%d: %d\n", j, count);
    	j++;
    }
    return 0;
}
