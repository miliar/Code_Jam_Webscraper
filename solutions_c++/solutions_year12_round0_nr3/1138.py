#include <iostream>
using namespace std;

char map[2000001];
int table[]={0,1,10,100,1000,10000,100000,1000000,10000000},D[10];
/*
int test(int a)
{
	int i,j=a;
	while(j)
	{
		i=j%10;
		if(D[i]==a)
			return 0;
		else
			D[i]=a;
		j = j/10;
	}
	return 1;
}
*/

int main()
{
	int i,j,T,A,B,cases=0;
	int num,digits,len,cnt;

	//freopen("D:\\C4.in", "r", stdin);
	freopen("G:\\chrome��������\\C-large.in", "r", stdin);
	freopen("D:\\C-large.out", "w", stdout);
	scanf("%d",&T);
	while(++cases<=T)
	{
		scanf("%d%d", &A, &B);
		num = 0;
		memset(map, 0, sizeof(map));
		memset(D, 0, sizeof(D));
		digits = A;
		len = 0;
		while(digits)
		{
			len++;
			digits/=10;
		}

		i=A;
		while(i<=B)
		{
			if(map[i]==0)
			{
				cnt = 1;
				digits = i;
				map[digits] = 1;
				for(j=1; j<len; j++)
				{
					digits = digits%table[len]*10+(digits/table[len]);
					//digits = digits/10+(digits%10*table[len]);
					if(digits>=A && digits<=B && map[digits]==0)
					{
						cnt++;
						map[digits]=1;
					}
				}
				if(cnt > 1)
					num += cnt*(cnt-1)/2;
			}
			i++;
		}
		printf("Case #%d: %d\n",cases, num);
	}
}