#include "stdio.h"
#include "algorithm"
using namespace std;


int getD(char s[])
{
    int dh;
	int dm;
	dh = (s[0] - '0')*10 + s[1] - '0';
	dm = (s[3] - '0')*10 + s[4] - '0';
	return dh*100 + dm;
}

int getA(char s[], int t)
{
	int ah;
	int am;
	ah = (s[6] - '0')*10 + s[7] - '0';
	am = (s[9] - '0')*10 + s[10] - '0';
	am = am + t;
	ah = ah + am/60;
	am = am%60;
	return ah*100 + am;
}

void main()
{
	int n;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d", &n);
	int now=1;
	while (now <= n)
	{
		int t;
		scanf("%d", &t);
		int na,nb;
		scanf("%d", &na);
		scanf("%d\n", &nb);

		int ad[101];
		int aa[101];

		int bd[101];
		int ba[101];

		char s[50];
		int i=0;
		for (; i<na; i++)
		{
			gets(s);
			ad[i] = getD(s);
			aa[i] = getA(s, t);
		}
		for (i=0; i<nb; i++)
		{
			gets(s);
			bd[i] = getD(s);
			ba[i] = getA(s, t);
		}

		sort(ad, ad+na);
		sort(aa, aa+na);
		sort(bd, bd+nb);
		sort(ba, ba+nb);

		int k=0,  l=0;
		int ca=0;
		for (; k<na; k++)
		{
			if (l >= nb)
			{
				ca++;
			}
			else if (ad[k] >= ba[l])
			{
				l=l+1;
			}
			else 
			{
				ca++;
			}
		}

		int cb=0;
		for (k=0,l=0; k<nb; k++)
		{
			if (l >= na)
			{
				cb++;
			}
			else if (bd[k] >= aa[l])
			{
				l++;
			}
			else
			{
				cb++;
			}
		}

		printf("Case #%d: %d %d\n", now, ca, cb);
		

		now++;
	}
}