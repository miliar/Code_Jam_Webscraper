#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int merger[30][30];
#define MERGER(a, b) merger[a-'A'+1][b-'A'+1]

bool opposer[30][30];
#define OPPOSER(a, b) opposer[a-'A'+1][b-'A'+1]

char line[105];

int main()
{
    freopen("B-large.in", "rt", stdin);
    freopen("b.small.out", "wt", stdout);
    int T;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        memset(merger, 0, sizeof(merger));
        memset(opposer, 0, sizeof(opposer));
        int C, D, N;
        char u, v, w;
        cin>>C;
        for (int i=0; i<C; ++i)
        {
            cin>>u>>v>>w;
            MERGER(u, v) = w;
            MERGER(v, u) = w;
        }
        cin>>D;
        for (int i=0; i<D; ++i)
        {
            cin>>u>>v;
            OPPOSER(u, v) = OPPOSER(v, u) = 1;
        }
        cin>>N;
        cin>>line;
        string L = "";
        int i;
        for (i=0; i<N; ++i)
        {
            L += line[i];
            int llen = L.length();
            if (MERGER(L[llen-1], L[llen-2]))
            {
                char new_elem = MERGER(L[llen-1], L[llen-2]);
                L.resize(llen-2);
                L += new_elem;
            }
            else
            {
                for (int j=llen-2; j>=0; --j)
                {
                    if (OPPOSER(L[j], L[llen-1]))
                    {
                        L.clear();
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<cas<<": [";
        if (L.length()) cout<<L[0];
        for (int i=1; i<L.length(); ++i) cout<<", "<<L[i];
        cout<<"]"<<endl;
    }
    return 0;
}
