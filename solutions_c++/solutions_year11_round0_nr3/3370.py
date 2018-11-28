
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>

using namespace std;

#define fori(i,n) for(int i = 0; i < (n); i++)
#define forr(i,a,b) for(int i = (a); i <= (b); i++)

#define EPS 1e-8
#define PI 3.1415926535897932

int main() {
    int T;
    cin >> T;
    fori(kas, T) {
        int n;
        cin >> n;
        int sum = 0;
        int min = INT_MAX;
        int accxor = 0;
        fori(i,n) {
            int x;
            cin >> x;
            if( x < min ) min = x;
            sum += x;
            accxor = accxor ^ x;
        }

        if( accxor ) {
            cout << "Case #" << (kas+1) << ": NO" << endl;
        } else {
            cout << "Case #" << (kas+1) << ": " << (sum-min) << endl;
        }
    }

	return 0;
}

