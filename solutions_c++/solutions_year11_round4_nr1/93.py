#include <cstdio>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

int total_len;
int walk;
int run;
int run_time;
int N;

struct accel_s
{
	int st;
	int ed;
	int speed;

	inline bool friend operator < (const accel_s &p, const accel_s &q)
	{
		return p.st < q.st;
	}
};

vector<accel_s> accel;
map<int, int> segment;

int main()
{
	int t;
	scanf("%d", &t);
	for (int ti = 1;ti <= t;ti++)
	{
		fprintf(stderr, "Case %d\n", ti);
		scanf("%d %d %d %d %d", &total_len, &walk, &run, &run_time, &N);
		accel.clear();
		for (int i = 0;i < N;i++)
		{
			accel_s x;
			scanf("%d %d %d", &x.st, &x.ed, &x.speed);
			accel.push_back(x);
		}

		sort(accel.begin(), accel.end());
		segment.clear();

		int last_x = 0;
		for (int i = 0;i < N;i++)
		{
			accel_s &cur = accel[i];

			int st_diff = cur.st - last_x;
			segment[0] += cur.st - last_x;
			segment[cur.speed] += cur.ed - cur.st;
			last_x = cur.ed;
		}

		segment[0] += total_len - last_x;

		double ans = 0;
		double run_left = run_time;
		map<int, int>::iterator it;
		for (it = segment.begin();it != segment.end();it++)
		{
			int speed = it->first;
			int len = it->second;
			double run_req_time = len / (double)(speed + run);

			double real_run_time = min(run_req_time, run_left);
			run_left -= real_run_time;
			double real_run_dist = real_run_time * (speed + run);
			ans += real_run_time;
			ans += (len - real_run_dist) / (speed + walk);
		}

		printf("Case #%d: %.10f\n", ti, ans);
	}
	return 0;
}
