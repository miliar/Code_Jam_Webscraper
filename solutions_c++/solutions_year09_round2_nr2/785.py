#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>
#include <string>
#include <cstring>
using namespace std;
#define sz(x) (int)x.size()
int main() {
    freopen("B-large.out", "w", stdout);
    int t;
    int Case = 1;
    scanf("%d", &t);
    while(t--)  {
        string s;
        cin >> s;
        string tmp = s;
        next_permutation(s.begin(), s.end());
        if(s <= tmp)  {
            s = tmp;
            s += "0";
            sort(s.begin(), s.end());
            int i = 0;
            while(s[i] == '0')  i++;
            swap(s[0], s[i]);
        }
        printf("Case #%d: %s\n", Case++, s.c_str());
    }
    
	return 0;
}
