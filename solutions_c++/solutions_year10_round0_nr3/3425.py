#include <stdio.h>
#include <string.h>

#define M 1005

struct node
{
   int sign;
   int len;
   __int64 sum;
}b[M][M];

int a[M],n;

__int64 get(int r)
{
	int i,j,sign = 0;
	for(i = 0; i<n; i++)
	{
		for(j = 0; j<n; j++)
			if(b[i][j].len == r)
			{
				sign = 1;
				break;
			}
			if(sign)
				break;
	}
    return b[i][j].sum;
}

int main()
{
    int t;
    int r,k;
	int i,j;
	int start,end;
	int sum = 0;
	int len = 0;
	int sign = 0;
	int cas = 0;
	__int64 forward = 0;
    __int64 s = 0;

    scanf("%d",&t);
	while(t--)
	{
	    scanf("%d%d%d",&r,&k,&n);
	    for(i = 0; i<n; i++)
		{
			scanf("%d",&a[i]);
			for(j = 0; j< n; j++)
			{
				b[i][j].sign = 0;
				b[i][j].len = 0;
				b[i][j].sum = 0;
			}
		}
	//	memset(b,0,sizeof(b));
		start = 0;
		end = n-1;
		len = 0;
		forward = 0;
		while(1)
		{
           i = start;
		   j = 0;
		   sum = 0;
		   while(sum + a[i]<= k && j<n)
		   {
			   sum += a[i];
			   i++;
			   j++;
			   if(i == n)
				   i = 0;
		   }
		   len++;
		   forward += sum;
		   b[start][end].sign = 1;
		   b[start][end].sum = forward;
		   b[start][end].len = len;
		   end = (i - 1 + n)%n;
		   start = i;
		   if(b[start][end].sign)
			   break;
		}

		printf("Case #%d: ",++cas);
		if(r<= len)
           printf("%I64d\n", get(r));
		else
		{
		   len = len - b[start][end].len + 1;
		   forward =forward - (s = get(b[start][end].len - 1));
		   r -= b[start][end].len - 1;
		   sum = r%len;
		   sum += b[start][end].len - 1;
		   if(sum == 0)
		   {
			   printf("%I64d\n",s + (r/len)*forward);
			   continue;
		   }
		   sign = 0;
		   for(i = 0; i<n; i++)
		   {
			   for(j = 0; j<n; j++)
				   if(b[i][j].len == sum)
				   {
					   sign = 1;
					   printf("%I64d\n",b[i][j].sum + (r/len)*forward);
					   break;
				   }
			   if(sign)
			       break;
		   }
		}  
	}
	return 0;
}