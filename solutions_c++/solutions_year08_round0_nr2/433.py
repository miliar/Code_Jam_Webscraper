#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

#define FOR(i, n) for(int i = 0; i < n; i++)

struct Timetable
{
	int time1;
	int time2;
	bool AB;
};

bool operator < (const Timetable &t1, const Timetable &t2)
{
	if(t1.time1 < t2.time1)
		return true;
	if(t1.time1 > t2.time1)
		return false;
	return t1.time2 < t2.time2;
}

vector <Timetable> arr;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, t, na, nb, a, b, c, d;
	scanf("%d", &n);
	FOR(i, n)
	{
		scanf("%d", &t);
		scanf("%d%d", &na, &nb);
		Timetable x;
		arr.clear();
		FOR(j, na)
		{
			scanf("%d:%d %d:%d", &a,&b,&c,&d);
			x.AB = true;
			x.time1 = a * 100 + b;
			x.time2 = c * 100 + d;
			arr.push_back(x);
		}
		FOR(j, nb)
		{
			scanf("%d:%d %d:%d", &a,&b,&c,&d);
			x.AB = false;
			x.time1 = a * 100 + b;
			x.time2 = c * 100 + d;
			arr.push_back(x);
		}
		sort(arr.begin(), arr.end());
		int v1[3000];
		int v2[3000];
		memset(v1, 0, sizeof(v1));
		memset(v2, 0, sizeof(v2));
		int ans1 = 0;
		int ans2 = 0;
		FOR(j, arr.size())
		{
			bool flag = false;
			if(arr[j].AB)
			{
				FOR(k, arr[j].time1 + 1)
					if(v1[k] > 0)
					{
						v1[k]--;
						int tt = arr[j].time2 + t;
						if(tt % 100 >= 60)
							tt += 40;
						v2[tt]++;
						flag = true;
						break;
					}
				if(flag == false)
				{
					ans1++;
					int tt = arr[j].time2 + t;
					if(tt % 100 >= 60)
						tt += 40;
					v2[tt]++;
				}
			}
			else
			{
				FOR(k, arr[j].time1 + 1)
					if(v2[k] > 0)
					{
						v2[k]--;
						int tt = arr[j].time2 + t;
						if(tt % 100 >= 60)
							tt += 40;
						v1[tt]++;
						flag = true;
						break;
					}
				if(flag == false)
				{
					ans2++;
					int tt = arr[j].time2 + t;
					if(tt % 100 >= 60)
						tt += 40;
					v1[tt]++;
				}
			}
		}
		printf("Case #%d: %d %d\n", i+1, ans1, ans2);
	}
	return 0;
}