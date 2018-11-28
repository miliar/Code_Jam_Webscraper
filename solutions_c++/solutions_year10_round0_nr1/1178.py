#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;
 
#define PB push_back
#define MP make_pair

int tt, n;
long long k;
int main()
    {
        freopen("A-large.in", "r", stdin);
        freopen("A-large.out", "w", stdout);
        cin >> tt;
        for (int nu = 1; nu <= tt; nu++)
            {
                cin >> n >> k;
                long long nn = 1;
                for (int i = 0; i < n; i++)
                    nn *= 2;
                
                k %= nn;
                printf("Case #%d: ", nu);
                if (k == nn - 1)
                    cout << "ON" << endl;
                else
                    cout << "OFF" << endl;
            }
    }
