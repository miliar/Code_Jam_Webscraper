#include <cstdio>
bool t[20000005];
int tt, a, b, suma, c, p, temp, m;
int pot[8]={0, 1, 10, 100, 1000, 10000, 100000, 1000000};
int mm[9]={0, 1, 3, 6, 10, 15, 21, 28};
int main()
{
	scanf("%d", &tt);
	for(int i=1; i<=tt; i++)
	{
		scanf("%d%d", &a, &b);
		temp=a;
		while(temp)
		{
			c++;
			temp/=10;
		}
		for(int j=a; j<=b; j++)
		{
			if(t[j]==0)
			{
				t[j]=1;
				p=j;
				for(int k=0; k<c; k++)
				{
					p=(p%10)*pot[c]+(p/10);
					if(t[p]==0 && p<=b && p>=a){t[p]=1;m++;}
				}
			}
			suma+=mm[m];
			m=0;
		}
		printf("Case #%d: %d\n", i, suma);
		suma=0;c=0;
		for(int q=a; q<=b; q++)	t[q]=0;
	}
	return 0;
}
