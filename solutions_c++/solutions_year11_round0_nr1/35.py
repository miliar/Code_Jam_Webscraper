#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;

#define MAX_N 1000

char Color[MAX_N];
int Position[MAX_N];
int Time[MAX_N];
int N;

int solve() {
    int OPos = 1;
    int BPos = 1;
    for (int i = 0; i < N; i++) {
        int pos = Position[i];
        if (Color[i] == 'O') {
           Time[i] = abs(pos - OPos) + 1;
           OPos = pos;
        } else {
           Time[i] = abs(pos - BPos) + 1;
           BPos = pos;
        }
    }    
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (Color[j] != Color[i]) {
               Time[j] -= Time[i];
               if (Time[j] < 1) {
                  Time[j] = 1;            
               }
               break;             
            }    
        }    
    }
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += Time[i];    
    }
    return sum;
}

int main() {
    int T;
    freopen("C:\\setup\\in1.txt", "r", stdin);
    freopen("C:\\setup\\out1.txt", "w", stdout);
    scanf ("%d", &T);
    int cse = 0;
    while (T--) {
        cse++;
        scanf("%d", &N);
        for (int i = 0; i < N; i++) {
            char clr[10];
            scanf("%s%d", clr, Position + i);
            Color[i] = clr[0];    
        }
        int result = solve();
        printf("Case #%d: %d\n", cse, result);
    }
    //system("pause");
    return 0;    
}
