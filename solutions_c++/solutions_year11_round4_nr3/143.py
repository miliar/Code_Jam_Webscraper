#include <iostream> 
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long int64;

bool prime[1000010];
int64 primes[1000000], pl;
int64 n;

void precount() {
    memset(prime, true, sizeof(prime));
    pl=0;
    for (int p = 2; p <= 1000000; p ++)
        if (prime[p]) {
            primes[++pl] = p;
            for (int tmp = p*2; tmp <= 1000000; tmp += p)
                prime[tmp] = false;
        }
}

void init() {
    cin >> n;
}

void solve(int case_index) {
    cerr<<case_index<<endl;
    if (n == 1) {
        printf("Case #%d: 0\n", case_index);
        return;
    }
    int delta = 1;
    
    for (int i = 1; i <= pl; i ++) {
        int64 p = primes[i], cp = primes[i];
        while (cp * p <= n)
            cp *= p, delta ++;
    }
    
   // printf("%d %d\n", min_t, max_t);
    
    printf("Case #%d: %d\n", case_index, delta);
}

int main() {
    //system("fc c_small_out.txt c_small_out2.txt");
    //system("pause");
    //freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
    //freopen("C-small-attempt1.in", "r", stdin);freopen("c_small_out.txt", "w", stdout);
    freopen("C-large.in", "r", stdin);freopen("c.large_out.txt", "w", stdout);
    
    precount();
    
    int case_count;
    scanf("%d", &case_count);
    for (int i = 1; i <= case_count; i ++) {
        init();
        solve(i);
    }
    return 0;
}
