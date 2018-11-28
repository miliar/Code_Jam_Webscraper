#include <iostream>
#include <string>
#include <stdio.h>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

void init()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
}

int rotate(int n, int B)
{
	int s = 10;
	vector <int> answers;
	while (n / s > 0)
	{
		int a = n % s;
		int b = n / s;
		int length = 1;
		while (b / 10 > 0)
		{
			b /= 10;
			++length;
		}
		b = n / s;
		while (length > 0)
		{
			a *= 10;
			--length;
		}
		a += b;
		if ((a > n) && (a <= B))
		{
			answers.push_back(a);
		}
		s *= 10;
	}
	sort(answers.begin(), answers.end());
	int ans = 0;
	if ((int) answers.size() > 0)
	{
		ans = 1;
	}
	for (int i = 1; i < (int) answers.size(); ++i)
	{
		if (answers[i] != answers[i - 1])
		{
			++ans;
		}
	}
	return ans;
}

int main()
{
	init();
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
			int A, B;
			cin >> A >> B;
			int ans = 0;
			for (int i = A; i <= B; ++i)
			{
				ans += rotate(i, B);
			}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}
