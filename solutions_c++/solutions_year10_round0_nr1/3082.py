#include<stdio.h>
#include<string.h>
#include<math.h>

char arr[65];

int makeBinary(int n)
{
	int i=0;
	while(n)
	{
		int r = n%2;
		arr[i++] = r;
		n/=2;
	}
	return i;
}
int main(void){
	int T;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int t=1; t<=T;t++)
	{
		int sn,move;
		scanf("%d%d",&sn,&move);

		int con = 0;
		if(move == 0)
		{
			con = 0;
		}
		else if(sn == 1)
		{
			if(move % 2)
				con = 1;
			else
				con = 0;
		}
		else
		{
			int sat = pow(2,sn) - 1;
			if(move < sat)
			{
				con = 0;
			}
			else if(move == sat)
			{
				con = 1;
			}
			else
			{
				int rem = move - sat;
				if(rem % (sat + 1) ==0)
				{
					con = 1;
				}
				else
				{
					con = 0;
				}
			}
		}
		
		if(con)
		{
			printf("Case #%d: ON",t);
		}
		else
		{
			printf("Case #%d: OFF",t);
		}
		puts("");
	}
	return 0;
}