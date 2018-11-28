#include <cstdlib>

#include <iostream>
#include <fstream>

using namespace std;

static long long  gcd(long long a, long long b) {
    while (b != 0) {
        long long  t = b;
        b = a % b;
        a = t;
    }

    return a;
}

class UF {
public:
    explicit UF (int n) {
        id = new int[n];
        sz = new int[n];
        for (int x = 0; x < n; x++) {
            id[x] = x;
            sz[x] = 1;
        }
    }

    int find(int x) {
        while (x != id[x])
            x = id[x];
        return x;
    }

    bool find (int p, int q) {
        return find (p) == find (q);
    }

    bool unite (int p, int q) {
        const int i = find (p);
        const int j = find (q);
        if (i == j)
            return false;
        if (sz[i] < sz[j]) {
            id[i] = j;
            sz[j] += sz[i];
        } else {
            id[j] = i;
            sz[i] += sz[j];
        }
        return true;
    }

    ~UF () {
        delete [] id;
        delete [] sz;
    }

private:
    int *id;
    int *sz;
};

static const int N = 1000001;
static int largest_prime [N];

int main(int, char *argv[])
{
    ifstream  input (argv[1], ifstream::in);
    ofstream  output (argv[2], ifstream::out);

    for (int i = 2; i < N; i++) {
        if (largest_prime[i] == 0) {
            for (int j = 2; i*j < N; j++) {
                largest_prime[i*j] = i;
            }
        }
    }
    for (int i = 2; i < N; i++) {
        if (largest_prime[i] == 0)
            largest_prime[i] = i;
    }
	int numCases;
	input >> numCases;
	for (int i = 1; i <= numCases; i++) {
        long long A, B, P;
		input >> A;
        input >> B;
        input >> P;
        int numSets = (int) (B - A + 1);
        UF uf (numSets);
        for (long long m = A; m <= B; m++) {
            for (long long n = m + 1; n <= B; n++) {
                if (uf.find ((int) (n - A), (int) (m - A)))
                    continue;
                long long d = gcd (n, m);
                if (d >= P) {
                    int k = (d != m) ? (int) d : (int) (n - m);
                    long long p = largest_prime [k];
                    if (p >= P) {
                        if (uf.unite ((int) (n - A), (int) (m - A)))
                            numSets--;
                    }
                }
            }
        }
		output << "Case #" << i << ": " << numSets << endl;
	}
    output.close();

	return EXIT_SUCCESS;
}
