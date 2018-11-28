#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>
#include <stack>
#include <stdexcept>

using namespace std;

typedef long long ll;

int main() {
    int num_cases;
    cin >> num_cases;
    string line;
    getline (cin, line);
    for (int case_num = 1; case_num <= num_cases; ++case_num) {
        cout << "Case #" << case_num << ": ";
        getline (cin, line);
        istringstream is (line);
        ll n,k;
        is >> n >> k;
        ll twopown = 1LL << n;
        if (k % twopown == twopown-1) 
        {
            cout << "ON" << endl;
        } else {
            cout << "OFF" << endl;
        }
    }
    
}
