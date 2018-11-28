#include <fstream>
#include <iostream>
#include <exception>
#include <string>
#include <vector>
#include <set>
#include <utility>
#include <queue>
#include <cmath>

typedef long long ll;
struct Vine {
	ll d, h;
};

void run(std::ifstream &fi, std::ofstream &fo) {
	int n;
	fi >> n;
	std::vector<Vine> v(n+2);
	for (int i=1; i<=n; i++)
		fi >> v[i].d >> v[i].h;
	v[0].d = 0;
	v[0].h = v[1].d;
	fi >> v[n+1].d;
	v[n+1].h = 0;
	typedef std::pair<int,int> State;
	std::set<State> possible;
	std::queue<State> q;
	possible.insert(std::make_pair(0,1));
	q.push(std::make_pair(0,1));
	while (!q.empty()) {
		int prev = q.front().first;
		int curr = q.front().second;
		ll maxDist = std::min(std::abs(v[curr].d - v[prev].d), v[curr].h);
		for (int next = 0; next<=n+1; next++) {
			if (next==curr) continue;
			ll dist = std::abs(v[next].d - v[curr].d);
			if (dist<=maxDist) {
				if (next==n+1) {
					fo << "YES";
					return;
				}
				State newState = std::make_pair(curr, next);
				if (possible.find(newState)==possible.end()) {
					possible.insert(newState);
					q.push(newState);
				}
			}
		}
		q.pop();
	}
	fo << "NO";
}

int main(int argc, const char **argv) {
	try {
		unsigned int T;
		std::string inFilename(argc<=1 ? "in" : argv[1]);
		std::string outFilename = inFilename + ".out";
		std::ifstream fi(inFilename);
		fi.exceptions(std::ios::badbit | std::ios::failbit);
		std::ofstream fo(outFilename);
		fo.exceptions(std::ios::badbit | std::ios::failbit);
		fi >> T;
		for (unsigned int t=1; t<=T; t++) {
			fo << "Case #" << t << ": ";
			run(fi, fo);
			fo << std::endl;
			std::cout << '\r' << t << '/' << T; std::cout.flush();
		}
		std::cout << std::endl;
	} catch (const std::exception &ex) {
		std::cerr << "\nexception: " << ex.what() << std::endl;
	} catch (...) {
		std::cerr << "\nwhoops\n";
	}
	return 0;
}
