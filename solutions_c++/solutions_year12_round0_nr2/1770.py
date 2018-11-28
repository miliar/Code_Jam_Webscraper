#include <iostream>
using namespace std;

// suprising scores
const size_t high_suprising_scores[] = {0, 0, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11};

inline size_t max_suprising_score(size_t n)
{
	return high_suprising_scores[n];
}

inline size_t max_not_suprising_score(size_t n)
{
	size_t high_score = n / 3;
	if (n % 3)
		++high_score;
	return high_score;
}

int main()
{
	size_t T = 0;
	cin >> T;

	for (size_t t = 0; t < T; ++t)
	{
		size_t n = 0, s = 0, p = 0;
		cin >> n >> s >> p;

		size_t y = 0;
		for (size_t i = 0; i < n; ++i)
		{
			size_t ti = 0;
			cin >> ti;

			const size_t max_s = max_suprising_score(ti);
			const size_t max_ns = max_not_suprising_score(ti);

			if (max_ns >= p)
				++y;
			else if (s && max_s >= p)
			{
				--s;
				++y;
			}
		}

		cout << "Case #" << t + 1 << ": " << y << endl;
	}

	return 0;
}