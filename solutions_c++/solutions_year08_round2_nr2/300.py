#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <set>
#include <list>
using namespace std;

typedef long long lint;
typedef unsigned long long ulint;

static const ulint primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997};
static const ulint nPrimes = sizeof(primes)/sizeof(primes[0]);

void merge(list<set<ulint> > &sets, int a, int b) {
	list<set<ulint> >::iterator first, second;
	list<set<ulint> >::iterator it = sets.begin();
	//set<ulint> *first = NULL;
//	set<ulint> *second = NULL;
	bool firstF = false;
	bool secondF = false;
	for (; it != sets.end(); ++it) {
		if (it->find(a) != it->end()) {
			first = it;
			firstF = true;
		}
		if (it->find(b) != it->end()) {
			second = it;
			secondF = true;
		}
		if (firstF && secondF) break;
	}
	if (first != second) {
		set<ulint>::iterator iter = second->begin();
		for (; iter != second->end(); ++iter) {
			first->insert(*iter);
		}
		sets.erase(second);
	}
}

int main(int argc, char const *argv[]) {
	int nCases;
	cin >> nCases;
	for (int N = 1; N <= nCases; N++) {
		ulint A, B, P;
		cin >> A >> B >> P;
		ulint D = B - A;
		
		list<set<ulint> > sets;
		for (ulint n = A; n <= B; n++) {
			set<ulint> singleton;
			singleton.insert(n);
			sets.push_back(singleton);
		}
		
		for (ulint i = 0; i < nPrimes; i++) {
			ulint p = primes[i];
			if (p < P) continue;
			if (p > D) break;
			
			ulint m = A - A % p;
			if (m < A) m += p;
			ulint n = m + p;
			for (; n <= B; m = n, n += p) {
				merge(sets, m, n);
			}
		}
		
		cout << "Case #" << N << ": "
		     << sets.size() << endl;
	}
	
	return 0;
}