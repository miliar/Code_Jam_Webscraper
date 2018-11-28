////
//// Crazy Rows
////
#include <iterator>
#include <iostream>
#include <iomanip>
#include <cstdlib> 
#include <fstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <algorithm>

typedef long long ll;  // 64bit integer
typedef unsigned long long ull;

// const int inf = 1000000009;
// const double pi = atan(1.0)*4.0;
// const double eps = 1e-8;
// ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }


int
mostRight1(const std::string str)
{
    int i = 0;

    for (i = static_cast<int>(str.size()) - 1; i >= 0; --i)
        if (str[i] == '1')
            break;

    return i;
}


ll
getMinNumSwap(const std::deque< std::string > matrix, const int rowNum)
{
    ll returnNum = 0;

    if (static_cast<int>(matrix.size()) == (rowNum + 1)) {
        returnNum = 0;
    }
    else  {
        std::vector<ll> ansVec;
        std::deque< std::string > copyMatrix;

        if (mostRight1(matrix[rowNum]) <= rowNum) {
            ansVec.push_back(getMinNumSwap(matrix, (rowNum + 1)));
        }

        for (int i = (rowNum + 1); i < static_cast<int>(matrix.size()); ++i) {
            if (mostRight1(matrix[i]) <= rowNum) {
                copyMatrix = matrix;

                for (int j = i; j >= 1; --j)
                    copyMatrix[j] = copyMatrix[j - 1];

                ansVec.push_back((i - rowNum) + getMinNumSwap(copyMatrix, (rowNum + 1)));
            }
        }

        returnNum = *(std::min_element(ansVec.begin(), ansVec.end()));
    }

    return returnNum;
}


void
solve(int testCaseNum)
{
    int N;
    std::cin >> N;

    std::deque< std::string > matrix;

    std::string row;
    for (int i = 0; i < N; ++i) {
        std::cin >> row;
        matrix.push_back(row);
    }

    std::cout << "Case #" << testCaseNum << ": " << getMinNumSwap(matrix, 0) << std::endl;
}


int
main()
{
    int nTestCase;
    std::cin >> nTestCase;

    for (int i = 1; i <= nTestCase; ++i)
        solve(i);
}
    
