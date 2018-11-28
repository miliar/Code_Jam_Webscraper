#include<stdio.h>
#include<iostream>
#define MAX 110
int a[MAX][MAX];
long double vals[MAX][3];

void calc_wp(int n)
{
	int i, j;
	int loss, win;
	for(i=0; i<n; ++i)
	{
		loss = 0;
		win = 0;
		for(j=0; j<n; ++j)
		{
			if(a[i][j] == 0)
				loss ++;
			else if(a[i][j] == 1)
				win ++;
		}
//		printf(">>%d win %d %d\n", i, win, loss);
		vals[i][0] = 1.0*win/(win+loss);
	}
}

void calc_owp(int n)
{
	int i, j, k;
	long double owp;
	int win, loss, n_opp;
	for(i=0; i<n; ++i)
	{
		owp = 0;
		n_opp = 0;//no. of opp
		for(j=0; j<n; ++j)
		{
			if(a[i][j] != 2)
			{
				n_opp ++;
				win = 0;
				loss = 0;
				for(k=0; k<n; ++k)
				{
					if(k != i)
					{
						if(a[j][k] == 1)
							win++;
						else if(a[j][k] == 0)
							loss++;
					}

				}
				owp += 1.0*win/(win+loss);
			}
		}
		owp = 1.0*owp/n_opp;
		vals[i][1] = owp;
	}
}
		

void calc_oowp(int n)
{
	int i;
	long double oowp;
	int n_opp, j;
	for(i=0; i<n; ++i)
	{
		oowp = 0;
		n_opp = 0;
		for(j=0; j<n; ++j)
		{
			if(a[i][j] != 2)
			{
				oowp += vals[j][1];
				n_opp ++;
			}
		}
		oowp = 1.0*oowp/n_opp;
		vals[i][2] = oowp;
	}
}





int main()
{
	int t;
	scanf("%d", &t);
	int tp = 0;
	int n;
	int i,j;
	char temp;
	long double rpi;
	while(t--)
	{
		tp++;
		scanf("%d", &n);
		for(i=0; i<n; ++i)
		{
			getchar();
			for(j=0; j<n; ++j)
			{
				scanf("%c", &temp);
				if(temp == '.')
				{
					a[i][j] = 2;
				}
				else
				{
					a[i][j] = (int)temp - '0';
				}
			}

		}
/*		printf("print\n");
		for(i=0; i<n; ++i)
		{
			for(j=0; j<n; ++j)
			{
			printf("%d ", a[i][j]);
			}
			printf("\n");
		}
		printf(">>");*/
		calc_wp(n);
		calc_owp(n);
		calc_oowp(n);
		printf("Case #%d:\n", tp);
		for(i=0; i<n; ++i)
		{
			rpi = 0.25*vals[i][0] + 0.5*vals[i][1] + 0.25*vals[i][2];
//			printf("%Lf %llf %llf <<\n", vals[i][0], vals[i][1], vals[i][2]);
			printf("%Lf\n", rpi);

		}
	}
	return 0;
}



