#include "fstream"
#include "iomanip"
#include "vector"
#include "algorithm"
#include "cmath"

using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

// My random library follows.
struct mersenne_twister {
private:
	static const int size;

	unsigned state[624];

	int index;

public:

	mersenne_twister(unsigned seed = 0XC78845B6) {
		index = 624;

		state[0] = seed;
		for (int i = 1; i < 624; i++) {
			state[i] = 0X6C078965 * (state[i - 1] ^ (state[i - 1] >> 30) + i);
		}
	}

	unsigned next() {
		if (index == 624) {
			index = 0;
			
			for (int i = 0, j = 1, k = 397; i < 624; i++, j++, k++) {
				if (j == 624) {
					j = 0;
				}
				if (k == 624) {
					k = 0;
				}

				unsigned p = (state[i] & 0X80000000U) | (state[j] & 0X7FFFFFFFU);
				state[i] = state[k] ^ (p >> 1U);
				if (p & 1U) {
					state[i] ^= 0X9908B0DFU;
				}
			}
		}

		unsigned p = state[index];
		p ^= p >> 11U;
		p ^= (p << 7U) & 0X9D2C5680U;
		p ^= (p << 15) & 0XEFC60000U;
		p ^= p >> 18U;

		index++;

		return p;
	}
};


template<typename engine>
struct random {
protected:
	engine engine;
	bool normal_init;
	double normal;

public:

	random(unsigned seed = 0) : engine(seed), normal_init(false)
	{ }

	unsigned next() {
		return engine.next();
	}

	unsigned next(unsigned upper) {
		if ((upper & (~upper + 1)) == upper) {
			// If upper is a power of 2. If it is 0, will have an undefined behaviour here.
			return engine.next() % upper;
		}

		// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX*******
		//             ^                       ^
		// complete chunks of size upper    1 incomplete chunk (cannot be empty, because upper is not a power of 2 now).
		// Have to find the size of incomplete chunk. It is exactly (1 << 32) - (1 << 32) % upper.
		// (1 << 32) % upper is equivalent to (0XFFFFFFFF + 0X1) % uppper, which is 0XFFFFFFFF % upper + 0X1, because upper is not a power
		// of 2, so it cannot divide 1 << 32, which prime factors are only 2s.
		// Thus the boundary expression becomes 0XFFFFFFFF - 0XFFFFFFFF % upper.
		unsigned boundary = 0XFFFFFFFF - 0XFFFFFFFF % upper;

		unsigned number;
		do {
			number = engine.next();
		} while (number >= boundary);

		return number % upper;
	}

	int next(int lower, int upper) {
		unsigned count = upper - lower;
		unsigned number = next(count);
		return number + lower;
	}

	double next_real() {
		return 1.0 * (((next() & 0X3FFFFFFULL) << 27U) | (next() & 0X7FFFFFFULL)) / 0X1FFFFFFFFFFFFFULL;
	}

	double next_normal() {
		if (normal_init) {
			normal_init = false;
			return normal;
		}

		double p, q, r;

		do {
			p = 2 * next_real() - 1;
			q = 2 * next_real() - 1;
			r = p * p + q * q;
		} while (r >= 1);

		double s = std::sqrt(-2 * std::log(r) / r);

		normal = q * s;
		normal_init = true;

		return p * s;
	}

};

// End of library code.

struct circle {
	int id;
	int r;
	double x;
	double y;
};

struct compare_r {
	bool operator ()(const circle &a, const circle &b) {
		return a.r > b.r;
	}
};

struct compare_id {
	bool operator ()(const circle &a, const circle &b) {
		return a.id < b.id;
	}
};

inline double sqr(double x) {
	return x * x;
}

bool valid(const vector<circle> &v, int i) {
	for (int j = 0; j < i; j++) {
		if (i != j && sqr(v[j].x - v[i].x) + sqr(v[j].y - v[i].y) < 1E-6 + sqr(v[j].r + v[i].r)) {
			return false;
		}
	}
	return true;
}

void solve(int test) {
	random<mersenne_twister> rand;
	int N, W, L;
	fin >> N >> W >> L;
	vector<circle> R(N);
	for (int i = 0; i < N; i++) {
		fin >> R[i].r;
		R[i].id = i;
	}

	bool swapped = false;
	if (W < L) {
		swap(W, L);
		swapped = true;
	}

	sort(R.begin(), R.end(), compare_r());

	int p = 0;
	int x = -R[0].r;
	int y = 0;
	int next_y = R[0].r;
	while (p < N) {
		if (x + R[p].r > W) {
			y = next_y + R[p].r;
			x = 0;
			next_y = y + R[p].r;
		}
		if (y > L) {
			break;
		}
		R[p].x = x + R[p].r;
		R[p].y = y;

		x += 2 * R[p].r;

		p++;
	}

	while (p < N) {
		while (!valid(R, p)) {
			R[p].x = rand.next_real() * W;
			R[p].y = rand.next_real() * L;
		}
		p++;
	}

	sort(R.begin(), R.end(), compare_id());
	fout << "Case #" << test << ":";
	for (int i = 0; i < N; i++) {
		if (swapped) {
			swap(R[i].x, R[i].y);
		}
		fout << " " << fixed << setprecision(10) << R[i].x << " " << fixed << setprecision(10) << R[i].y;
	}
	fout << "\n";
}

int main() {
	int T;
	fin >> T;

	for (int i = 1; i <= T; i++) {
		solve(i);
	}

	return 0;
}
