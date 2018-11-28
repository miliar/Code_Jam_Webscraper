#include <string>
#include <fstream>
#include <algorithm>
using namespace std;

#define TYPE_A false
#define TYPE_B true
const int MAX_N = 205;

ifstream in("B.in");
ofstream out("B.out");

struct train {
    int start, end;
    bool type;
    bool operator < (const train &B) const {
        const train &A = *this;
        if(A.start != B.start)
            return A.start < B.start;
        if(A.end != B.end)
            return A.end < B.end;
        return A.type < B.type;
    }
};

int T, N;
train A[MAX_N];
bool marked[MAX_N];
int cntA, cntB;

inline int get_minutes(const string &s) {
    return ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + ((s[3] - '0') * 10 + (s[4] - '0'));
}

void read() {
    int NA, NB;
    string s1, s2;
    in >> T >> NA >> NB;
    N = NA + NB;
    for(int i = 0; i < NA; ++i) {
        in >> s1 >> s2;
        A[i].start = get_minutes(s1);
        A[i].end = get_minutes(s2) + T;
        A[i].type = TYPE_A;
    }
    for(int i = 0; i < NB; ++i) {
        in >> s1 >> s2;
        A[i + NA].start = get_minutes(s1);
        A[i + NA].end = get_minutes(s2) + T;
        A[i + NA].type = TYPE_B;
    }
}

void solve() {
    cntA = cntB = 0;
    sort(A, A + N);
    memset(marked, 0, N * sizeof(bool));
    for(int i = 0; i < N; ++i)
        if(!marked[i]) {
            marked[i] = true;
            if(A[i].type == TYPE_A)
                ++cntA;
            else
                ++cntB;
            for(int last = i, j; last < N; last = j)
                for(j = last + 1; j < N; ++j)
                    if(!marked[j] && A[j].type != A[last].type && A[last].end <= A[j].start) {
                        marked[j] = true;
                        break;
                    }
        }
}


int main() {
    int T;
    in >> T;
    for(int i = 1; i <= T; ++i) {
        read();
        solve();
        out << "Case #" << i << ": " << cntA << " " << cntB;
        if(i < T)
            out << "\n";
    }
    return 0;
}
