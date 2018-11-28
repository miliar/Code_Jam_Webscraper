#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>


__int64 powerof(__int64 x, __int64 y)
{
	__int64 p = 1;
	__int64 i;

	for(i=0; i<y; i++)
		p *= x;
	
	return p;
}


int main(void)
{	
	//freopen("c:\\IO\\A-large.in", "rt", stdin);
	//freopen("c:\\IO\\A-large_out.out", "wt", stdout);

	__int64 i, j, k, len, t, base, index, res;
	char num[256];
	char visited[256];
	__int64 val[256], digits[256];

	scanf(" %I64d " ,&t);


	for(i=1; i<=t; i++)
	{
		scanf( " %s" ,num);
		len = (__int64)strlen(num);
		memset(visited, 0, sizeof(visited));
		index = 0;

		for(j=0; j<len; j++)
		{
			if(visited[num[j]] == 1)
			{
				digits[j] = val[num[j]];
			}

			else
			{
				if(j==0)
				{
					digits[j] = 1;
					val[num[j]] = 1;
					index = 1;
				}

				else if(index == 1)
				{
					digits[j] = 0;
					val[num[j]] = 0;
					index = 2;
				}
				
				else
				{
					digits[j] = index;
					val[num[j]] = index++;
				}

				visited[num[j]] = 1; 
			}
		}

		base = index;

		if(base < 2)
			base = 2;

		res = 0;
		for(j=len-1, k=0; j>=0 ;j--,k++)
		{
			res += digits[j] * powerof(base, k);
		}


		printf("Case #%I64d: %I64d\n" ,i ,res);
	
	}


	return 0;
}


