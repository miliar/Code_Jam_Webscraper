#include <cstdio>
#include <vector>
using namespace std;
int t, idx1, idx2, temp;
pair<int,int> or[200];
pair<int,int> bl[200];
int orange, blue;
char c;
int abs(int x)
{
	if (x<0) return -x;
	return x;
}
int main()
{
	int n = 0;
	int lic=1;
	scanf("%d", &t); getchar();
	while (t--)
	{
		for (int i = 0; i < 200; i++)
			bl[i].first=bl[i].second=or[i].first=or[i].second=2000000000;
		scanf("%d", &n); getchar();
		idx1=idx2=0;
		for (int i = 0; i < n; i++)
		{
			scanf("%c %d", &c, &temp); getchar();
			if (c=='O') or[idx1++]=make_pair(temp, i);
			else bl[idx2++]=make_pair(temp, i);
		}
		orange=1;
		blue=1;
		int ou=0, bu=0;
		int ruchy=0;
		for (int i = 0; i < n; i++)
		{
			if ((or[ou].second<bl[bu].second) && ou<idx1)
			{
				int tury = abs(orange-or[ou].first);
				orange = or[ou].first;
				tury++;
				ruchy+=tury;
				if (blue<=bl[bu].first) blue = min(bl[bu].first, blue+tury);
				else blue = max(bl[bu].first, blue-tury);
				ou++;
			}
			else
			{
				int tury = abs(blue-bl[bu].first);
				blue = bl[bu].first;
				tury++;
				ruchy+=tury;
				if (orange<=or[ou].first) orange = min(or[ou].first, orange+tury);
				else orange = max(or[ou].first, orange-tury);
				bu++;
			}
		}
		printf("Case #%d: %d\n", lic, ruchy);
		lic++;
	}
	return 0;
}
