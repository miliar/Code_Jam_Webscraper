#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
using namespace std;
#define ll long long

char s[1001];
char s_tmp[1001];
int perm[6];

int main(){
    int TC;
    scanf("%d\n", &TC);
    for(int tc = 1; tc <= TC; ++tc){
        int k;
        scanf("%d\n", &k);
        scanf("%s\n", s);
        int len = strlen(s);
        for(int i = 0; i < k; ++i)
            perm[i] = i;
        int min_count = len;
        do {
            for(int i = 0; i < len/k; ++i)
                for(int j = 0; j < k; ++j)
                    s_tmp[i*k + j] = s[i*k + perm[j]];
            int count = 1;
            char last_c = s_tmp[0];
            for(int i = 1; i < len; ++i)
                if(s_tmp[i] != last_c){
                    last_c = s_tmp[i];
                    ++count;
                }
            min_count = min(min_count, count);
        } while(next_permutation(perm, &perm[k]));
        printf("Case #%d: %d\n", tc, min_count);
    }
    return 0;
}
