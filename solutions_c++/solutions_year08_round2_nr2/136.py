#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
int sieve[1001], primes[1000], NP=0;
struct UnionFind 
{
    vector<int> data;
    UnionFind(int size) : data(size, -1) {}
    bool unionSet(int x, int y) {
	x = root(x); y = root(y);
	if (x != y) {
	    if (data[y] < data[x]) swap(x, y);
	    data[x] += data[y]; data[y] = x;
	}
	return x != y;
    }
    bool findSet(int x, int y) {
	return root(x) == root(y);
    }
    int root(int x) {
	return data[x] < 0 ? x : data[x] = root(data[x]);
    }
    int sameSet(int x, int y) { return root(x) == root(y); }
    int size(int x) {
	return -data[root(x)];
    }
};

int main()
{
    fill(sieve+2, sieve+1001, 1);
    for (int i=2; i<32; ++i) {
	if (! sieve[i]) continue;
	for (int j=i+i; j<1001; j+=i) sieve[j] = false;
    }
    for (int i=2; i<1001; ++i) 
	if (sieve[i]) { primes[NP++] = i; }
    
    int N, A, B, P;
    cin >> N;
    for (int t=0; t<N; ++t) {
	cin >> A >> B >> P;
	UnionFind uf(B+1);
	int count = B-A+1;
	for (int j=0; j<NP; ++j) {
	    if (primes[j] < P) continue;
	    int first_one = 0;
	    for (int i=A; i<=B; ++i) {
		if (i % primes[j]) continue;
		if (first_one == 0) first_one = i;
		else if (uf.unionSet(first_one, i)) --count;
	    }
	}
	cout << "Case #" << t+1 << ": " << count << endl;
    }
}
