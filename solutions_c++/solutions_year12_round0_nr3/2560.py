#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <set>
using namespace std;

int tens[7];

void fill()
{
	tens[0] = 1;
	for(int i = 1; i < 7; i++)
	{
		tens[i] = tens[i - 1] * 10;
	}
}

int countDigs(int n)
{
	int res = 0;
	if(n == 0) return 1;
	while(n > 0)
	{
		res++;
		n /= 10;
	}
	return res;
}

int main()
{
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	fill();
	int T;
	cin >> T;
	int x, y, newn;
	set< pair<int, int> > s;
	for(int test = 1; test <= T; test++)
	{
		int a, b;
		cin >> a >> b;
		int digs = countDigs(a);
		s.clear();
		for(int i = a; i < b; i++)
		{
			for(int j = 1; j < digs; j++)
			{
				x = i % tens[j];
				y = i / tens[j];
				if(x < tens[j - 1]) continue;

				newn = x * tens[digs - j] + y;
				if(i < newn && newn <= b)
				{
					s.insert(make_pair(i, newn));
				}
			}
		}
		cout << "Case #" << test << ": " << s.size() << endl;
	}
	return 0;
}