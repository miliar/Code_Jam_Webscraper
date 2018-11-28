#include <iostream>
#include <string>

using namespace std;

int pos[100];

int main ()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t; 
	cin >> t;
	string tmp;
	char c;
	int score;
	for (int o = 0; o < t; o++)
	{
		int res = 0, i, j;
		for (i = 0; i < 100; i++)
			pos[i] = 0;
		int n, s, p;
		cin >> n >> s >> p;
		for (int p0 = p; p0 <= 10; p0++)
		{
			for (i = max(p0-1, 0); i <= min(p0+1, 10); i++)
				for (int j = max(p0-1, 0); j <= min(p0+1, 10); j++)
					if (abs(i - j) <= 1)
						pos[p0 + i + j] = 1;
			for (i = max(p0-2, 0); i <= min(p0+2, 10); i++)
				for (int j = max(p0-2, 0); j <= min(p0+2, 10); j++)
					if (abs(i - j) <= 2 && pos[p0 + i + j] == 0)
						pos[p0 + i + j] = 2;
		}
		/*for (i = 0; i < 30; i++)
			cout << pos[i] <<" ";
		cout << endl;*/
		for (i = 0; i < n; i++)
		{
			cin >> score;
			if (pos[score] == 1)
				res++;
			if (pos[score] == 2 && s > 0)
			{
				res++;
				s--;
			}
		}
		cout << "Case #" << o+1 << ": ";
		cout << res;
		cout << endl; 
	}
	return 0;
}