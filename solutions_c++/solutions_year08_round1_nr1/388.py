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

using namespace std;

typedef long long LL;
typedef vector <int> VI;
typedef vector <double> VD;
typedef vector <vector<int > > VVI;
typedef pair <int,int> PII;
typedef vector <LL> VL;
typedef vector <string> VS;

VS split(string s, string t=" ") {
    VS ret;
    int a,b=0;
    while ((a=s.find_first_not_of(t,b))!=-1) {
        b=s.find_first_of(t,a);
        ret.push_back(s.substr(a,b-a));
    }
    return ret;
}

long long dot(VI v1, VI v2) {
    int n = v1.size();
    long long ret = 0;
    for (int i=0; i<v1.size(); i++) {
        ret += ((long long)v1[i])*((long long)v2[i]);
    }
    return ret;
}

int main()
{
    int _nn;
    scanf("%d\n", &_nn);
    for (int tr=0; tr<_nn; tr++) {
        int n = 0;
        scanf("%d\n", &n);
        VI v1;
        VI v2;
        for (int i=0; i<n; i++) {
            int tmp;
            cin >> tmp;
            v1.push_back(tmp);
        }
        for (int i=0; i<n; i++) {
            int tmp;
            cin >> tmp;
            v2.push_back(tmp);
        }

        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        reverse(v2.begin(),v2.end());
        long long ret = dot(v1,v2);
        printf("Case #%d: %lld\n", tr+1, ret);
    }
    return 0;
}

