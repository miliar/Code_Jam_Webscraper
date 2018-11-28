// includes
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int n;
int ds[20000];
int ls[20000];
int start[20000];
int d;

bool swing(int vine) {
    if (d - ds[vine] <= start[vine])
        return true;
    // go back
    for (int i = vine - 1; i >= 0 && ds[vine] - ds[i] <= start[vine]; --i) {
        int x = min(ls[i], ds[vine] - ds[i]);
        if (x > start[i]) {
            start[i] = x;
            if (swing(i))
                return true;
        }
    }
    // go forward
    for (int i = vine + 1; i < n && ds[i] - ds[vine] <= start[vine]; ++i) {
        int x = min(ls[i], ds[i] - ds[vine]);
        if (x > start[i]) {
            start[i] = x;
            if (swing(i))
                return true;
        }
    }
    return false;
}

// main
int main() {
	int num_tests; cin >> num_tests;
	for (int test = 1; test <= num_tests; ++test) {
		cout << "Case #" << test << ": ";
        // read in inputs
		cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> ds[i] >> ls[i];
        cin >> d;
        // do stuff
        start[0] = min(ls[0], ds[0]);
        for (int i = 1; i < n; ++i)
            start[i] = 0;
        cout << (swing(0) ? "YES" : "NO") << endl;
	}
}

