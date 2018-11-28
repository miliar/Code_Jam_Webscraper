#include <vector>
#include <map>
#include <iostream>

using namespace std;

inline bool is(const pair<unsigned int, unsigned int> &w1, const pair<unsigned int, unsigned int> &w2)
{
    return (w1.first < w2.first && w1.second > w2.second) || (w2.first < w1.first && w2.second > w1.second);
}

int main()
{
    unsigned int T;
    cin >> T;
    for (unsigned int t=1; t<=T; ++t) {
        unsigned int N;
        cin >> N;
        vector< pair<unsigned int, unsigned int> > W(N);
        for (unsigned int n=0; n<N; ++n)
            cin >> W[n].first >> W[n].second;
        unsigned long long I = 0;
        for (unsigned int n1=0; n1<N; ++n1) {
            for (unsigned int n2=n1+1; n2<N; ++n2) {
                if (is(W[n1], W[n2]))
                    ++I;
            }
        }
        cout << "Case #" << t << ": " << I << endl;
    }
}
