#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long LL;

const int SZ = 2000000;

bool primev[SZ];
vector<LL> primes;

void initPrimes()
{
    primes.clear();
    fill(primev, primev + SZ, true);
    primev[0] = primev[1] = false;

    for (int i = 2; i < SZ; ++i)
        if (primev[i]) {
            primes.push_back(i);
            for (int j = i + i; j < SZ; j += i)
                primev[j] = false;
        }
    return;
}

struct Tree
{
    Tree* parent;

    Tree(): parent(0) {}

    bool merge(Tree* tree) {
        while (tree->parent)
            tree = tree->parent;

        return domerge(tree);
    }

    bool domerge(Tree* tree) {
        if (parent) {
            bool r = parent->domerge(tree);
            parent = tree;
            return r;
        }
        if (this == tree) return false;
        parent = tree;
        return true;
    }
};

int main()
{
    initPrimes();

    int cases;
    cin >> cases;
    for (int cs = 0; cs < cases; ++cs) {
        LL A, B, P;
        cin >> A >> B >> P;

        vector<Tree*> nodes;
        for (LL i = A; i <= B; ++i) {
            nodes.push_back(new Tree);
        }

        LL sz = B - A + 1;

        for (int i = 0; i < (int)primes.size(); ++i) {
            LL p = primes[i];
            if (p < P) continue;
            LL base = (A / p) * p;
            while (base < A) base += p;
            LL val = base;
            while (val <= B) {
                if (nodes[val - A]->merge(nodes[base - A])) --sz;
                val += p;
            }
        }

        for (LL val = A; val <= B; ++val) {
            int i = 0;
            LL v = val;
            while (v > 1 && i < (int)primes.size()) {
                LL p = primes[i];
                while (v % p == 0) v /= p;
                ++i;
            }
            if (v > 1) {
                LL base = (A / v) * v;
                while (base < A) base += v;
                LL val = base;
                while (val <= B) {
                    if (nodes[val - A]->merge(nodes[base - A])) --sz;
                    val += v;
                }
            }
        }

        for (int i = 0; i < (int)nodes.size(); ++i)
            delete nodes[i];

        cout << "Case #" << cs + 1 << ": " << sz << '\n';
    }

    return 0;
}
