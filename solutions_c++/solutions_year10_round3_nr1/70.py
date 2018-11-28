#include <cstdio>
#include <iostream>
#define MAXN 1001
using namespace std;

int T, n;
int x[MAXN], y[MAXN], d[MAXN];
int ai, bi, g;

void qsort(int ll, int rr){
    int i = ll, j = rr, xx = x[d[(i+j)/2]], c;
    while (i <= j){
        while (x[d[i]] < xx) i++;
        while (x[d[j]] > xx) j--;
        if (i <= j){
            c = d[i]; d[i] = d[j]; d[j] = c;
            i++; j--;
        }
    }
    if (i < rr) qsort(i,rr);
    if (ll < j) qsort(ll,j);
}

int main(){
    cin >> T;
    for (int t = 1; t <= T; t++){
        cin >> n;
        for (int i = 0; i < n; i++){
            cin >> ai >> bi;
            x[i] = ai;
            y[i] = bi;
            d[i] = i;
        }
        qsort(0,n-1);
        g = 0;
        for (int i = 0; i < n-1; i++)
            for (int j = i +1; j < n; j++){
                if (y[d[j]] < y[d[i]]) g++;
            }
        cout << "Case #" << t << ": " << g << endl;
    }

    return 0;
}
