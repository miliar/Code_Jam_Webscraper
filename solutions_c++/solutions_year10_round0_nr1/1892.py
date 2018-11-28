#include <iterator>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstdlib> 
#include <fstream>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <limits>
#include <cstring>
#include <cmath>
using namespace std;

void
solve(int testCaseNum)
{
    int N, K;
    cin >> N >> K;

    const int pow2N = (int)pow(2, N);

    cout << "Case #" << testCaseNum << ": ";

    if (((K % pow2N) + 1) & (1 << N))
        cout << "ON";
    else
        cout << "OFF";

    cout << endl;
}


int
main()
{
    int N;
    cin >> N;

    for (int i = 1; i <= N; ++i)
        solve(i);
}
    
