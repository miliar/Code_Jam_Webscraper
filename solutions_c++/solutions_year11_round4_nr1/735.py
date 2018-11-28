#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>

struct data {
	data(int s, int l) : speed(s), length(l) {};
	int speed;
	int length;
};

bool cmp(const data& a, const data& b)
{
	return (a.speed < b.speed);
}
void solve(int q_no)
{
	std::cout << "Case #" << q_no << ": ";
	std::vector<data> d;

	int len;
	int s1;
	int s2;
	double t2;
	int c;
	
	std::cin >> len >> s1 >> s2 >> t2 >> c;
	int start =0;
	for(int i =0; i < c;++i)
	{
		int b, e, s;
		std::cin >> b>> e >>s;
		if(start < b)
		{
			d.push_back(data(s1, b - start));
		}
		d.push_back(data(s1 + s, e-b));
		start = e;
	}
	if(start < len)
	{
		d.push_back(data(s1, len - start));
	}

	bool can_run = true;
	std::sort(d.begin(), d.end(), cmp);
	double total = 0;
	for(int i =0; i < d.size();++i)
	{
		if(can_run)
		{
			double t = double(d[i].length) / double(d[i].speed - s1 + s2);
			if(t > t2)
			{
				can_run = false;
				t = t2 + (double(d[i].length) - t2 * double(d[i].speed - s1 + s2)) / double(d[i].speed);
				t2=0;
			}
			else
			{
				t2 -= t;
			}
			total +=t;
		}
		else 
		{
			total += double(d[i].length)/ double(d[i].speed);
		}
	}
	printf("%.7f\n", total);
}

int main(void)
{
	int count;
	std::cin >> count;
	for(int i =0; i < count;++i)
	{
		solve(i+1);
	}
	return 0;
}
