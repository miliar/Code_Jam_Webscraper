# include <cstdio>
# include <deque>
# include <set>
# include <algorithm>
using namespace std;

int main()
{
	int cases, T, na, nb, i, hours, minu, t1, t2, tt;
//	freopen("D:\\input.txt", "r", stdin);
//	freopen("D:\\output.txt", "w", stdout);
	scanf("%d", &cases);
	tt = 0;
	while (cases--)
	{
		scanf("%d%d%d", &T, &na, &nb);
		deque <pair<int,int> > da, db;
		for (i = 0; i < na; i++)
		{
			scanf("%d:%d", &hours, &minu);
			t1 = hours * 60 + minu;
			scanf("%d:%d", &hours, &minu);
			t2 = hours * 60 + minu;
			da.push_back(pair<int, int>(t1, t2));
		}
		for (i = 0; i < nb; i++)
		{
			scanf("%d:%d", &hours, &minu);
			t1 = hours * 60 + minu;
			scanf("%d:%d", &hours, &minu);
			t2 = hours * 60 + minu;
			db.push_back(pair<int, int>(t1, t2));
		}
		sort(da.begin(), da.end());
		sort(db.begin(), db.end());
		multiset <int> sa, sb;
		int ansa, ansb;
		ansa = ansb = 0;
		while (na || nb)
		{
			if (!nb || (na && da[0] < db[0]))
			{
				if (sa.empty()) ansa++;
				else if (da[0].first < *(sa.begin())) ansa++;
				else sa.erase(sa.begin());
				sb.insert(da[0].second + T);
				da.pop_front();
				na--;
			}
			else {
				if (sb.empty()) ansb++;
				else if (db[0].first < (*sb.begin())) ansb++;
				else sb.erase(sb.begin());
				sa.insert(db[0].second + T);
				db.pop_front();
				nb--;
			}
		}
		printf("Case #%d: %d %d\n", ++tt, ansa, ansb);
	}
	return 0;
}