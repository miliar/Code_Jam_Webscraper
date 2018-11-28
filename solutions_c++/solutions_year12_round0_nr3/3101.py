#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define FORALL(a,b) for(typeof((b).begin()) a = (b).begin(); a != (b).end(); ++a)
#define FOR(i,a,b) for(int i = a; i < (int)(b); ++i)

typedef long long LL;

const double EPS = 1e-6;
const int INF = 1<<29;

const int MAX = 9999999;
const int N = 60;
int A[N], B[N], t;

int arr[10];
int base[10];
int ans[N];

void Dfs(int pos, int idx, int value){
    if (value > MAX) return;
    if (pos == 0){
        for (int i = 9; i > 0; --i){
            arr[pos] = i;
            Dfs(pos+1, -1, value*10+i);
        }
    }
    else{
        if (idx == -1 || (idx+1)*2 >= pos){
            set<int> st;
            int v = value;
            while (!st.count(v)){
                st.insert(v);
                int x = v/base[pos];
                v%=base[pos];
                v = v*10+x;
            }
            int cnt[60] = {};
            set<int>::iterator it;
//            printf("#%d %d ", value, pos);
            for (it = st.begin(); it != st.end(); ++it){
                int tmp = *it;
                if (tmp < base[pos]) continue;
                for (int j = 0; j < t; ++j){
                    if (tmp < A[j]) continue;
                    if (tmp > B[j]) continue;
//                  printf("%d ", tmp);
                    ++cnt[j];
                }
            }
//            putchar('\n');
            for (int j = 0; j < t; ++j) ans[j] += (cnt[j]*(cnt[j]-1))>>1;
        }
        for (int i = 9; i >= 0; --i){
            arr[pos] = i;
            if (arr[pos] > arr[idx+1]) continue;
            if (arr[pos] == arr[idx+1]){
                Dfs(pos+1, idx+1, value*10+i);
            }
            else Dfs(pos+1, -1, value*10+i);
        }
    }
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    base[1] = 1;
    for (int i = 1; i < 8; ++i) base[i+1] = base[i]*10;

    int cas = 0;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i){
        ans[i] = 0;
        scanf("%d %d", &A[i], &B[i]);
    }
    Dfs(0, -1, 0);
    for (int i = 0; i < t; ++i) printf("Case #%d: %d\n", ++cas, ans[i]);
    return 0;
}

