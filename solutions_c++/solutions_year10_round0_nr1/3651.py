#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <map>
#include <vector>
#include <queue>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define EPS 1E-9
#define INF 0x3F3F3F3f
#define D(x) cout<<__LINE__<<"  "#x" is "<<x<<endl

int main()
{
//    freopen("in/A-small.0.in","r",stdin);
//    freopen("out/A-small.0.out","w",stdout);
    freopen("in/A-large.in","r",stdin);
    freopen("out/A-large.out","w",stdout);

    int T, N, K;

    scanf("%d",&T);
    FOR(TT,T)
    {
        cout << "Case #" << (TT+1) << ": ";
        scanf("%d%d",&N,&K);
        int p = (1<<N);
        if(((K+1)%p)==0) cout << "ON";
        else cout << "OFF";
        cout << endl;
    }


    return 0;
}
