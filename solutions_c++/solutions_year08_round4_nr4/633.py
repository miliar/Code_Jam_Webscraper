#include <iostream>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}
int main() {
    int kase;
    freopen("d.out","w", stdout);
    scanf("%d", &kase);
    int cou = 1;
    while(kase--){
        printf("Case #%d: ", cou);
        cou++;
        int k;
        scanf("%d", &k);
        char str[1010];
        scanf("%s", str);
        int len = strlen(str);
        char sto[1010];
        int per[10];
        for (int i = 0; i < k ; ++i)
            per[i] = i;
        int mmin = maxint;
        do{
            for (int i = 0; i < len / k; ++i){
                for (int j = 0; j < k; ++j){
                    sto[i * k + j] = str[i * k + per[j]];
                }
            }
            int cnt = 1;
            for (int i = 1; i < len; ++i){
                if (sto[i - 1] != sto[i])
                    cnt++;
            }
            get_min(mmin, cnt);
        }while(next_permutation(per, per + k));
        printf("%d\n", mmin);
    }
    return 0;
}

