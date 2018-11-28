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
#include <gmpxx.h>

// for compilation see http://gmplib.org/

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
        int n;
        is >> n;
        std::vector<mpz_class> numbers;
        for (int i = 0; i < n; ++i) 
        {
            mpz_class tmp;
            is >> tmp;
            numbers.push_back (tmp);
        }
        sort (numbers.begin(),numbers.end());
        for (int i = 1; i < n; ++i) 
        {
            numbers[i] = numbers[i] - numbers[0];
        }

        mpz_class gcd = numbers[1];

        for (int i = 2; i < n; ++i) 
        {
            mpz_gcd (gcd.get_mpz_t(), numbers[i].get_mpz_t(),gcd.get_mpz_t());
        }

        if (numbers[0] % gcd == 0)
            cout << "0\n";
        else
            cout << gcd - (numbers[0] % gcd) << endl;
        
    }
    
}
