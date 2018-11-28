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

const int maxn = 30;

int t;
int f[30];

int main() {

    string str1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
    string str2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

    for(int i=0; i<maxn; i++) f[i] = -1;

    int count = 0;
    for(int i=0; i<str1.length(); i++) {
        int u = str1[i]-'a';
        int v = str2[i]-'a';

        if (f[u] !=-1 && f[u] != v) {
            // cout << f[u] << " " << f[v] << endl;
        } else
        if (f[u] ==-1 ) {
            //cout << str1[i] << endl;
            count++;
        }

        f[u] = v;
    }

    // cout << count << endl;

    for(int i=0; i<'z'-'a'+1; i++) if (f[i] == -1) {
       // cout << char(i+'a') << endl;
    }

    f['z'-'a'] = 'q' - 'a';
    f['q'-'a'] = 'z' - 'a';

    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int test;
    cin >> test;
    cin.ignore();

    string str;
    for(int i=0; i<test; i++) {
        getline(cin,str);
        cout << "Case #" << i+1 << ": ";
        for(int j=0; j<str.length(); j++) if (str[j] != ' ') {
            cout << char( f[ str[j]-'a' ] + 'a');
        } else {
            cout << str[j];
        }
        cout << endl;
    }

    return 0;
}
