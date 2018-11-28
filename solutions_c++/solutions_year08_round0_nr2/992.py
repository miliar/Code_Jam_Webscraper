
#include <iostream>
using namespace std;

struct train
{
	int departure;
	int ready;
	bool seen;
};

train a2b[200];
train b2a[200];

int ind_a, ind_b;
int turnaround;
int na, nb;

bool cmp_train(const train & a, const train & b)
{
	if (a.seen != b.seen)
		return b.seen;

	return a.departure < b.departure;
}

void add_train(char src, int index)
{
	switch (src)
	{
		case 'a':
//			printf("stop A, leaving at %d:%d, arriving at %d:%d\n", a2b[index].departure/60, a2b[index].departure%60, a2b[index].ready/60, a2b[index].ready%60);
			a2b[index].seen = true;
			for (int i = ind_b; i < nb; i++)
				if (!b2a[i].seen && a2b[index].ready <= b2a[i].departure)
				{
					add_train('b', i);
					break;
				}
			break;
		case 'b':
	//		printf("stop B, leaving at %d:%d, arriving at %d:%d\n", b2a[index].departure/60, b2a[index].departure%60, b2a[index].ready/60, b2a[index].ready%60);
			b2a[index].seen = true;
			for (int i = ind_a; i < na; i++)
				if (!a2b[i].seen && b2a[index].ready <= a2b[i].departure)
				{
					add_train('a', i);
					break;
				}
			break;
	}
}

pair<int, int> calc()
{
	int a = 0, b = 0;
	while (ind_a < na && ind_b < nb)
	{
//		printf("next train:\n");
		if (cmp_train(a2b[ind_a], b2a[ind_b]))
			add_train('a', ind_a), a++;
		else
			add_train('b', ind_b), b++;

		/* increment the index till the next unseen scheduled trip */
		while (ind_a < na && a2b[ind_a].seen) ind_a++;
		while (ind_b < na && b2a[ind_b].seen) ind_b++;
	}

	while (ind_a < na)
	{
		if (!a2b[ind_a].seen)
			add_train('a', ind_a), a++;

		ind_a++;
	}

	while (ind_b < nb)
	{
		if (!b2a[ind_b].seen)
			add_train('b', ind_b), b++;
		ind_b++;
	}

	return make_pair(a, b);
}

void solve(int testcase)
{
	cin >> turnaround >> na >> nb;
	ind_a = ind_b = 0;

	for (int i = 0; i < na; i++)
	{
		int a, b, c, d;
		scanf("%d:%d %d:%d", &a, &b, &c, &d);
		a2b[i].departure = a*60+b;
		a2b[i].ready = c*60+d+turnaround;
		a2b[i].seen = false;
	}

	for (int i = 0; i < nb; i++)
	{
		int a, b, c, d;
		scanf("%d:%d %d:%d", &a, &b, &c, &d);
		b2a[i].departure = a*60+b;
		b2a[i].ready = c*60+d+turnaround;
		b2a[i].seen = false;
	}

	sort(a2b, a2b+na, cmp_train);
	sort(b2a, b2a+nb, cmp_train);

	pair<int, int> r = calc();

	printf("Case #%d: %d %d\n", testcase, r.first, r.second);
}

int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		solve(i);
	
	return 0;
}
