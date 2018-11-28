#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

int o[200], b[200], o_h, o_t, b_h, b_t, o_p[200], b_p[200], o_c, b_c, time;

int solve()
{
	o_h = o_t = b_h = b_t = time = 0;
	o_c = b_c = 1;
	int n;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		char A;
		int B;
		cin >> A >> B;
		if (A == 'O')
		{
			o[o_t] = B;
			o_p[o_t++] = i;
		} else {
			b[b_t] = B;
			b_p[b_t++] = i;
		}
	}
	while (o_h < o_t || b_h < b_t)
	{
		bool us = false;
		if (o_h >= o_t || b_h >= b_t)
		{
			if (o_h >= o_t)
			{
				if (b_c == b[b_h])
					b_h++;
				else
				{
					if (b_c > b[b_h])
						b_c--;
					else
						b_c++;
				}
			} else {
				if (o_c == o[o_h])
					o_h++;
				else 
				{
					if (o_c > o[o_h])
						o_c--;
					else
						o_c++;
				}
			}
			time++;
			continue;
		}
		if (o_c == o[o_h])
		{
			if (o_p[o_h] < b_p[b_h])
			{
				o_h++;
				us = true;
			}
		} else {
			if (o_c > o[o_h])
				o_c--;
			else
				o_c++;
		}
		if (b_c == b[b_h])
		{
			if (b_p[b_h] < o_p[o_h] && !us)
				b_h++;
		} else {
			if (b_c > b[b_h])
				b_c--;
			else
				b_c++;
		}
		time++;
	}
	return time;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
		cout << "Case #" << i << ": " << solve() << endl;
	return 0;
}