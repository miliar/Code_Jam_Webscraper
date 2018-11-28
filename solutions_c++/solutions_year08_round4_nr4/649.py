/*
Coder: Vlad Dumitriu
Email: vladut[dot]mail[at]gmail[dot]com
Quote: 'He is no fool who gives what he cannot keep,
to gain what he cannot lose.' - Jim Eliot

*/

//INCLUDE FILES -  inspiration.h
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
const long double eps = 1e-7;
typedef long long LL;
typedef long double LD;
#define PB push_back
#define NP next_permutation
#define MP make_pair
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define FORE(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define STERGE(v) memset(v,0,sizeof v)
template<class A, class B> A i2s(B x){stringstream s; s<<x; A r; s>>r;return r;} //i2s<string, int>(X)
typedef istringstream iss;
/////////////////////THE CODE BEGINS HERE ////////////////////////////////////////////////////////


void go();
int main() 
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) go();
    //fclose(stdin);
    //getchar();
    return 0;
}

int Case = 0;
string solve(string s, vector<int> P) {
       string R = s;
       for (int i = 0; i < P.size(); ++i) R[i] = s[P[i]-1];
       return R;
       }
void go() {
     int k;
     cin >> k;
     string S;
     cin >> S;
     vector<string> v(S.size() / k);
     int i, j;     for (i = 0; i < S.size(); ++i) v[i/k]+=S[i];
     vector<int> P;
     for (i = 1; i <= k; ++i) P.PB(i);
     int best = S.size();
     do {
         string R = "";
         for (i = 0; i < v.size(); ++i) R+=solve(v[i], P);
         int cost = 0;
         char lst = '*';
         for (i = 0; i < R.size(); ++i) {
             if (R[i] == lst) continue;
             ++cost; lst = R[i];
             }    
         if (cost < best) best = cost;
         } while (NP(all(P)));
     cout << "Case #" << ++Case << ": ";
     cout << best << '\n';
     }
