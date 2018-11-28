#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
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
#include <string>
#include <utility>
#include <vector>
using namespace std;

int sets;
struct node {
  int size; node *p;
	void make_set() { p=this, size=1; }
  void u(node* y) { // union, works if already in same set.
		node* xR = find(), *yR = y->find();
		if (xR==yR) return; // already in same set.
		--sets;
		if(xR->size > yR->size) yR->p = xR, xR->size += yR->size;
		else xR->p = yR, yR->size += xR->size;
	}
	// Van Leeuwen, halving, one pass method, asymptotically optimal.
	node* find() { 		
		node *x=this;
		while (x->p->p != x->p) x = x->p = x->p->p;
		return x->p;
	}
};
typedef long long LL;

const int MAX=1000500;
bool isprime[MAX];
vector<LL> primes;
node S[MAX];
LL P,A,B;

int main() {
	memset(isprime,1,sizeof isprime);
	isprime[0]=isprime[1]=0;
	for (LL i=2;i<MAX;++i) if (isprime[i]) {
		primes.push_back(i);
		for (LL j=2;i*j<MAX;++j) isprime[i*j]=0;
	}
	int T;
	cin >>  T;	
	for (int z=1;z<=T;++z) {
		cin >> A >> B >> P;
		sets=0;
		for (LL i=A;i<=B;++i) S[i-A].make_set(),++sets;
		for (LL i=0;i<primes.size();++i) if (primes[i]>=P) {
			LL last = -1;
			LL p = (A/primes[i])*primes[i];
			for (;p<=B;p+=primes[i]) {
				if (A <= p && p <= B) {
					if (last!=-1) S[p-A].u(&S[last-A]);
					last=p;
				}
			}
		}
		printf("Case #%d: %d\n", z, sets);
	}
}
