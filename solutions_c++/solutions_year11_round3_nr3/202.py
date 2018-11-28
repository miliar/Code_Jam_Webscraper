#include <cstring>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

long long notes[10005];

int main()
{
    freopen("C-small-attempt0.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int T, N;
    long long L, H;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        cin>>N>>L>>H;
        for (int i=0; i<N; ++i)
        {
            cin>>notes[i];
        }
        bool pos = 0;
        long long i;
        printf("Case #%d: ", cas);
        for (i=L; i<=H && !pos; ++i)
        {
            pos = 1;
            for (int j=0; j<N && pos; ++j)
            {
                if (notes[j]%i && i%notes[j]) pos = 0;
            }
            if (pos) cout << i << endl;
        }
        if (!pos) cout << "NO" << endl;
    }
    return 0;
}
