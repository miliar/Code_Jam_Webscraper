#include <iostream>
#include <string>
#include <fstream>
#include <queue>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int ns[1010];
int val[1010];
int next[1010];
int r, k, n;

int main()
{
	int T;
	long long money;
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		memset(val, -1, sizeof(val));
		memset(next, -1, sizeof(next));
		in >> r >> k >> n;
		for (int i = 0; i < n ; i++)
			in >> ns[i];
		money = 0;
		int s, ddd, d;
		for (int i = 0; i < n; i++)
		{
			s = i;
			ddd = 0;
			d = 0;
			while(d < k && ddd < n)
			{
				if (d + ns[s] > k)
					break;
				d += ns[s];
				s++;
				s %= n;
				ddd++;
			}
			val[i] = d;
			next[i] = s;
		}
		int beg = 0;
		for (int i = 0; i < r; i++)
		{
			money += val[beg];
			beg = next[beg];
		}
		out << "Case #" << t << ": " << money << endl;
	}
	return 0;
}