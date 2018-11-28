#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

const int MAX = 205;

int pos[MAX], man[MAX], D, C;


bool cmp(int a, int b)
{
	return pos[a] < pos[b];
}

bool can(double t)
{
	double left;
	for(int i = 0; i < C; i++)
	{
		double man_len = (man[i] - 1) * D;
		if(man_len > 2 * t)  return false;
		if(i == 0)  left = pos[i] - t + man_len;

		if(i && pos[i] + t - man_len < left + D)  return false;

		if(i)  left = max(left + D, pos[i] - t) + man_len;
	}
	return true;
}

double go()
{
	//sort(man, man + C, cmp);
	//sort(pos, pos + C);

	double low = 0, high = 1e8;
	while(high - low > 1e-8)
	{
		double mid = (low + high) / 2;
		if(can(mid))  high = mid;
		else  low = mid;
	}
	return low;
}

int main()
{
	freopen("d:\\Desktop\\GCJ\\B-small-attempt2.in", "r", stdin);
	freopen("d:\\Desktop\\GCJ\\B-small-attempt2.out", "w", stdout);
	
	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		printf("Case #%d: ", ++c);
		scanf("%d%d", &C, &D);
		for(int i = 0; i < C; i++)
			scanf("%d%d", &pos[i], &man[i]);
		printf("%.8lf\n", go());
	}
}