#include <stdio.h>
inline int abs(int x)
{
	return x>0?x:-x;
}

int u, a[1000], b[1000], d[1000];
void init()
{
	int n, sumb, sumd,s,t,ss,tt;
	sumb = 0;
	sumd = 0;
	char c;
	scanf("%d", &n);
	int current;
	current = 0;
	for (int i = 0; i < n; i++)
	{
		getchar();
		scanf("%c", &c);
		if (c == 'O')
		{
			a[i] = 0;
			scanf("%d", &b[sumb++]);
		}
		else
		{
			a[i] = 1;
			scanf("%d", &d[sumd++]);
		}
	}
	s=1;ss=0;
	t=1;tt=0;
	int total=0;
	for (int i=0;i<n;i++)
	{
		if (a[i]==0)
		{
			total+=abs(b[ss]-s)+1;
			if (abs(d[tt]-t)>abs(b[ss]-s)+1)
			{
				if (d[tt]>t)
				{
					t=t+abs(b[ss]-s)+1;
				}
				else
				{
					t=t-abs(b[ss]-s)-1;
				}
			}
			else
			{
				t=d[tt];
			}
			s=b[ss];
			ss++;
		}
		else
		{
			total+=abs(d[tt]-t)+1;
			if (abs(b[ss]-s)>abs(d[tt]-t)+1)
			{
				if (b[ss]>s)
				{
					s=s+abs(d[tt]-t)+1;
				}
				else
				{
					s=s-abs(d[tt]-t)-1;
				}
			}
			else
			{
				s=b[ss];
			}
			t=d[tt];
			tt++;
		}
	}
	printf("Case #%d: %d\n",u,total);
}
int main()
{
	int w;
	scanf("%d",&w);
	while (w--)
	{
		u++;
		init();
	}
	return 0;
}
