#include <iostream>
#include <fstream>
#include <cstdint>

using namespace std;

struct ratio
{
	uint64_t n, d;
	ratio(uint64_t n = 0, uint64_t d = 1) : n(n), d(d)
	{
		normalize();
	}
	void normalize()
	{
		int g = gcd(n, d);
		n /= g;
		d /= g;
	}
	static int gcd(uint64_t a, uint64_t b)
	{
		while (b != 0)
		{
			uint64_t t = b;
			b = a % b;
			a = t;
		}
		return a;
	}
	ratio& operator=(uint64_t i)
	{
		n = i;
		d = 1;
		return *this;
	}
	ratio& operator*=(const ratio& r)
	{
		n *= r.n;
		d *= r.d;
		normalize();
		return *this;
	}
};
ratio operator*(const ratio& r1, const ratio& r2)
{
	return ratio(r1.n * r2.n, r1.d * r2.d);
}
ratio operator+(const ratio& r1, const ratio& r2)
{
	return ratio(r1.n * r2.d + r2.n * r1.d, r1.d * r2.d);
}
bool operator<(const ratio& r1, const ratio& r2)
{
	return r1.n * r2.d < r2.n * r1.d;
}
ostream& operator<<(ostream& stream, const ratio& r)
{
	return stream << (r.n / (double)r.d);
}

double p[100000];
void solve(istream& input, ostream& output)
{
	int A, B;
	p[0] = 1;

	input >> A >> B;
	for (int i = 1; i <= A; ++i)
	{
		input >> p[i];
		/*int a, b;
		input >> a;
		input.ignore();
		input >> b;
		if (a == 0)
		{
			int d = 10;
			while (d < b)
				d *= 10;
			p[i] = ratio(b, d);
		}
		else
			p[i] = a;*/
		p[i] *= p[i - 1];
	}

	double bestex = B + 2;

	for (int bs = 0; bs <= A; ++bs)
	{
		int ks1 = bs + (B - (A - bs)) + 1;
		int ks2 = ks1 + B + 1;
		
		double p1 = p[A - bs];
		double p2 = 1 - p1;
		//ratio p2 = ratio(p1.d - p1.n, p1.d);

		double ex = p1 * ks1 + p2 * ks2;
		if (ex < bestex)
			bestex = ex;
	}

	output << bestex;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	fout.setf(ios_base::fixed);
	fout.precision(6);

	int T;
	fin >> T;
	for (int i = 1; i <= T; ++i)
	{
		fout << "Case #" << i << ": ";
		solve(fin, fout);
		fout << "\n";
	}
}