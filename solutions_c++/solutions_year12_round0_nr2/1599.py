#include <cstdio>
#include <vector>
using namespace std;

int T, S, N, p;
vector< int > vec;

void input() {
    vec.clear();
    scanf("%d%d%d", &N, &S, &p);
    for(int i = 0, j; i < N; ++i) {
        scanf("%d", &j);
        vec.push_back(j);
    }
}

int cal() {
    vector< int > d1;
    vector< vector< int > > d2(3, d1);
    for(int i = 0, j = vec.size(); i < j; ++i) {
        d2[vec[i] % 3].push_back(vec[i] / 3);
    }
    int ret = 0;
    for(int i = 0, j = d2[1].size(); i < j; ++i) {
        if(d2[1][i] + 1 >= p) {
            ++ret;
        }
    }
    for(unsigned i = 0; i < d2[2].size(); ) {
        if(d2[2][i] + 1 >= p) {
            ++ret;
            d2[2].erase(d2[2].begin() + i);
        } else {
            ++i;
        }
    }
    unsigned i = 0;
    while(S > 0 && i < d2[2].size()) {
        for(i = 0; i < d2[2].size(); ) {
            if(d2[2][i] + 2 >= p) {
                ++ret;
                --S;
                d2[2].erase(d2[2].begin() + i);
                break;
            } else {
                ++i;
            }
        }
    }
    for(unsigned i = 0; i < d2[0].size(); ) {
        if(d2[0][i] >= p) {
            ++ret;
            d2[0].erase(d2[0].begin() + i);
        } else {
            ++i;
        }
    }
    i = 0;
    while(S > 0 && i < d2[0].size()) {
        for(i = 0; i < d2[0].size(); ) {
            if(d2[0][i] + 1 >= p && d2[0][i] - 1 >= 0) {
                ++ret;
                --S;
                d2[0].erase(d2[0].begin() + i);
                break;
            } else {
                ++i;
            }
        }
    }

    return ret;
}

void output(int cases) {
    printf("Case #%d: %d\n", cases, cal());
}

int main() {
    scanf("%d", &T);
    for(int i = 1; i <= T; ++i) {
        input();
        output(i);
    }
    return 0;
}