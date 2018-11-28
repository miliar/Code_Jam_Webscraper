#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
using namespace std;

int main()
{
	map <string, char> gabung, buang;
	int i, j, k, c, d, T, sz, len, pos;
	bool cek, hilang;
	string st1, st2, dum;
	vector <char> vec;
	char dummy, ch1, ch2, ch3;
	char st[105];
//	freopen("2-2.in", "r", stdin);
//	freopen("2-2.out", "w", stdout);
	scanf("%d", &T);
	for (i = 1; i <= T; ++i)
	{
		gabung.clear();
		buang.clear();
		vec.clear();
		scanf("%d", &c);
		for (j = 0; j < c; ++j)
		{
			scanf("%c", &dummy);
			scanf("%c%c%c", &ch1, &ch2, &ch3);
			st1 = ch1;
			st2 = ch2;
			st1 = st1 + ch2;
			st2 = st2 + ch1;
			gabung[st1] = ch3;
			gabung[st2] = ch3;
		}
		scanf("%d", &d);
		for (j = 0; j < d; ++j)
		{
			scanf("%c", &dummy);
			scanf("%c%c", &ch1, &ch2);
			st1 = ch1;
			st2 = ch2;
			st1 = st1 + ch2;
			st2 = st2 + ch1;
			buang[st1] = 1;
			buang[st2] = 1;
		}
		scanf("%d", &len);
		scanf("%c", &dummy);
		gets(st);
		if (len > 1)
		{
			dum = st[0];
			dum = dum + st[1];
			if (gabung.count(dum) != 0)
			{
				pos = 2;
				vec.push_back(gabung[dum]);
			}
			else
			{
				pos = 1;
				vec.push_back(st[0]);
			}
			for (j = pos; j < len; ++j)
			{
				sz = vec.size();
				cek = true;
				if (sz == 0)
					vec.push_back(st[j]);
				else
				{
					dum = vec[sz-1];
					dum = dum + st[j];
					if (gabung.count(dum) != 0)
					{
						vec[sz-1] = gabung[dum];
						cek = false;
					}
					else
						vec.push_back(st[j]);
				}
				if (cek && (sz != 0))
				{
					dum = vec[sz];
					dum = "0" + dum;
					hilang = false;
					for (k = 0; k < sz; ++k)
					{
						dum[0] = vec[k];
						if (buang.count(dum) != 0)
							vec.clear();
					}
				}
			}
			printf("Case #%d: [", i);
			sz = vec.size();
			for (j = 0; j < sz; ++j)
			{
				if (j != 0)
					printf(", ");
				printf("%c", vec[j]);
			}
			printf("]\n");
		}
		else
			printf("Case #%d: [%c]\n", i, st[0]);
	}
//	fclose(stdin); fclose(stdout);
	return 0;
}
