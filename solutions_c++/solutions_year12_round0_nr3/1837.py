// http://code.google.com/codejam
// Task: 

#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> split(int x) {
    vector<int> res;
    while (x > 0) {
        res.push_back(x % 10);
        x = x / 10;
    }
    return res;
}


int test(int n, int A, int B) {
    int res = 0;
    vector<int> a = split(n);
    reverse(a.begin(), a.end());
    set <int> s;
    int N = a.size();
    for (int i = 1; i < N; ++i) {
        int m = 0;
        for (int j = 0; j < N; ++j) {
            int k = (j+i) % N;
            m = m*10 + a[k];
        }
        if (m > n && n >= A && m <= B && s.find(m)==s.end()) {
            res++;
            s.insert(m);
        }
    }
    return res;
}


int main () {
    int test_num;
    scanf("%d", &test_num);
    for(int test_idx = 1; test_idx <= test_num; test_idx++) {
        int A, B;
        scanf("%d %d", &A, &B);

        int res = 0;
        for(int i = A; i < B; i++) {
            res += test(i, A, B);
        }

        printf("Case #%d: %d\n", test_idx, res);
    }
    return 0;
}
