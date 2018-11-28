#include <cstdio>
struct snapper
{
	bool power;
	bool on;
};
snapper s[12];
int main ()
{
	int T;
	scanf("%d",&T);
	int cas=0;
	while (T--)
	{
		int n;
		int k;
		scanf ("%d %d", &n, &k);
		for (int i=0;i<n;i++)
		{
			s[i].power = false;
			s[i].on = false;
		}
		s[0].power = true;
		for (int i=0;i<k;i++)
		{
			for (int j=0;j<n;j++)
			{
				if (s[j].power)
					s[j].on=s[j].on?false:true;
			}
			for (int j=0;j<n;j++)
			{
				if (s[j].power && s[j].on)
					s[j+1].power=true;
				else
					s[j+1].power=false;
			}
		}
		if (s[n-1].power && s[n-1].on)
			printf ("Case #%d: ON\n", ++cas);
		else
			printf ("Case #%d: OFF\n", ++cas);
	}

	return 0;
}