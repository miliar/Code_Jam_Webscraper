/* 
 * File:   Theme_Park.cpp
 * Author: kimi
 *
 * Created on May 8, 2010, 2:51 PM
 */

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
#include <complex>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <climits>
#define Fill(A,n) memset(A,n,sizeof(A))
#define pb push_back

using namespace std;

const int MAX_N = 1000;


int R, k, N;

struct Tcost {
    long long sum; // Money already gained.
    int rnd; // Rounds already covered.
} F[MAX_N];
int g[MAX_N];

long long sum;

int getNext(int p) {
    sum = 0;
    for (int i = 0; i < N; i++)
        if (g[(i + p) % N] + sum <= k) sum += g[(i + p) % N];
        else return (i + p) % N;
    return p;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        scanf("%d%d%d", &R, &k, &N);
        for (int i = 0; i < N; i++) scanf("%d", &g[i]);
        Fill(F, 0);
        long long rst;
        for (int p = 0,nextp;; p = nextp) {
            nextp=getNext(p);
            if (F[nextp].rnd) {
                int Lr=F[p].rnd-F[nextp].rnd+1;
                long long Sr=F[p].sum-F[nextp].sum+sum;
                int left=(R-F[nextp].rnd)%Lr;
                int pp=nextp;
                for (int i=0; i<left; i++) pp=getNext(pp);
                rst=F[pp].sum+(R-F[pp].rnd)/Lr*Sr;
                break;
            }
            F[nextp].rnd=F[p].rnd+1;
            F[nextp].sum=F[p].sum+sum;
            if (F[nextp].rnd==R) {
                rst=F[nextp].sum;
                break;
            }
        }
        cout << "Case #" << t+1 << ": " << rst << endl;
    }
    return (EXIT_SUCCESS);
}
