#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

int main()
{
    int t,a,b,i,j,k,len, temp, tmp1, tmp2;
    int ans;
    scanf("%d", &t);
    j=1;
    while(t--)
    {
		scanf("%d%d", &a,&b);
		ans=0;
		for(i=a;i<b;i++)
		{
			k=i;
			for(len=0;k>0;len++,k/=10);
			//printf("\nlen=%d\n", len);
			for(k=1;k<len;k++)
			{
				tmp1 = pow(10,k);
				tmp2 = pow(10,len-k);
				temp = (i/tmp1 + tmp2*(i%tmp1));
				if(temp<=b&&i<temp)
				{
					//printf("%d\t%d\t%d\n", i, temp, ans);
					ans++;
				}
			}
		}
    	printf("Case #%d: %d\n", j, ans);
    	j++;
    }
    return 0;
}
