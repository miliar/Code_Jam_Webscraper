#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <list>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

#define SZ(a) ((int)(a).size())
#define MOD 1000000000
#define MODL 9

using namespace std;

typedef unsigned long long LL;
typedef vector <unsigned long long> VI;
typedef vector <double> VD;
typedef vector <vector<unsigned long long> > VVI;
typedef pair <int,int> PII;
typedef vector <LL> VL;
typedef vector <string> VS;

VI split(string s, string t=" ") {
    VI ret;
    int a,b=0;
    while ((a=s.find_first_not_of(t,b))!=-1) {
        b=s.find_first_of(t,a);
        ret.push_back(atol(s.substr(a,b-a).c_str()));
    }
    return ret;
}

#define INF 0x7fffffff
unsigned long long pow1(unsigned long long a, int b) {
    unsigned long long ret = 1;
    for (int i=0; i<b; i++) {
        ret *= a;
    }
    return ret;
}

main()
{
    int t;
    scanf("%d\n", &t);
    for (int tt =0; tt < t; tt++) {
        unsigned long long ret;
        char buf[1000];
        gets(buf);
        int n = strlen(buf);
        set<int> dict;
        deque<int> numbers;
        for (int i=0; i<n; i++) {
            dict.insert(buf[i]);
            numbers.push_back(i+1);
        }
        numbers[0] = 2;
        numbers[1] = 1;

        int b = dict.size();
        if (b == 1) b = 2;
        map<int,int> memo;
        ret = 0;
        if ( b == 1 ) {
            printf("Case #%d: %d\n", tt+1, 0);
        } else {
            for (int i=0; i<n; i++) {
                unsigned long long p = pow1(b,n-1-i);

                if (!memo[buf[i]]) {
                    memo[buf[i]] = numbers.front();
                    numbers.pop_front();
                }
                ret += p * (unsigned long long)(memo[buf[i]]-1);
            }

            printf("Case #%d: %llu\n", tt+1, ret);
        }
    }
}
