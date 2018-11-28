#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int A, B;

string itos(int n) {
    stringstream out;
    out<<n;
    return out.str();
}

int bruteCount() {
    int res = 0;
    for(int i = A;i<=B;++i) {
        for(int j = i+1;j<=B;++j) {
            string s1 = itos(i);
            string s2 = itos(j);
            int N = s1.size();
            for(int k = 0;k<N;++k) {
                string p1 = s1.substr(0,k+1);
                string p2 = s1.substr(k+1,N - k - 1);
                if(p2+p1 == s2) { 
                    ++res;
                    break;
                }
            }
        }
    }
    return res;
}

int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 0;t<T;++t) {
        scanf("%d %d",&A,&B);
        printf("Case #%d: %d\n",t+1, bruteCount());
    }
    return 0;
}
