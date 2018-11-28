#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

#define FORr(i,A,B)	for (int i=(A); i<(B); ++i)
#define FOR(i, N)	FORr(i,0,N)

using namespace std;

int 	get_int()		{int a; 	scanf("%d", &a); 	return a;}
double	get_double()	{double a;	scanf("%lf", &a);	return a;}
char	get_char()		{char c; 	scanf("%c", &c); 	return c;}

char str_buf[100000];
string	get_str()		{scanf("%s", str_buf); return str_buf;}

typedef std::pair<int, int> a_pair;

struct pair_less {
  bool operator()(const a_pair& x, const a_pair& y) const {
    return x.second > y.second;
  }
};

int L;
int t;
int N;
int C;
int a[1010];
bool b[1010];

a_pair c[1010];
std::vector<a_pair> list;

int get_dist(int n)
{
	return a[n%C];
}

int travel(int n, int left_L, int curr_time)
{
	if (n == N) return curr_time;

	// no booster
	int time = travel(n+1, left_L, curr_time + get_dist(n) * 2);

	// use booster
//	if (left_L > 0 && b[n%C])
	if (left_L > 0)
	{
		bool use = b[n%C];

		if (N-n < C)
		{
			int rank = 0;

			for (int nn=n+1; nn<N; ++nn)
			{
				if (get_dist(n) < get_dist(nn)) ++rank;
			}

			if (rank <= left_L) use = true;
		}

		int time_b;
		if (curr_time < t)
		{
//			if (b[n%C])
			if (use)
			{
				int nbt = t - curr_time;

				time_b = travel(n+1, left_L-1, curr_time + nbt + (get_dist(n) - nbt/2));
				time = min(time, time_b);
			}
		}
		else
		{
//			if (b[n%C])
			if (use)
			{
				time_b = travel(n+1, left_L-1, curr_time + get_dist(n));
				time = min(time, time_b);
			}
		}
	}

	return time;
}

void solve()
{
	L = get_int();
	t = get_int();
	N = get_int();
	C = get_int();
	FOR(i, C) a[i] = get_int();

	// calc b
	{
		FOR(i, C)
		{
			c[i].first = i;
			c[i].second = a[i];
			list.push_back(c[i]);
		}

		std::sort(list.begin(), list.end(), pair_less());
//		std::reverse(list.begin(), list.end());

		FOR(i, C)
		{
			b[list.at(i).first] = ((N / C + 1) * i) <= L;
//			printf("%d: %d\n", list.at(i).first, list.at(i).second);
		}
	}

	printf("%d", travel(0, L, 0));
}

int main()
{
	int T = get_int();
	FOR (t, T)
	{
		printf("Case #%d: ", t + 1);
		solve();
		printf("\n");
	}
}
