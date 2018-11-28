#include <stdio.h>
#include <vector>
#include <algorithm>

using std::vector;

__int64 gcd(__int64 a,__int64 b)
{
	if(a < b) return gcd(b,a);
	if(0 == b) return a;
	if(1 == b) return 1;
	return gcd(b,a%b);
}

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int n = 0;__int64 l = 0,h = 0;
		scanf("%d%I64d%I64d",&n,&l,&h);
		vector<__int64> freqs(n);
		for(int i = 0;i < n;++i) scanf("%I64d",&freqs[i]);
		std::sort(freqs.begin(),freqs.end());

		__int64 ret = 0;
		for(int i = 0;i <= n;++i)
		{
			__int64 lcd = freqs[0],maxd = freqs[n-1];
			bool overhigh = false;
			for(int k = 0;k < i;++k) 
			{
				__int64 d = gcd(lcd,freqs[k]);
				__int64 t = lcd/d;
				if(freqs[k] > h/t) { overhigh = true;break; }
				lcd = freqs[k]*t;
			}
			if(overhigh) break;
			if(0 == i) lcd = 0;
			for(int k = i;k < n;++k) maxd = gcd(maxd,freqs[k]);
			if(i == n) maxd = 0;
			// maxd的约数,最小公倍数的倍数

			//printf("gcd = %I64d,lcd = %I64d\n",maxd,lcd);

			if(0 != maxd && maxd < l) continue;
			if(0 != lcd && lcd > h) break;
			if(0 != ret && lcd > ret) break;
			if(0 != lcd && maxd%lcd) continue;

			if(0 == maxd)
			{
				// lcd的倍数
				__int64 mint = l/lcd;
				__int64 maxt = h/lcd;
				if(l%lcd) ++mint;
				if(mint <= maxt)
				{
					__int64 t = mint*lcd;
					if(0==ret||t<ret) ret = t;
				}
			}
			else
			{
				__int64 x = 0;
				for(__int64 t = 1;t*t <= maxd;++t)
				{
					if(maxd%t) continue;
					if(t >= l && t <= h)
					{
						if((0==lcd||0==t%lcd))
						{
							if(0==x||t<x) x = t;
						}
					}
					__int64 s = maxd/t;
					if(s >= l && s <= h)
					{
						if((0==lcd||0==s%lcd))
						{
							if(0==x||s<x) x = s;
						}
					}
				}
				if(0==ret||x<ret) ret = x;
			}
			//printf("index = %d,ret = %I64d\n",i,ret);
		}

		if(ret == 0) printf("Case #%d: NO\n",iCases);
		else printf("Case #%d: %I64d\n",iCases,ret);
	}
	return 0;
}