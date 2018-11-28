#include<stdio.h>

char a[1111][1111];
int n;
int T;

double WP(int i, int j = -1)
{
	int l1;

	int up = 0, down = 0;
	for(l1=0;l1<n;l1++) 
	{
		if(l1 == j) continue;
		if(a[i][l1] == '1')
		{
			up++; down++;
		}
		else if(a[i][l1] == '0')
		{
			down++;
		}
	}
	if(down == 0) return 0;
	return (double)up / down;
}

double OWP(int i, int j = -1)
{
	double up = 0, down = 0;
	int l1;

	for(l1=0;l1<n;l1++)
	{
		if(l1 == j) continue;
		if(a[i][l1] == '1' || a[i][l1] == '0')
		{
			up += WP(l1, i);
			down += 1;
		}
	}

	return up / down;
}

double OOWP(int i, int j = -1)
{
	int l1;

	double up = 0, down = 0;

	for(l1=0;l1<n;l1++)
	{
		if(l1 == j) continue;
		if(a[i][l1] == '0' || a[i][l1] == '1')
		{
			up += OWP(l1);
			down += 1;
		}
	}
	return up / down;
}

int main(void)
{
	int l0, l1, l2;

	freopen("A2.in","r",stdin);
	freopen("A2.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&n);
		for(l1=0;l1<n;l1++) scanf("%s",a[l1]);



		printf("Case #%d:\n",l0);
		for(l1=0;l1<n;l1++) printf("%.10lf\n",0.25*WP(l1)+0.50*OWP(l1)+0.25*OOWP(l1));
	}
	return 0;
}