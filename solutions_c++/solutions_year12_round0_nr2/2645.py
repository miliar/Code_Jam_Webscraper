#include <fstream>
using namespace std;

ifstream cin("B-small-attempt0.in");
ofstream cout("B-small-attempt0.out");
int main() {
    int t, i, j, s, p, n, score, best, cnt;
    cin>>t;
    for (i=0; i<t; ++i) {
        cin>>n>>s>>p;
        cnt = 0;
        for (j=0; j<n; ++j) {
            cin>>score;
            if (score%3 == 0)
                best = score/3;
            else
                best = score/3 + 1;
            if (best>=p)
                ++cnt;
            else
                if (s>0 && best+1>=p && best+1<=score) {
                    --s;
                    ++cnt;
                }
        }
        cout<<"Case #"<<i+1<<": "<<cnt<<endl;
    }
    return 0;
}
