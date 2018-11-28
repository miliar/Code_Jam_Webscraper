#include <cstdio>
#include <cstring>
#include <cctype>
#include <climits>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdarg>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <exception>
#include <stdexcept>
#include <memory>
#include <locale>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <iterator>
#include <functional>
#include <string>
#include <complex>
#include <valarray>

#define rep(i, n) for (int i = 0; i < n; ++ i)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define ll long long
#define cmplxd complex <long double>
#define pi 3.14159265358979323846264338327950288


using namespace std;

int ntest;

int getleng(int num) {
    int leng = 0;
    while (num>0) {
        leng++;
        num = num/10;
    }

    return leng;
}

int cal(int u,int b) {
    int num = u;
    int leng = getleng(num);
    int l = 1;

    for(int i=1; i<leng; i++) l = l*10;

    set<int> m;
    m.clear();

    for(int i=1; i<leng; i++) {
        num = (num%10)*l + (num/10);
        if (num <=b && num>u) {
            // cout << u << " " << num << endl;
            m.insert(num);
        }
    }

    return int(m.size());
}

int main() {

    freopen("C-large.in","r",stdin);
    freopen("Clarge.txt","w",stdout);

    cin >> ntest;
    int a,b,res;
    //cout << ntest << endl;
    for(int test=0; test < ntest; test++) {
        cin >> a >> b;
        res = 0;
        for(int i=a; i<=b; i++) {
            res += cal(i,b);
        }

        cout << "Case #" << test+1 << ": " << res << endl;
    }

    return 0;
}
