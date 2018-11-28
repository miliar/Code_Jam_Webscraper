#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int n;
string st;
map<char, char> M;

int main() {
        ios_base::sync_with_stdio(0);

        ifstream in("map.txt");
        while (getline(in, st)) {
                M[st[0]] = st[2];
        }
        in.close();

        cin >> n;
        getline(cin, st);
        for (int i = 0; i < n; ++i) {
                cout << "Case #" << i + 1 << ": ";
                getline(cin, st);
                int l = st.length();
                for (int j = 0; j < l; ++j) {
                        cout << M[st[j]];
                }
                cout << endl;
        }

        return 0;
}
