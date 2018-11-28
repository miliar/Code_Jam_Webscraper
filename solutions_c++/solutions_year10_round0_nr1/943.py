#include <iostream>
#include <string>
#include <sstream>
#include <math.h>
#include <vector>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <numeric>
#include <string.h>
using namespace std;

int main()
{
    int nc; cin >> nc; for (int cc = 0; cc < nc; cc++) {
        int n; long long k; cin >> n >> k;
        string res = "OFF";
        if (k%(1LL<<n) == ((1LL<<n)-1)) res = "ON";
        cout << "Case #" << cc + 1 << ": " << res << endl;
    }
    return 0;
}
