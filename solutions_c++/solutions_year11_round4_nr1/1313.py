#include<algorithm>
#include<vector>
#include<iostream>

using namespace std;

typedef struct d
{
	double weight;
	double w;
} data;

bool sort_t(data a, data b)
{
	return (a.w < b.w);
}

void cas(int tt)
{
	int i, j;

	int n;
	double x, s, r;
	double t, rem;
	
	cin >> x >> s >> r >> t >> n;

	r -= s;
	rem = t;
	vector<data> v;

	data d;

	double curval = 0.0;
	double a, b, wi;

	for (i = 0; i < n; i++)
	{
		cin >> a >> b >> wi;

		if (curval < a)	{
			d.weight = a - curval;
			d.w = s;
			v.push_back(d);
		}

		d.weight = b - a;
		d.w = wi + s;
		v.push_back(d);
		curval = b;
	}

	if (curval < x) {
		d.weight = x - curval;
		d.w = s;
		v.push_back(d);
	}
	
	sort(v.begin(), v.end(), sort_t);
	
	double ct = 0.0, cit;

	for (i = 0; i < v.size(); i++)
	{
		if (rem > 0.0) {
			if (( cit = v[i].weight/(v[i].w + r)) <= rem )
			{
				ct += cit;
				rem -= cit;
			}
			else
			{
				v[i].weight -= (v[i].w + r) * rem;
				ct += rem;
				rem = 0.0;
				cit = v[i].weight/v[i].w;
				ct += cit;
			}
		} else {
			ct += (v[i].weight/v[i].w);
		}
	}

	printf("Case #%d: %0.10lf\n", tt, ct);

	return;
}

int main()
{
	int t, i;

	cin >> t;
	
	for (i = 1; i <= t; i++)
		cas(i);
	
	return 0;
}
