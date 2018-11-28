#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

long long A, B, P;

vector<long long> primes;

struct Node {
	long long p, rank;
};

vector<struct Node> sets;

long long find_set(long long x)
{
	if (x != sets[x].p) {
		sets[x].p = find_set(sets[x].p);
	}

	return sets[x].p;
}

void link(long long x, long long y)
{
	if (sets[x].rank > sets[y].rank) {
		sets[y].p = x;
	} else {
		sets[x].p = y;
		if (sets[x].rank == sets[y].rank) {
			sets[y].rank++;
		}
	}
}

void u_set(long long x, long long y)
{
	link(find_set(x), find_set(y));
}


void dop(long long p)
{
	long long i, j;
	long long l = (A+p-1)/p*p;
	for (i=l; i<=B; i+=p) {
		for (j=i+p; j<=B; j+=p) {
			//cout << "union: " << i << ' ' << j << ' ' << p << endl;
			u_set(i-A, j-A);
		}
	}
}

long long calc()
{
	sets.clear();
	sets.resize(B-A+1);

	long long i, j, k;
	for (i=0; i<B-A+1; ++i) {
		sets[i].p = i;
		sets[i].rank = 0;
	}

	if (P == 2) {
		dop(2);
	}

	if ((P&1) == 0) P++;

	while (P <= B) {
		bool isp = true;
		for (j=0; primes[j]*primes[j]<=P; ++j) {
			if (P%primes[j] == 0) {
				isp = false;
				break;
			}
		}
		if (isp) {
			dop(P);
		}
		P += 2;
	}

	/*
	for (i=0; i<B-A+1; ++i) {
		cout << i+A << ' ' << find_set(i) << endl;
	}
	*/

	vector<long long> pp;
	for (i=0; i<B-A+1; ++i) {
		pp.push_back(find_set(i));
	}
	sort(pp.begin(), pp.end());
	pp.push_back(-1);

	long long ans = 0;
	long long pre = 0;
	for (i=1; i<pp.size(); ++i) {
		if (pp[i] != pp[pre]) {
			ans++;
			pre = i;
		}
	}
	return ans;
}

int main(void)
{
	primes.push_back(3);

	for (long long i=5; i<=1000001; i+=2) {
		bool isp = true;
		for (long long j=0; primes[j]*primes[j]<=i; ++j) {
			if (i%primes[j] == 0) {
				isp = false;
				break;
			}
		}

		if (isp) {
			primes.push_back(i);
		}
	}

	int N;
	cin >> N;
	for (int i=1; i<=N; ++i) {
		cin >> A >> B >> P;
		cout << "Case #" << i << ": " << calc() << endl;
	}

	return 0;
}
