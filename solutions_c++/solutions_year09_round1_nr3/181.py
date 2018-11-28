#include <iostream>
#include <limits>
#include <string>
#include <vector>

#include <boost/random.hpp>

long double CalcCombo(int x, int y)
{
	long double patterns = 1.0;
	for (int i = 0; i < y; ++i)
	{
		patterns *= (x - i);
		patterns /= i + 1;
	}
	return patterns;
}

double Calculate(int N, int C)
{
	boost::mt19937 gen;
	boost::uniform_int<> dist(0, std::numeric_limits<int>::max());
	boost::variate_generator<boost::mt19937 &, boost::uniform_int<> >
		rand(gen, dist);

	// After the 1st pack.
	std::vector<double> current_rate(C - N + 1, 0.0);
	current_rate[C - N] = 1.0;

	long double all_patterns = CalcCombo(C, N);

	// After the next pack.
	std::vector<std::vector<double> > future_rate(C + 1);
	for (int current = 1; current <= C - N; ++current)
	{
		future_rate[current].resize(C - N + 1, 0.0);

		for (int next = 0; next <= current; ++next)
		{
			if (next < current - N)
				continue;

			future_rate[current][next] = 
				CalcCombo(C - current, N - (current - next))
				* CalcCombo(current, current - next) / all_patterns;
//			std::cerr << current << " -> " << next
//				<< ": " << future_rate[current][next] << std::endl;
		}
	}

	double value = current_rate[0];
	for (int i = 2; i < 1 << 12; ++i)
	{
		std::vector<double> next_rate(C - N + 1, 0.0);
		for (int j = 1; j <= C - N; ++j)
		{
			if (current_rate[j] == 0.0)
				continue;

			for (int k = 0; k <= C - N; ++k)
				next_rate[k] += current_rate[j] * future_rate[j][k];
		}

		value += i * next_rate[0];
		next_rate[0] = 0.0;

		current_rate.swap(next_rate);
	}

	return value;
}

int main()
{
	int num_cases;
	std::cin >> num_cases;

	for (int i = 1; i <= num_cases; ++i)
	{
		int C, N;
		std::cin >> C >> N;

		std::cerr << "Case #" << i << ": " << N << ", " << C << std::endl;
		std::cout << "Case #" << i << ": " << Calculate(N, C) << std::endl;
	}

	return 0;
}
