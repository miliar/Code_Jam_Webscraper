#include <iostream>

using namespace std;

bool can_make_it(int,int);
bool can_surprise(int,int);

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t ; i++)
	{
		int n, s, p, cnt = 0, surc = 0;
		cin >> n >> s >> p;
		for(int j = 0; j < n; j++)
		{
			int tmp;
			cin >> tmp;
			if(can_make_it(tmp,p))
				cnt++;
			else if(can_surprise(tmp,p) && surc < s)
				surc++;
		}
		cout << "Case #" << i << ": " << cnt+surc << endl;
	}
	return 0;
}

bool can_make_it(int score, int p)
{
	return score > 3*(p-1);
}

bool can_surprise(int score, int p)
{
	if(p == 1) return score > 0;
	return score >= p+(p-2)+(p-2);
}