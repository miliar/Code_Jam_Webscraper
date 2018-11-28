#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <string>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

#define x first
#define y second
#define rep(i,n) for(ll i=0; i<int(n); i++)
#define dist(i,j) sqrt((i)*(i)+(j)*(j))

using namespace std;

typedef vector<int> vi;
typedef vector<vi>  vvi;
typedef pair<int,int> pii;
typedef long long ll;

ll area(double a, double b, double c) {
    double s = (a + b + c) / 2.;
    double d = s*(s-a)*(s-b)*(s-c);
    if (d<0) return -1;
    double A = sqrt(d);
    return ll(2*A + 0.1);
}

int main() {
    int __N; cin >> __N;
    for (int Nc = 1; Nc <= __N; Nc++) {
        ll n, m, a;
        cin >> n >> m >> a;
        cout << "Case #" << Nc << ": ";
        rep (i,n+1) rep(j,m+1) rep(ii,n+1) rep(jj,m+1) {
           if (area(dist(i,j), dist(ii,jj), dist(i-ii, j-jj)) == a) {
               cout << "0 0 " << i << " " << j << " " << ii << " " << jj << endl;
               goto end;
           } 
        }
        cout << "IMPOSSIBLE" << endl;
        end: ;
    }
}
