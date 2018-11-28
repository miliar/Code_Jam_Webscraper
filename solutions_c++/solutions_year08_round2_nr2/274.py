#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

#define FOREACH(it,x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define ALL(x) (x).begin(), (x).end()
template<class T> void DUMP(const T& v) { FOREACH(it,v) cout<<*it<<' '; cout<<endl; }

class union_find {
private:
  vector<int> u;
  vector<int> w;
public:
  union_find(size_t n) : u(n), w(n,1) {
    for (int i = 0; i < u.size(); i++) u[i] = i;
  }
  int root(int p) {
    for (; p != u[p]; p = u[p]) u[p] = u[u[p]];
    return p;
  }
  // returns true if p and q were already linked.
  bool link(int p, int q) {
    p = root(p); q = root(q);
    if (p == q) return true;
    u[p] = q; w[q] += w[p]; w[p] = 0;
    return false;
  }
  bool find(int p, int q) { return root(p) == root(q); }
  int size(int p) { return w[root(p)]; }
  int count() {
    int cnt = 0;
    for (int i = 0; i < u.size(); i++) cnt += w[i] != 0 ? 1 : 0;
    return cnt;
  }
};

vector<int> make_prime(int n) {
	vector<int> p(n);
	for (int i = 2; i < n; i++) p[i] = i;
	for (int i = 2; i*i < n; i++)
		if (p[i])
			for (int j = i*i; j < n; j+=i)
				p[j] = 0;
	p.erase(remove(p.begin(),p.end(),0),p.end());
	return p;
}

int main() {
	int TC; cin>>TC;
	vector<int> prime = make_prime(1001);
	for (int testcase = 1; testcase <= TC; testcase++) {
		int a, b, p;
		cin>>a>>b>>p;
		union_find uf(b-a+1);
		int start = lower_bound(ALL(prime), p) - prime.begin();
		//cout<<start<<endl;
		for (int n = a; n < b; n++) {
			for (int m = n+1; m <= b; m++) {
				for (int i = start; i < prime.size(); i++) {
					if (n % prime[i] == 0 && m % prime[i] == 0) {
						uf.link(n-a,m-a);
						//cout<<n<<m<<endl;
						break;
					}
				}
			}
		}
		cout<<"Case #"<<testcase<<": "<<uf.count()<<endl;
	}
	return 0;
}
