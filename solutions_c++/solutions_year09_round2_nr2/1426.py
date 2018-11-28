#include <stdio.h>

#define DEBUG 0

int n, pam[10][2], d;

void clear(void)
{
	for(int i = 0; i < d; i++)
		pam[i][1] = 0;
}




int isSolve(int n)
{
	clear();
	int flag;

	while(n > 0)
	{
		for(int i = 0; i < d; i++)
		{
			flag = 0;
			if(pam[i][0] == n % 10 && pam[i][1] == 0)
			{
				pam[i][1] = 1;
				flag = 1;
				break;
			}
		}
		if(flag == 0 && n % 10 != 0) return 0;
		n /= 10;
	}

	for(int i = 0; i < d; i++)
		if(pam[i][1] == 0)
			return 0;
	return 1;
}

void init(int n)
{
	d = 0;

	while(n > 0)
	{
		pam[d++][0] = n % 10;
		n /= 10;
	}
}

int main()
{

	int cases;

	scanf("%d\n", &cases);

	for(int i=1;i<=cases;i++)
	{
		scanf("%d\n", &n);
		init(n);


		while(1)
		{
			n++;
			if(n == 151)
				int a = 4;
			if(isSolve(n))
			{
				printf("Case #%d: %d\n", i,n);
				break;
			}
		}


		//

	
	}
	

#if !DEBUG
	fclose (stdout);
#endif

	return 0;
}