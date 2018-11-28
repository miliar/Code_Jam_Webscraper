#include <iostream>
using namespace std;

const int MAX_EL = 1000;
const int MINS_IN_A_DAY = 24*60;

int aa[MAX_EL], ad[MAX_EL], ba[MAX_EL], bd[MAX_EL];

int scan()
{
	int x, y;
	scanf("%d%*c%d", &x, &y);
	return x * 60 + y;
}

int main()
{
	int i, j, k, n;
	int na, nb, t;
	int z = 1;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &n);

	for(;n--;z++)
	{
		int a = 0, b = 0;
		int ares = 0, bres = 0;
		int adi=0, bai=0, bdi=0, aai=0;
		scanf("%d%d%d", &t, &na, &nb);
		
		for(i=0; i<na; i++)
		{
			ad[i] = scan();
			ba[i] = scan()+t;
		}
		
		for(i=0; i<nb; i++)
		{
			bd[i] = scan();
			aa[i] = scan()+t;
		}
		sort(ad, ad+na);
		sort(ba, ba+na);
		sort(bd, bd+nb);
		sort(aa, aa+nb);
		
		for(j=0; j<MINS_IN_A_DAY; j++)
		{
            while(bai < na && j == ba[bai])
			{
				b++;
				bai++;
			}
			
			while(aai < nb && j == aa[aai])
			{
				a++;
				aai++;
			}
			

			while(adi < na && j == ad[adi])
			{
				if(a > 0)
				{
					a--;
				}
				else
				{
					ares++;
				}
				adi++;
			}
			
			while(bdi < nb && j == bd[bdi])
			{
				if(b > 0)
				{
					b--;
				}
				else
				{
					bres++;
				}
				bdi++;
			}
		}
		
		printf("Case #%d: %d %d\n", z, ares, bres);
	}

	return 0;
}
