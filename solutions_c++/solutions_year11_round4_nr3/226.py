//#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <sstream>
#include <queue>
#include <stack>
#define FOR(i,a,b) for(int i = (a); i <= (b); i++) 
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DR(i,a) for(int i = (a)-1; i >= 0; i--)
#define REP(i,a) for(int i = 0; i < (a); i++)
#define Rep(i,a) for(int i = 0; i < (a); i++)
#define For(i,a,b) for(int i = (a); i <= (b); i++)

#define sqr(x) ((x)*(x))
#define dout debug && cout 
#define ll long long
#define sz size()
#define ull unsigned long long
#define pb push_back
/* DEBUGGING */
bool debug = false;
/* MAIN PROGRAM */

using namespace std;

/*************************TEMPLATE**********************************/
long long convertToNum(string s)
{
    long long val = 0; FR(i,s.size()) val = val * 10 + s[i] - '0';
    return val;
}
string convertToString(long long a) {
    string res = ""; if (!a) return "0";
    while (a) { res = (char)(a % 10 + 48) + res;  a /= 10; }
    return res;
}
long long GCD(long long x,long long y)  {
    if (!x) return y; if (!y) return x;
    if (x == y) return x; if (x < y) return GCD(x,y%x); else return GCD(x%y,y);
}
long long POW(long long x,long long y,long long Base){
    if (!y) return 1; long long u = POW(x,y/2,Base);
    u = (u * u) % Base;
    if (y & 1) return (u * x) % Base; else return u;
}

//newstate = (newstate-1) & oldstate
/**************************CODE HERE*****************************/
#define oo 2000000000000LL
#define maxc 1500000
bool Prime[maxc*2];
vector<long long> list;
void insert(long long u) {
    long long delta = u * u;
    while (delta <= oo) {
        list.push_back(delta);
        delta *= u;
    }
}
void init() {
    list.push_back(2);
    memset(Prime,true,sizeof(Prime));
    Prime[1] = false;
    FOR(i,2,maxc)
    if (Prime[i]) {
        insert(i);
        FOR(j,2,maxc/i) Prime[i*j] = false;
    }
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    init();
    sort(list.begin(),list.end());
    int ntest;
    cin >> ntest;
    long long n;
    FOR(test,1,ntest) {
        cin >> n;
        cout << "Case #" << test << ": ";
        cout << upper_bound(list.begin(),list.end(),n)-list.begin() << endl;
    }
//    system("pause");
    return 0;
}

