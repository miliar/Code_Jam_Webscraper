#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

struct data
{
	double dis;
	double w;
};

bool compare(data a, data b)
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
	double cur = 0.0;
	double a, b, wi;
	for (i = 0; i < n; i++)
	{
		cin >> a >> b >> wi;
		if (cur < a)
		{
			d.dis = a - cur;
			d.w = s;
			v.push_back(d);
		}
		d.dis = b - a;
		d.w = wi + s;
		v.push_back(d);
		cur = b;
	}
	if (cur < x)
	{
		d.dis = x - cur;
		d.w = s;
		v.push_back(d);
	}
	
	sort(v.begin(), v.end(), compare);
	
	double ct = 0.0, cit;
	for (i = 0; i < v.size(); i++)
	{
	//	cout << v[i].dis << endl;
		if (rem > 0.0)
		{
			if (( cit = v[i].dis/(v[i].w + r)) <= rem )
			{
				ct += cit;
				rem -= cit;
			}
			else
			{
				v[i].dis -= (v[i].w + r) * rem;
				ct += rem;
				rem = 0.0;
				cit = v[i].dis/v[i].w;
				ct += cit;
			}
		}
		else
		{
			ct += (v[i].dis/v[i].w);
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
	{
		cas(i);
	}
	return 0;
}
