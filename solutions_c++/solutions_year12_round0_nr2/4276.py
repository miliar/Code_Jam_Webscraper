#include <iostream>
#define maxn 111
using namespace std;
int main () {
    int Ntest, a[maxn];
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);    
    scanf("%d",&Ntest);
    for(int run = 0; run < Ntest; run ++) {
            int N, S, p , result(0);
            cin >> N >> S >> p;
            while (N--) {
                  int t;
                  cin >> t;
                  if (!p) {result ++; continue;}
                  if (p==1) {
                            if (t>0) result++;
                            continue;
                  }
                  if (t > (p-1) * 3) result++;
                  else if (t >= p * 3 - 4) 
                       if (S) { S--; result ++;}
            }        
            cout << "Case #" << run+1 << ": " << result << endl;
    }
    return 0;   
}
