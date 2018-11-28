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
typedef vector <int> VI;
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
#define SQR(x) (x)*(x)
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
        int p,q;
        scanf("%d %d\n", &p, &q);
        VI v(q);
        for (int i=0;i<q;i++) {
            scanf("%d", &v[i]);
        }
        scanf("\n");
        sort(v.begin(),v.end());
        int ret = INF;
        do {
            int sum = 0;
            VI memo(p,0);
            for (int i=0; i<v.size(); i++) {
                memo[v[i]-1] = 1;
                for (int j=v[i]-1+1; j<p; j++) {
                    if (memo[j]==0) sum++;
                    else break;
                }
                for (int j=v[i]-1-1; j>=0; j--) {
                    if (memo[j]==0) sum++;
                    else break;
                }
            }
            if (ret > sum) ret = sum;
        } while (next_permutation(v.begin(),v.end()));

        printf("Case #%d: %d\n", tt+1, ret);
    }
}
