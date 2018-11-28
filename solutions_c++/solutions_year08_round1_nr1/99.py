#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long int64;

int		nCase, N;
vector<int>	x_pos, x_neg, y_pos, y_neg;

int	main()
{
	scanf("%d", &nCase);
	for (int nowCase = 1; nowCase <= nCase; ++nowCase)
	{
		scanf("%d", &N);

		int x_value, y_value;

		x_pos.clear(); y_pos.clear();
		x_neg.clear(); y_neg.clear();

		for (int i = 0; i < N; ++i) 
		{
			scanf("%d", &x_value);
			if (x_value > 0) 
				x_pos.push_back(x_value); 
			else 
				x_neg.push_back(- x_value);
		}

		for (int i = 0; i < N; ++i) 
		{
			scanf("%d", &y_value);
			if (y_value > 0) 
				y_pos.push_back(y_value); 
			else
				y_neg.push_back(- y_value);
		}

		sort(x_pos.begin(), x_pos.end());
		sort(y_pos.begin(), y_pos.end());
		sort(x_neg.begin(), x_neg.end());
		sort(y_neg.begin(), y_neg.end());

		int64 answer = 0;
		for (int i = 0; i < min(x_pos.size(), y_neg.size()); ++i)
			answer -= int64( x_pos[x_pos.size() - i - 1] ) * y_neg[y_neg.size() - i - 1];

		for (int i = 0; i < min(x_neg.size(), y_pos.size()); ++i)
			answer -= int64( x_neg[x_neg.size() - i - 1] ) * y_pos[y_pos.size() - i - 1];

		int M = x_pos.size() - y_neg.size();
		if (M < 0) M = -M;
		if (x_pos.size() > y_neg.size())
			for (int i = 0; i < M; ++i) answer += int64( x_pos[i] ) * y_pos[M - i - 1];
		else
			for (int i = 0; i < M; ++i) answer += int64( x_neg[i] ) * y_neg[M - i - 1];
		cout << "Case #" << nowCase << ": " << answer << endl;
	}
	return 0;
}
