#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define M 3100

class data_type
{
public:
	int B,E;
	double w;
};

data_type data[M];

int n;
int X;
double S,R,t;

bool cmp(data_type a,data_type b)
{
	return a.w < b.w;
}

void read_data()
{
	cin >> X >> S >> R >> t >> n;
	int i;
	for (i=1;i<=n;i++)
	{
		cin >> data[i].B >> data[i].E >> data[i].w;
		data[i].w += 0;
	}
	int _n = n;
	_n++;
	data[_n].B = 0; data[_n].E = data[1].B; data[_n].w = 0;
	_n++;
	data[_n].B = data[n].E; data[_n].E = X; data[_n].w = 0;
	for (i=1;i<n;i++)
	{
		_n++;
		data[_n].B = data[i].E;  data[_n].E = data[i + 1].B;
		data[_n].w = 0;
	}
	n = _n;
	sort(data + 1,data + n + 1,cmp);
}

double work_ans()
{
	int i;
	double ans = 0;
	double temp;
	for (i=1;i<=n;i++)
	{
		temp = (data[i].E - data[i].B) / (R + data[i].w);
		if (t >= temp)
		{
			t -= temp;
			ans += temp;
		}
		else
		{
			ans += t;
			ans += (data[i].E - data[i].B - (R + data[i].w) * t) / (S + data[i].w);
			t=0;
		}
	}
	return ans;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	int i;
	double ans;
	for (i=1;i<=t;i++)
	{
		read_data();
		ans =work_ans();
		printf("Case #%d: %.10lf\n",i,ans);
	}
	return 0;
}