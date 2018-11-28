
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

const int N=100;
int t, n;
int a[N], b[N];

int main()
{
	//freopen("A-small-attempt3.in", "r", stdin);
	//freopen("A-small-attempt3.out", "w", stdout);
	int i, j, k, io, ib, iio, iib, cnt, cas1, tmp;
	scanf("%d", &t);
	for(cas1=1; cas1<=t; cas1++)
	{
		scanf("%d", &n);
		for(i=1; i<=n; i++)
		{
			scanf(" %c %d", &a[i], &b[i]);
			//printf(" %c %d", a[i], b[i]);
		}
		iio = iib = n+1;
		io = ib = 1;
		
		for(i=1; i<=n; i++)
			if(a[i]=='O')
			{
				iio = b[i];
				break;
			}
		for(j=1; j<=n; j++)
			if(a[j]=='B')
			{
				iib = b[j];
				break;
			}
		cnt = 0;
		while(i<=n || j<=n)
		{
			if(i<j)
			{
				tmp = (abs(io-iio)+1);
				io = iio;
				for(i++; i<=n; i++)
					if(a[i]=='O')
					{
						iio = b[i];
						break;
					}
				
				if(tmp>=abs(ib-iib)+1)
					ib = iib;
				else
					if(iib>ib)
						ib += tmp;
					else
						ib -= tmp;
				cnt += tmp;
			}
			else
			{
				tmp = abs(ib-iib)+1;
				ib = iib;
				for(j++; j<=n; j++)
					if(a[j]=='B')
					{
						iib = b[j];
						break;
					}
				if(tmp>=abs(io-iio)+1)
					io = iio;
				else
					if(iio>io)
						io += tmp;
					else
						io -= tmp;
				cnt += tmp;
			}
		}
		printf("Case #%d: %d\n", cas1, cnt);
	}

	return 0;
}