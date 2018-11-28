#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;

static int facts[] = {2, 3, 5, 7};
string s;
int main() {
    int n;
    int modulo = 2*3*5*7;
    scanf("%d", &n);
    for (int cas = 1; cas <= n; cas++) {
        char buf[64]; scanf("%s", buf);
        s = buf;

        int num[50][50]; // [i][j][k] == numbers from j..k mod i
            for (int a = 0; a < s.length(); a++) {
                int n = 0;
                for (int b = a; b < s.length(); b++) {
                    n *= 10;
                    n += s[b] - '0';
                    n %= modulo;
//                    printf("num[%d][%d] = %d\n", a, b, n);
                    num[a][b] = n;
                }
            }
        map<int, long long> answers[50]; // answers[i][j] == map of possible answers mod facts[i] -> count that can be reached with first j chars
        for (int i = 0; i < s.length(); i++) {
            answers[i+1][num[0][i]] = 1;
        }
            for (int l = 2; l <= s.length(); l++) {
                for (int p = 1; p < l; p++) {
                    for (map<int, long long>::iterator it = answers[p].begin(); it != answers[p].end(); ++it) {
                        int ans = it->first + num[p][l-1];
                        ans %= modulo;
 //                       printf("ans[%d][%d] += %d (p = %d)\n", l, ans, it->second, p);
                        answers[l][ans] += it->second;
                        ans = it->first - num[p][l-1];
                        ans %= modulo;
                        ans += modulo;
                        ans %= modulo;
  //                      printf("ans[%d][%d] += %d (p = %d)\n", l, ans, it->second, p);
                        answers[l][ans] += it->second;
                    }
                }
            }
        
        long long ans = 0;
        
        for (map<int, long long>::iterator it = answers[s.length()].begin(); it != answers[s.length()].end(); ++it) {
            if (it->first % 2 == 0 || it->first % 3 == 0 || it->first % 5 == 0 || it->first % 7 == 0) {
   //             printf("%d: %d\n", it->first, it->second);
                ans += it->second;
             }
        }
        
        printf("Case #%d: %lld\n", cas, ans);
    }
}
