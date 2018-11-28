#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

set<int>* sets[1024];
vector<int> factors[1024];

vector<int> factorize(int n)
{
	vector<int> v;
	for (int i = 2; n != 1; ++i) {
		if (n % i == 0)
			v.push_back(i);
		while (n % i == 0)
			n /= i;
	}
	return v;
}

void printset(set<int> *s)
{
	printf("%p:", s);
	for (set<int>::iterator it = s->begin(); it != s->end(); ++it) {
		printf(" %d", *it);
	}
	puts("");
}

int main()
{
	int T, A, B, P;
	for (int i = 1; i < 1024; ++i)
		factors[i] = factorize(i);

	scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		scanf("%d %d %d", &A, &B, &P);

		for (int i = A; i <= B; ++i) {
			sets[i] = new set<int>();
			sets[i]->insert(i);
		}

		for (int i = A; i <= B; ++i) {
			for (int j = A; j <= B; ++j) {
				if (sets[i] == sets[j])
					continue;
				int x = 0, y = 0;
				while (x < SZ(factors[i]) && y < SZ(factors[j])) {
					if (factors[i][x] == factors[j][y]) {
						if (factors[i][x] >= P) {
							//printset(sets[i]);
							//printset(sets[j]);
							//puts("--------------------");
							//fflush(stdout);
							//static int t = 0;
							//if (++t > 4) exit(1);
							sets[i]->insert(ALL(*sets[j]));
							set<int> *p = sets[j];
							for (set<int>::iterator it = p->begin(); it != p->end(); ++it) {
								sets[*it] = sets[i];
							}
							delete p;
							break;
						}
						x += 1;
						y += 1;
					} else if (factors[i][x] < factors[j][y]) {
						x += 1;
					} else {
						y += 1;
					}
				}
			}
		}

		set< set<int>* > pointers;
		for (int i = A; i <= B; ++i) {
			if (sets[i] == 0)
				continue;
			pointers.insert(sets[i]);
		}

		printf("Case #%d: %d\n", tt+1, SZ(pointers));

		for (int i = A; i <= B; ++i) {
			set<int> *p = sets[i];
			if (p == 0)
				continue;
			for (set<int>::iterator it = p->begin(); it != p->end(); ++it) {
				sets[*it] = 0;
			}
			delete p;
		}
	}
	return 0;
}
