#include <cstdio>
#include <deque>
#include <set>
using namespace std;

char A[2000005];

int T, n, m;

void input() {
    scanf("%d%d", &n, &m);
}

int subdeq(deque< int >& d, int from, int to) {
    int t = 1, ret = 0;
    while(to >= from) {
        ret += d[to] * t;
        --to;
        t *= 10;
    }
    return ret;
}

int cal() {
    int ret = 0;
    int t = 1, nn = n, d = 0;
    while(nn) {
        t *= 10;
        nn /= 10;
        ++d;
    }
    t /= 10;
    int m_t = m - t + 1;
    for(int i = 0; i < m_t; ++i) {
        A[i] = 0;
    }
    for(int i = n; i <= m; ++i) {
        int x = i - t;
        if(A[x] == 0) {
            int num = i;
            deque< int > deq;
            set< int > setn;
            setn.insert(num);
            while(num) {
                int r = num % 10;
                deq.push_front(r);
                num /= 10;
            }
            for(unsigned j = 0, k = deq.size(); j < k; ++j) {
                deq.push_back(deq[j]);
            }
            for(unsigned j = 1, k = j + d; k < deq.size(); ++j, ++k) {
                int sh_num = subdeq(deq, j, k - 1);
                if(sh_num >= n && sh_num <= m && sh_num != i) {
                    setn.insert(sh_num);
                    //printf("[%d] ", sh_num);
                }
            }
            if(setn.size() > 1) {
                int add = (1 + (setn.size() - 1)) * (setn.size() - 1) / 2;
                set< int > :: const_iterator it = setn.begin();
                while(it != setn.end()) {
                    A[*it - t] = 1;
                    ++it;
                }
                ret += add;
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
