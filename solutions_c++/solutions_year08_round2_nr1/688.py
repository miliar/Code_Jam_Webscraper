#include  <stdio.h>
#include  <stdlib.h>
#include  <string.h>
#include  <math.h>
#include  <inttypes.h>
#include  <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

const double EPS = 1e-10;
#define _inline(f...) f() __attribute__((always_inline)); f
#define all(c) (c).begin(), (c).end()
#define tr(c,it) \
    for(typeof(c).begin() it = (c).begin(); it != (c).end(); it++)
#define pb push_back

#define AYBABTU "All your base are belong to us"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;


_inline(int cmp)(double x, double y = 0, double tol = EPS) {
    return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

long long px[100001];
long long py[100001];

int main(int argc, char **argv) {
    long long n, N, a, b, c, d, x0, y0, m;
    long long result;

    cin >> N;
    for(int i=0; i < N; i++){
    	cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
        px[0] = x0;
        py[0] = y0;
        for(int j = 1; j < n; j++){
            px[j] = (a * px[j-1] + b) % m;
            py[j] = (c * py[j-1] + d) % m;
        }
        result = 0;
        for(int k = 0; k < n-2; k++){
            for(int s = k+1; s < n-1; s++){
                for(int t = s+1; t < n; t++){
                    long long tx = px[k]+px[s]+px[t];
                    long long ty = py[k]+py[s]+py[t];
                    if( !( tx % 3 ) && !( ty % 3 ) ){
                        result++;
                    }
                }
            }
        }
        cout << "Case #" << i+1 << ": " << result << endl;
    }
    return 0;
}

