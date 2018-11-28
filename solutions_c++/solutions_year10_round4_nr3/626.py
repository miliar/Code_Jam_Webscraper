#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 

set<pii> s[2];

int main()
{
    int cn;
    scanf("%d", &cn);
    for (int ci = 1; ci <= cn; ci++) {
        printf("Case #%d: ", ci);
        int R;
        scanf("%d", &R);
        int p[4];
        s[0].clear();
        s[1].clear();
        REP(idx, R) {
            REP(i, 4)
                scanf("%d", p + i);
            for (int i = p[0]; i <= p[2]; i++)
                for (int j = p[1]; j <= p[3]; j++)
                    s[0].insert(make_pair(i, j));
        }
        R = 0;
        int st = 0;
        while (s[st].size()) {
            //~ cout<<s[st].size()<<endl;
            R++;
            for (set<pii>::iterator it = s[st].begin(); it != s[st].end(); it++) {
                int x = (*it).first;
                int y = (*it).second;
                if (s[st].find(make_pair(x - 1, y)) != s[st].end() || s[st].find(make_pair(x, y - 1)) != s[st].end())
                        s[1 - st].insert(make_pair(x, y));
                x++;
                if (s[st].find(make_pair(x, y - 1)) != s[st].end())
                    s[1 - st].insert(make_pair(x, y));
            }
            s[st].clear();
            st = 1 - st;
        }
        printf("%d\n", R);
        cerr<<ci<<endl;
    }
    return 0;
}
