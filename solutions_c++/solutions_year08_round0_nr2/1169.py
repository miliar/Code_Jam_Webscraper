#include <stdio.h>
#include <algorithm>

using namespace std;

const int maxNA = 100;
const int maxNB = 100;

int main()
{
	int n;
	scanf("%d", &n);
	for(int _case=1; _case<=n; ++_case)
	{
		int t, na, nb;
		scanf("%d %d %d", &t, &na, &nb);
		pair<int, int> a[maxNA+1], b[maxNB+1];
		for(int i=0; i<na; ++i)
		{
			int m1, s1, m2, s2;
			scanf("%d:%d %d:%d", &m1, &s1, &m2, &s2);
			a[i]=make_pair(m1*60+s1, m2*60+s2);
		}
		for(int i=0; i<nb; ++i)
		{
			int m1, s1, m2, s2;
			scanf("%d:%d %d:%d", &m1, &s1, &m2, &s2);
			b[i]=make_pair(m1*60+s1, m2*60+s2);
		}
		sort(a, a+na);
		sort(b, b+nb);
		int pa=0, pb=0, ka=0, kb=0, resa=0, resb=0;
		bool fla[maxNA+1], flb[maxNB+1];
		memset(fla, false, sizeof(fla));
		memset(flb, false, sizeof(flb));
		while (ka<na || kb<nb)
		{
			if (ka>=na) { resb+=nb-kb; break; }
			if (kb>=nb) { resa+=na-ka; break; }
			int time;
			bool fl;
			if (a[pa]<b[pb])
			{
				++ka, ++resa, fla[pa]=true;
				time=a[pa].second+t;
				fl=false;
			}
			else
			{
				++kb, ++resb, flb[pb]=true;
				time=b[pb].second+t;
				fl=true;
			}
			while (1)
			{
				if (!fl)
				{
					for(int i=0; i<nb; ++i)
						if (!flb[i] && b[i].first>=time)
						{
							flb[i]=true; ++kb; time=b[i].second+t;
							fl=true; break;
						}
					if (!fl) break;
				}
				else
				{
					for(int i=0; i<na; ++i)
						if (!fla[i] && a[i].first>=time)
						{
							fla[i]=true; ++ka; time=a[i].second+t;
							fl=false; break;
						}
					if (fl) break;
				}
			}
			for(int i=0; i<na; ++i)
				if (!fla[i]) { pa=i; break; }
			for(int i=0; i<nb; ++i)
				if (!flb[i]) { pb=i; break; }
		}
		printf("Case #%d: %d %d\n", _case, resa, resb);
	}
}