#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

double mytime[1000010];
double profit[1000010];
long long ar[1000010];
long long br[1000010];

long long cas()
{
	long long i, j;
	//double t;
	long long l, n, c, t;
	cin >> l >> t >> n >> c;
	for (i = 0; i < c; i++)
	{
		cin >> br[i];
	}
	double temp = 0;
	mytime[0] = 0;
	for (i = 0; i < n; i++)
	{
		ar[i] = br[i%c];
		mytime[i+1] = temp + 2*ar[i];
		temp = mytime[i+1];
		if (mytime[i+1] > t) 
		{
			if (mytime[i] > t) profit[i] = (mytime[i+1] - mytime[i]) / 2;
			else profit[i] = (mytime[i+1] - t)/2;
		}
		else profit[i] = 0.0;
	}
	sort(profit, profit + n);
	double tot_profit = 0.0;
	for (i = n-1, j = 0; j < l; i--, j++) tot_profit += profit[i];
	return mytime[n] - tot_profit;
}

int main()
{
	long long t;
	cin >> t;
	long long i;
	for (i = 1; i <= t; i++)
	{
		printf("Case #%lld: %lld\n", i, cas());
	}
	return 0;
}
