#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

int testNum = 0;
double result;
double X,S,R,t, tbackup;
long long N;

struct walk
{
	int B;
	int E;
	int w;
};

bool operator<(walk w1, walk w2)
{
	return w1.w < w2.w;
}
walk w[1000000];

void read()
{
	int i;
	cin >> X >> S >> R >> t >> N;
	for (i = 1; i <= N; ++i)
		cin >> w[i].B >> w[i].E >> w[i].w;
}
void printOut()
{
	cout << "Case #" << testNum << ": ";
	cout << fixed << setprecision(15) << result << "\n";
}

void getAns1()
{
	tbackup = t;
	sort(w + 1, w + 1 + N);
	result = 0;
	// demic tsaker@!
	double sum = 0;
	int i;
	for (i = 1; i <= N; ++i)
		sum += w[i].E - w[i].B;
	if (X - sum < R * t)
	{
		result += (X - sum) / R;
		t -= result; // vazeci sagh tsaker@!
	}
	else
	{
		result += t + (X - sum - t * R) / S;
		t = 0.0; // vazeci inchqan karaca, mnacats@ qayleci
	}

	for (i = 1; i <= N; ++i)
	{
		if ((w[i].E - w[i].B) / (R + w[i].w) < t)
		{
			result += (w[i].E - w[i].B) / (R + w[i].w);
			t -= (w[i].E - w[i].B) / (R + w[i].w); // sagh vazeci
		}
		else
		{
			result += t + (w[i].E - w[i].B - (R + w[i].w) * t) / (S + w[i].w);
			t = 0.0;
		}
	}
	t = tbackup;
}



bool canBeDone(double AVGS)
{
	if (AVGS < S)
		return true;
	double Tneed = 0.0;
	double sum = 0, dist, v1;
	int i;
	for (i = 1; i <= N; ++i)
		sum += w[i].E - w[i].B;
	dist = X - sum;
	v1 = S;
	Tneed += (dist - dist * v1 / AVGS) / (R - S);
	if ((dist - dist * v1 / AVGS) / (R - S) > dist / (v1 + R - S))
		return false;
	for (i = 1; i <= N; ++i)
	{
		dist = w[i].E - w[i].B;
		v1 = w[i].w + S;
		if (v1 > AVGS)
			return Tneed < t;
		if ((dist - dist * v1 / AVGS) / (R - S) > dist / (v1 + R - S))
			return false;
		Tneed += (dist - dist * v1 / AVGS) / (R - S);
	}
return Tneed < t;
}


double getTime(double AVGS)
{
	double res = 0.0;
	double Tneed = 0.0;
	double sum = 0, dist, v1;
	int i;
	for (i = 1; i <= N; ++i)
		sum += w[i].E - w[i].B;
	dist = X - sum;
	v1 = S;
	Tneed = (dist - dist * v1 / AVGS) / (R - S);
	res += Tneed + (dist - Tneed * (R - S + v1)) / v1;
	for (i = 1; i <= N; ++i)
	{
		dist = w[i].E - w[i].B;
		v1 = w[i].w + S;
		if (v1 > AVGS)
		{
			res += dist / v1;
		}	
		else
		{
			Tneed = (dist - dist * v1 / AVGS) / (R - S);
			res += Tneed + (dist - Tneed * (R - S + v1)) / v1;
		}
	}
return res;
}

void getAns2()
{
	sort(w + 1, w + 1 + N);
	double st, end;
	st = S;
	end = 300;
	while (end - st > 0.000000001)
	{
		if (canBeDone((end + st) / 2))
			st = (end + st) / 2;
		else
			end = (end + st) / 2;
	}
	result = getTime(end);
}

void solve()
{
	read();
	getAns1();
	double result1 = result;
	getAns2();
	if (result < result1)
	{
		cerr << "this is better\n";
		cerr << result << " " << result1 << "\n";
	}
	else
		result = result1;
	printOut();
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	while(t)
	{
		cerr << testNum << "\n";
		++testNum;
		solve();
		--t;
	}
return 0;
}