#include<stdio.h>
#include<string.h>

#define SZ 105

char data[SZ][115] , q[1002][115];

int main()
{
	freopen("AA.in" , "r" , stdin);
	freopen("AA.out" , "w" , stdout);
	int n ,s , test , i , kase = 1 , j , k;
	scanf("%d" , &test);
	while(test--)
	{
		scanf("%d" , &n);
		scanf("\n");
		for(i = 0;i<n;i++)
			gets(data[i]);
		scanf("%d" , &s);
		scanf("\n");
		int ret = 0 , x  , l;
		for(i = 0;i<s;i++)
			gets(q[i]);
		x = -1;
		i = 0;
		while(i<s){
			l = 0;
			for(j = 0;j<n;j++)
			{
				if(j == x) continue;
				for(k = i;k<s;k++)
					if(strcmp(data[j] , q[k]) == 0)
						break;
					if(k > l){
						l = k;
						x = j;
					}
			}
			if(l < s)
				ret++;
			if(!l) i++;
			else i = l;
		}
		printf("Case #%d: %d\n" , kase++ , ret);
	}
	return 0;
}
