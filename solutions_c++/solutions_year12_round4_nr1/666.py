#include <iostream>
#include <vector>
#include <set>

int N;
std::vector<int> dist;
std::vector<int> len;
std::set<std::pair<int, int> > done;
int goal;
int min(int a, int b)
{
	return (a<b) ? a : b;
}
bool solve(int start, int range)
{
	if (done.find(std::pair<int, int>(start, range)) != done.end()) {
		return false;
	}

	// reach the end ?
	if (dist[start] + range >= goal) {
		return true;
	}
	
	for (int i = start+1; i < N; i++) {
		if (dist[i] > dist[start] + range) {
			break;
		}
		
		if (solve(i, min(dist[i] - dist[start], len[i]))) {
			return true;
		}
	}
	
	done.insert(std::pair<int, int>(start, range));
	return false;
}

int main(int argc, char* argv[])
{
	int T;
	std::cin >> T;
	
	for (int t = 0; t < T; t++) {
		
		std::cin >> N;
		dist.resize(N);
		len.resize(N);
		for (int n = 0; n < N; n++) {
			std::cin >> dist[n];
			std::cin >> len[n];
		}
		std::cin >> goal;

		done.clear();
		bool res = solve(0, dist[0]);
		
		
		std::cout << "Case #" << (t+1) << ": " << (res == true ? "YES" : "NO") << std::endl;
	}
}
