#include <iostream>
#include <stdio.h>
#include <math.h>

#define ct (int) 1e3

using namespace std;

struct bin
{
	int value, cnt, norm;
};

bin operator + (bin a, int b)
{
	a.value ^= b;
	a.cnt++;
	a.norm += b;

	return a;
}

int t, n, a[ct], max_;
bool mark[ct];

void perebor (int pos, bin sum1, bin sum2)
{
	if (pos == n)
	{
		if (sum1.value == sum2.value && sum1.value != 0 && sum2.value != 0)	
			max_ = max(max_, max(sum1.norm, sum2.norm));
            
        return;
	}

	perebor(pos + 1, sum1 + a[pos], sum2);
	perebor(pos + 1, sum1, sum2 + a[pos]);

	return;	
}


int main()
{   	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	freopen("log.txt", "w", stderr);
    	 
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cin >> n;

		for (int j = 0; j < n; j++)
			mark[j] = false;
		max_ = -1;
					
		for (int j = 0; j < n; j++)
			cin >> a[j];

		bin c, d;
		c.value = d.value = c.cnt = d.cnt = c.norm = d.norm = 0;

		perebor(0, c, d);

		cout << "Case #" << i + 1 << ": ";
		if (max_ == -1)
			cout << "NO" << endl;
		else
			cout << max_ << endl;
	}

   
	return 0;
}