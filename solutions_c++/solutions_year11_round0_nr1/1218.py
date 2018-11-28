#include <stdio.h>


int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t, test, n, nr, counto, countb;
	int o[128], b[128];
	int o2[128], b2[128];
	int co, cb;
	char ch;
	scanf("%d", &t);

	for(int test = 1; test <= t; ++test)
	{
		o[0] = b[0] = 0;
		counto = countb = 1;
		co = cb = 1;
		scanf("%d ", &n);
		for(int i = 0; i < n; ++i)
		{
			scanf(" %c %d ", &ch, &nr);
			if(ch == 'O')
			{
				o[++o[0]] = nr;
				o2[o[0]] = i;
			}
			else
			{
				b[++b[0]] = nr;
				b2[b[0]] = i;
			}
		}
		int sol = 0;
		while(counto <= o[0] || countb <= b[0])
		{
			++sol;
			if(counto <= o[0])
			{
				if(countb <= b[0])
				{
					if(o2[counto] < b2[countb])
					{
						if(co < o[counto])
						{
							++co;
						}
						else if(co > o[counto])
						{
							--co;
						}
						else
						{
							++counto;
						}
						if(cb < b[countb])
						{
							++cb;
						}
						if(cb > b[countb])
						{
							--cb;
						}
					}
					else
					{
						if(co < o[counto])
						{
							++co;
						}
						else if(co > o[counto])
						{
							--co;
						}
						if(cb < b[countb])
						{
							++cb;
						}
						else if(cb > b[countb])
						{
							--cb;
						}
						else
						{
							++countb;
						}
					}
				}
				else
				{
					if(co < o[counto])
					{
						++co;
					}
					else if(co > o[counto])
					{
						--co;
					}
					else
					{
						++counto;
					}
				}
			}
			else
			{
				if(cb < b[countb])
				{
					++cb;
				}
				else if(cb > b[countb])
				{
					--cb;
				}
				else
				{
					++countb;
				}

			}
		}
		printf("Case #%d: %d\n", test, sol);
	}

	return 0;
}
