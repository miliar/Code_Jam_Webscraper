



#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int calc(int v, int s) {
    int ret = 0;
    
    if (v == 0) return 0;
    if (v == 1) return 1;
    if (v == 2) {
        if (s == 0) return 1;
        else return 2;
    }
    
    if (s) {
        switch (v%3) {
            case 0:
                ret = v/3+1;
                break;
            case 1:
                ret = v/3+1;
                break;
            case 2:
                ret = v/3+2;
                break;
        }
    } else {
        switch (v%3) {
            case 0:
                ret = v/3;
                break;
            case 1:
                ret = v/3+1;
                break;
            case 2:
                ret = v/3+1;
                break;
        }
    }
    return ret;
}

int main() {

    int T;
    scanf("%d", &T);
    
    for (int tt = 1; tt <= T; tt++) {
    
        int N, S, P;
        scanf("%d %d %d", &N, &S, &P);
    
        vector<int> totals;
        
        for (int i = 0; i < N; i++) {
            int t;
            scanf("%d", &t);
            totals.push_back(t);
        }
        
        
        int sol = 0;
    
        for (int i = 0; i < N; i++)
            if (calc(totals[i], 0) >= P) {
                sol++;
            } else if (calc(totals[i], 1) >= P && S) {
                sol++;
                S--;
            } 
           
    
        printf("Case #%d: %d\n", tt, sol);
        
        
        
    }

}
