#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <vector>
#include <set>
using namespace std;

vector<int> primes;

void genPrimes() {
	const int MAX_PR = 1100000;
	bitset<MAX_PR + 1> bs(0);
	bs[0] = bs[1] = 1;
	for (int i = 2; i < MAX_PR; i++) {
		if (bs[i])
			continue;
		primes.push_back(i);
		for (int j = 2*i; j < MAX_PR; j+=i) {
			bs[j] = true;
		}
	}
}



typedef pair<long long, long long> pii;

inline pii swapFS(const pii& p) throw() {
	return pii(p.second, p.first);
}

pii solveDiaf(long long a, long long b) {
	if (a < b)
		return swapFS(solveDiaf(b, a));
	if (b == 0) {
		assert(a == 1);
		return pii(1, 0);
	}
	pii r = solveDiaf(b, a % b);
	r.first -= a / b * r.second;
	return swapFS(r);
}

inline long long safeMod(long long x, long long p) {
	long long i = p;
	while (x < 0) {
		x += i;
		i += i;
	}
	return x % p;
}

inline int findObr(int p, int x) {
	long long res = solveDiaf(x, p).first;
	assert((x * res - 1) % p == 0);
	return (int)safeMod(res, p);
}

int main(void) {
	genPrimes();
	int testNum;
	cin >> testNum;
	// scanf("%d", &testNum);
	for (int testNo = 1; testNo <= testNum; testNo++) {
		cout << "Case #" << testNo << ": ";
		int k, d;
		cin >> d >> k;
		int limit = 1;
		while (d--)
			limit*=10;
		vector<int> rndOut(k);
		int minp = 0;
		for (int i = 0; i < k; i++) {
			cin >> rndOut[i];
			minp = max(minp, rndOut[i] + 1);
		}
		if (k < 3) {
			if (k == 2 && rndOut[0] == rndOut[1])
				cout << rndOut[0] << endl;
			else
				cout << "I don't know." << endl;
			continue;
		}
		set<int> res;
		int s1 = rndOut[0];
		int s2 = rndOut[1];
		int s3 = rndOut[2];
		int slast = rndOut.back();
		for (int i = 0; primes[i] <= limit; i++) {
			long long a, b;
			int p = primes[i];
			if (p < minp)
				continue;
			if (s1 == s2) {
				a = 1;
				b = 0;
			} else {
				int det = s1 - s2;
				if (det < 0)
					det += p;
				int obrdet = findObr(p, det);
				long long deta = s2 - s3;
				if (deta < 0)
					deta += p;
				long long detb = safeMod(s1 * (long long)s3 - s2 * (long long)s2, p);
				a = safeMod(deta * obrdet, p);
				b = safeMod(detb * obrdet, p);
				assert((a * s1 + b) % p == s2);
				assert((a * s2 + b) % p == s3);
			}
			bool good = false;
			for (int i = 0; i < k; i++) {
				if (i == k - 1)
					good = true;
				else {
					if ((a * rndOut[i] + b) % p != rndOut[i + 1]) {
						break;
					}
				}
			}
			if (good)
				res.insert((a * rndOut.back() + b) % p);
		}
		assert(res.size() != 0);
		if (res.size() == 1) {
			cout << *res.begin() << endl;
		} else
			cout << "I don't know." << endl;
	}
	return 0;
}
