#include <fstream>
#include <iostream>
#include <exception>
#include <string>
#include <memory>
#include <concrt.h>
#include <ppl.h>
#include <algorithm>
#include <random>

typedef long long ll;

struct TestInput {
	ll W, H;
	std::vector<ll> r;
};

struct Position {
	bool good;
	ll x, y, r;
};

struct TestOutput {
	ll scale;
	std::vector<Position> pos;
};

std::istream &operator>>(std::istream &fi, TestInput &in) {
	int n;
	fi >> n >> in.W >> in.H;
	in.r.resize(n);
	for (int i=0; i<n; i++)
		fi >> in.r[i];
	return fi;
}

inline void print(std::ostream &fo, long long x, long long scale) {
	fo << (static_cast<double>(x) / static_cast<double>(scale));
}

std::ostream &operator<<(std::ostream &fo, TestOutput &out) {
	for (size_t i=0; i<out.pos.size(); i++) {
		fo << ' ';
		print(fo, out.pos[i].x, out.scale);
		fo << ' ';
		print(fo, out.pos[i].y, out.scale);
	}
	return fo;
}

inline ll sqr(ll x) { return x*x; }

inline bool good(const Position &p1, const Position &p2) {
	ll dist = sqr(p1.x-p2.x) + sqr(p1.y-p2.y);
	return dist >= sqr(p1.r+p2.r);
}

TestOutput run(TestInput in) {
	ll max = *std::max_element(in.r.begin(), in.r.end());
	max = std::max(max, std::max(in.W, in.H));
	TestOutput res;
	res.scale = 1;
	while (max<std::numeric_limits<int>::max()/20) {
		res.scale *= 10;
		max *= 10;
	}
	in.W *= res.scale;
	in.H *= res.scale;
	for (size_t i=0; i<in.r.size(); i++)
		in.r[i] *= res.scale;
	std::vector<int> items(in.r.size());
	res.pos.resize(in.r.size());
	for (size_t i=0; i<in.r.size(); i++) {
		items[i] = (int)i;
		res.pos[i].good = false;
		res.pos[i].r = in.r[i];
	}
	std::mt19937_64 rand(1);
	while (!items.empty()) {
		size_t i = rand()%items.size();
		int item = items[i];
		std::swap(items[i], items.back());
		items.pop_back();
		i = item;

		res.pos[i].x = rand() % in.W;
		res.pos[i].y = rand() % in.H;
		for (size_t j=0; j<in.r.size(); j++) {
			if (res.pos[j].good) {
				if (!good(res.pos[i], res.pos[j])) {
					res.pos[j].good = false;
					good(res.pos[i], res.pos[j]);
					items.push_back((int)j);
				}
			}
		}
		res.pos[i].good = true;
	}

	return res;
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
		std::unique_ptr<TestInput[]> in(new TestInput[T]);
		std::unique_ptr<TestOutput[]> out(new TestOutput[T]);
		for (unsigned int t=0; t<T; t++)
			fi >> in[t];
		unsigned int count = 0;
		concurrency::critical_section mutex;
		concurrency::parallel_for(0u, T, [T, &in, &out, &count, &mutex] (unsigned int i) {
			out[i] = run(in[i]);
			concurrency::critical_section::scoped_lock lock(mutex);
			std::cout << '\r' << (++count) << '/' << T; std::cout.flush();
		});
		for (unsigned int t=0; t<T; t++)
			fo << "Case #" << (t+1) << ": " << out[t] << std::endl;
		std::cout << std::endl;
	} catch (const std::exception &ex) {
		std::cerr << "\nexception: " << ex.what() << std::endl;
	} catch (...) {
		std::cerr << "\nwhoops\n";
	}
	return 0;
}
