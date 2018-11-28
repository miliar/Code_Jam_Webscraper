#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>;

using namespace std;

int T;
double X, S, R, time, N;
double b[1010];
double e[1010];
double w[1010];
vector<double> t1;
vector<double> t2;
double r[4010];
double c[4010];

void input()
{
	t1.clear();
	t2.clear();
	cin >> X >> S >> R >> time >> N;
	for (int i=0; i<N; i++)
	{
		cin >> b[i] >> e[i] >> w[i];
		if (i==0)
		{
			t1.push_back((b[i] - 0) / S);
			t2.push_back((b[i] - 0) / R);
		}
		else
		{
			t1.push_back((b[i] - e[i-1]) / S);
			t2.push_back((b[i] - e[i-1]) / R);
		}
		t1.push_back((e[i] - b[i]) / (w[i] + S));
		t2.push_back((e[i] - b[i]) / (w[i] + R));
		if (i==N-1)
		{
			t1.push_back((X-e[i]) / S);
			t2.push_back((X-e[i]) / R);
		}
	}
}

double solve()
{
	double total = 0;
	for (int i=0; i<t1.size(); i++)
		if (t2[i] != 0)
		{
			r[i] = t1[i] / t2[i];
			c[i] = t2[i];
		}
		else
		{
			r[i] = 0;
			c[i] = 0;
		}
	for (int i=0; i<t1.size(); i++) total += t1[i];
	for (int i=0; i<t1.size(); i++)
		for (int j=i+1; j<t1.size(); j++)
			if (r[j] > r[i])
			{
				double t = r[j]; r[j] = r[i]; r[i] = t;
				t = c[j]; c[j] = c[i]; c[i] = t;
			}
	for (int i=0; i<t1.size(); i++)
		if (time >= c[i])
		{
			total = total + c[i] - c[i] * r[i];
			time -= c[i];
		}
		else if (time > 0)
		{
			total = total + time - time * r[i];
			time = 0;
			break;
		}
	return total;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> T;
	for (int i=1; i<=T; i++)
	{
		input();
		printf("Case #%d: %.9f\n", i, solve());
	}
}