#include <cstdio>
#include <string>
#include <algorithm>
#include <tr1/unordered_map>
using namespace std;
using namespace std::tr1;

unordered_map<int, int> M;

inline int min_rec(int x){
    int ret = x, pow10 = 1, cip;
    for(cip = 1; pow10*10 <= x; cip++)
        pow10 *= 10;
    for(int i = 0; i < cip; i++){
        int t = x%10;
        x /= 10;
        x += t*pow10;
        if(t && x < ret)
            ret = x;
    }
    return ret;
}

inline long long choose2(int x){
    return (long long)x*(x-1)/2;
}

long long cnt(int from, int to){
    M.clear();
    for(int i = from; i <= to; i++)
        M[min_rec(i)]++;
    long long ret = 0;
    for(unordered_map<int, int>::iterator it = M.begin(); it != M.end(); it++)
        ret += choose2(it -> second);
    return ret;
}

int main(void){
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        int a, b;
        scanf("%d %d", &a, &b);
        printf("Case #%d: %lld\n", i, cnt(a, b));
    }
}
