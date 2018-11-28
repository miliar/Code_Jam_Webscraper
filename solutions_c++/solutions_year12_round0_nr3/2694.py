#include <iostream>
#include <stdio.h>
#include <map>

using namespace std;

int pow10(int c)
{
	int res = 1;
	for (int i = 0; i < c; i++)
		res *= 10;
	return res;
}
int digitcount(int n)
{
	int c = 0;
	while(n > 0)
	{
		c++;
		n /=  10;
	}
	return c;
}
int process(int start, int end)
{
	if(start == end || end < 10) return 0;

	int count = 0;
	map<int, int> testmap;
	for(int c = start; c < end; c++)
	{
		int dc = digitcount(c);
		for(int i = 1; i <= dc -1; i++)
		{
			int t = (c % pow10(i)) * pow10(dc - i);
			t += (c / pow10(i));
			if(t > c && digitcount(t) == digitcount(c) && t <= end) 
			{
				if(testmap[c] == t || testmap[t] == c)
					continue;
				count++;
				// cout << c << "," << t << endl;
				testmap[c] = t; testmap[t] = c;
			}
		}
	}
	return count;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int i = 0; i < cases; i++)
	{
		int start, end;
		scanf("%d %d", &start, &end);
		cout << "Case #" << i+1 << ": " << process(start, end) << endl;
	}

}
