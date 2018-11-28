#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std ;

#define	FILE_IN			"B-small.in"
#define	FILE_OUT		"B-small.out"
//#define	FILE_IN			"B-large.in"
//#define	FILE_OUT		"B-large.out"
#define	INF					1000000
#define MIN(a, b)	((a) < (b) ? (a) : (b))
#define MAXN				1000005
#define ok(a, b, c) (((a) + (b) + (c)) % 3 == 0)
#define smaller(x1, y1, x2, y2) (((x1) < (x2) || ((x1) == (x2) && ((y1) <= (y2)))))

typedef long long LL ;

int num_tests ;
LL A, B, P ;

vector<LL> primes ;
int n, ip, t [MAXN] ;

bool is_prime(int n) {
	int limit = (int) sqrt(n) + 5 ;
	for (int i = 0 ; i < primes.size() ; i ++) {
		if (primes [i] > limit) break ;
		if (n % primes [i] == 0) return false ;
	}
	return true ;
}

void gen_primes() {
	primes.push_back(2) ;
	int cur = 3 ;
	while (cur <= 1000005) {
		if (is_prime(cur)) primes.push_back(cur) ;
		cur += 2 ;
	}
}

int find_prime(int prime) {
	int l = 0, r = primes.size() - 1 ;
	while (l < r) {
		int mid = (l + r) / 2 ;
		if (prime == primes [mid]) return mid ;
		if (prime < primes [mid]) r = mid - 1 ;
		else l = mid + 1 ;
	}
	return l ;
}

LL cp, tmp ;

int findgroup(int p) {
	if (t [p] == p) return p ;
	t [p] = findgroup(t [p]) ;
}

void mergegroup(int p1, int p2) {
	if (p1 < p2) t [p2] = p1 ;
	else t [p1] = p2 ;
}

int t2 ;

int dfs(int sgn, LL cur) {
	if (t [cur] == cur) {
		t [cur] = sgn ;
		tmp = sgn ;
		for (int i = ip ; i < primes.size() ; i ++) {
			cp = primes [i] ;
			if (A + cur + cp <= B) {
		 		if ((A + cur) % cp == 0) {
					t [cur] <?= dfs(t [cur], cur + cp) ;
				}
			}
			else {
				break ;
			}
		}		
		return t [cur] ;
	}
	return t [cur] ;
}

int main(int argc, char **argv) {
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;
	
	gen_primes() ;
	in >> num_tests ;	
	for (int test = 1 ; test <= num_tests ; test ++) {
		in >> A >> B >> P ;

		if (P > 1000000) {
			out << "Case #" << test << ": " << (B - A + 1) << endl ;
		}
		else {
			n = B - A ;
			ip = find_prime(P) ;
			for (int i = 0 ; i <= n ; i ++) t [i] = i ;
		
			for (int i = 0 ; i <= n ; i ++) {
				if (t [i] == i) {
					int tmp = dfs(i, i) ;
					if (tmp < t [i]) t [i] = tmp ;
				}
			}
			int cnt = 0 ;
			for (int i = 0 ; i <= n ; i ++) {
				if (t [i] == i) cnt ++ ;
//				cout << i << ", " << t [i] << endl ;
			}
	//		cout << "end" << endl ;
			out << "Case #" << test << ": " << cnt << endl ;
		}
	}
//	int tmp ;
	//cin >> tmp ;
		
	return 0 ;
}


