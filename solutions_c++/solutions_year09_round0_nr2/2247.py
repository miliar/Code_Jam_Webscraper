#include <iostream>
#include <vector>
#include <map>
using namespace std;
typedef vector<int> A;
typedef vector<A> AA;
typedef vector<char> C;
typedef vector<C> CC;
void solve(const AA& tc, CC& cc) {
    const size_t H = tc.size();
    const size_t W = tc[0].size();
    for (size_t i=0; i<H; i++) {
        for (size_t j=0; j<W; j++) {
            int cur = tc[i][j];
            if (i!=0 && tc[i-1][j] < cur) continue;
            if (j!=0 && tc[i][j-1] < cur) continue;
            if (j+1!=W && tc[i][j+1] < cur) continue;
            if (i+1!=H && tc[i+1][j] < cur) continue;
            cc[i][j] = '-';
        }
    }
    char nextch='A';
    for (size_t i=0; i<H; i++)
        for (size_t j=0; j<W; j++)
            if (cc[i][j] == '-') {
                cc[i][j] = nextch;
                nextch++;
            }
    //int limit = 10000;
    while (true) {
        bool death = false;
        //if (limit-- == 0) {
        //    cout << "bug!!" << W << "," << H << "," << cnt << endl;
        //    break;
        //}
        for (size_t i=0; i<H; i++) {
            for (size_t j=0; j<W; j++) {
                if (cc[i][j]=='*') death = true;
                if (cc[i][j]!='-') {
                    int no,we,es,so;
                    int mn=tc[i][j];
                    no=we=es=so=10000;
                    if (i!=0 && tc[i-1][j] < mn) {
                        no=tc[i-1][j];
                        mn=min(no,mn);
                    }
                    if (j!=0 && tc[i][j-1] < mn) {
                        we=tc[i][j-1];
                        mn=min(we,mn);
                    }
                    if (j+1!=W && tc[i][j+1] < mn) {
                        es=tc[i][j+1];
                        mn=min(es,mn);
                    }
                    if (i+1!=H && tc[i+1][j] < mn) {
                        so=tc[i+1][j];
                        mn=min(so,mn);
                    }
                    if (mn==no) {cc[i][j]=cc[i-1][j];continue;}
                    if (mn==we) {cc[i][j]=cc[i][j-1];continue;}
                    if (mn==es) {cc[i][j]=cc[i][j+1];continue;}
                    if (mn==so) {cc[i][j]=cc[i+1][j];continue;}
                }
            }
        }
        if (! death) break;
    }
    // lexico order
    map<char,char> m;
    nextch='a';
    for (size_t i=0; i<H; i++) {
        for (size_t j=0; j<W; j++) {
            if (m.find(cc[i][j])==m.end()) {
                m[cc[i][j]]=nextch;
                cc[i][j]=nextch;
                nextch++;
            } else {
                cc[i][j]=m[cc[i][j]];
            }
        }
    }
    for (size_t i=0; i<H; i++) {
        size_t l = W - 1;
        for (size_t j=0; j<W; j++) {
            cout << cc[i][j];
            if (j==l) cout << endl;
            else cout << " ";
        }
    }
}
int main () {
    int T; cin >> T;
    vector<AA> testcase(T);
    vector<CC> output(T);
    for (int i=0; i<T; i++) {
        int H, W; cin >> H >> W;
        AA aa(H);
        CC cc(H, C(W, '*'));
        for (int y=0; y<H; y++) {
            A a(W); C c(W);
            for (int x=0; x<W; x++) {
                int inp; cin >> inp;
                a[x]=inp;
            }
            aa[y]=a;
        }
        testcase[i]=aa;
        output[i]=cc;
    }
    // foreach testcase
    for (int i=0; i<T; i++) {
        printf("Case #%d:\n", i+1);
        solve(testcase[i], output[i]);
    }
}
