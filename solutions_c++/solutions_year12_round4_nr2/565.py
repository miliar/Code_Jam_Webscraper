#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

int W, L;
std::vector<std::pair<double, int> > v;
std::vector<std::pair<double, double> > positions;

double yoyo(int max)
{
	double d = ((double)rand() / (double)RAND_MAX) * max;
	return d;
}

void place(int i)
{
	positions[i].first = yoyo(W);
	positions[i].second = yoyo(L);
}

bool check(int until)
{
	int U = v[until].second;
	for (int i = 0; i < until; i++) {
		int V = v[i].second;
		double dist = sqrt(pow(positions[U].second - positions[V].second, 2) + pow(positions[U].first - positions[V].first, 2));
		if (dist < v[i].first + v[until].first) {
			return false;
		}
	}

	return true;
}

int main(int argc, char* argv[])
{
	srand(time(NULL));
	int T;
	std::cin >> T;
	
	for (int t = 0; t < T; t++) {
		int N;
		std::cin >> N >> W >> L;
		
		
		v.resize(N);
		positions.resize(N);
		for (int n = 0; n < N; n++) {
			v[n].second = n;
			std::cin >> v[n].first;
		}
		std::greater<std::pair<double, int> > C;
		std::sort(v.begin(), v.end(), C);
		
		for (int n = 0; n < N; n++) {
			do {
				place(v[n].second);
			} while (false == check(n));
		}
		
		std::cout << "Case #" << (t+1) << ": ";
		for (int n = 0; n < N; n++) {
			std::cout << positions[n].first << " " << positions[n].second << " ";
		}
		std::cout << std::endl;
	}

	return 0;
}
