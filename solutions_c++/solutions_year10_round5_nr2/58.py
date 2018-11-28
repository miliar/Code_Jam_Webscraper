/* 
 * File:   Fence.cpp
 * Author: kimi
 *
 * Created on June 12, 2010, 10:26 PM
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

const string Filename = "B-large";

const int MAXSIZE=200,MAXB=200000;
int N,a[MAXSIZE],best[MAXB],exist[MAXB];
long long L;

bool Less(int a, int b)
{
    if (a==-1) return false;
    if (b==-1) return true;
    return a<b;
}
int main() {
    freopen((Filename + ".in").c_str(), "r", stdin);
    freopen((Filename + ".out").c_str(), "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        cin >> L;
        scanf("%d",&N);
        int n=0;
        for (int i=0; i<N; i++) {
            scanf("%d",&a[i]);
            n=max(n,a[i]);
        }
        Fill(best,-1);
        best[(n-L%n)%n]=0;
        queue<int> que;
        que.push((n-L%n)%n);
        Fill(exist,false);
        while (!que.empty()) {
            int x=que.front();
            exist[x]=false;
            que.pop();
            for (int i=0; i<N; i++)
                if (Less(best[x]+1-(x+a[i]>=n),best[(x+a[i])%n])) {
                    best[(x+a[i])%n]=best[x]+1-(x+a[i]>=n);
                    if (!exist[(x+a[i])%n]) que.push((x+a[i])%n);
                }
        }
        cout << "Case #" << t+1 << ": ";
        if (best[0]>=0) cout << best[0]+(L-1)/n+1;
        else cout << "IMPOSSIBLE";
        cout << endl;
    }
    return (EXIT_SUCCESS);
}
