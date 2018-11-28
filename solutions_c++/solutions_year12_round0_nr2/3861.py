#include <iostream>
#include <string>

using namespace std;

void doit(const int t)
{
	int n, s, p, ans(0);
	cin >> n >> s >> p;
	for (int i = 0; i != n; ++i)
	{
		int score, tmp;
		cin >> score;
		tmp = p - 1 > 0 ? p - 1 : 0;
		if (p + tmp + tmp <= score)
		{
			++ans;
		}
		else 
		{
			tmp = p - 2 > 0 ? p - 2 : 0;
			if ((s > 0) && (p + tmp + tmp <= score))
			{
				++ans;
				--s;
			}
		}
	}
	cout << "Case #" << t << ": " << ans << endl;
}


int main()
{
	int t;
	cin >> t;
	for (int i = 0; i != t; ++i)
		doit(i + 1);
	return 0;
}
