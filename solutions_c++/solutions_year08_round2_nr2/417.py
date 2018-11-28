#include <algorithm>
#include <string>
#include <cstdio>
#include <map>
#include <vector>
#define X first
#define Y second
#define PII pair<int, int>
#define PB push_back
#define FOREACH(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define MAXN 1000

using namespace std;

int pr[MAXN+1];

int gcd(int a, int b) { 
   return ( b != 0 ? gcd(b, a % b) : a ); 
}

int main() {
    int ncase;
    scanf("%d", &ncase);

    for (int i = 0; i < MAXN+1; ++i)
        pr[i] = 0;
    for (int i = 2; i < MAXN+1; ++i)
        if (pr[i] == 0)
            for (int j = 1; i*j < MAXN+1; ++j)
                pr[i*j] = i;
    
    for (int icase = 0; icase < ncase; ++icase) {
        int a, b, p;
        scanf("%d %d %d", &a, &b, &p);
        int inset[b-a+1];
        for (int i = a; i <= b; ++i)
            inset[i-a] = i;
        for (int i = a; i < b; ++i)
            for (int j = i+1; j <= b; ++j) {
                int gcd_ = gcd(j, i);
                if (gcd_ > 1 && pr[gcd_] >= p) {
                    int isi = inset[i-a];
                    int isj = inset[j-a];
                    for (int k = a; k <= b; ++k)
                        if (inset[k-a] == isi)
                            inset[k-a] = isj;
                }
            }
        bool found[b-a+1];
        for (int i = a; i <= b; ++i)
            found[i-a] = false;
        int sol = 0;
        for (int i = a; i <= b; ++i) {
            if (!found[inset[i-a]-a]) {
                ++sol;
                found[inset[i-a]-a] = true;
            }
        }       
        printf("Case #%d: %d\n", icase+1, sol);
    }
    return 0;
}
