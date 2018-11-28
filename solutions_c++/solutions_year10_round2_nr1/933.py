#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <set>
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
    freopen("in/A-large.in","r",stdin);
    freopen("out/A-large.out","w",stdout);

    string str, p;
    int T, N, M, cnt;

    getline(cin,str);
    sscanf(str.c_str(),"%d",&T);
    for(int TT=0; TT<T; ++TT)
    {
        set<string> exist;
        getline(cin,str);
        sscanf(str.c_str(),"%d%d",&N,&M);
        for(int i=0; i<N; ++i)
        {
            getline(cin,str);
            str += "/";
            string::size_type loc = str.find("/",1);
            while(loc != string::npos)
            {
                exist.insert(str.substr(0, loc));
//                cout << "added: " << str.substr(0, loc) << endl;
                loc = str.find("/", loc + 1);
            }
            exist.insert(str);
        }
        cnt = 0;
        for(int i=0; i<M; ++i)
        {
            getline(cin,str);
            str += "/";
//            cout << str << endl;
            string::size_type loc = str.find("/", 1);
            while(loc != string::npos)
            {
                p = str.substr(0, loc);
//                cout << "str: " << str << " p: " << p << endl;
                if(exist.find(p) != exist.end())
                {
//                    cout << "found: " << p << " on " << str << endl;
                }
                else
                {
                    cnt++;
                    exist.insert(p);
                }
                loc = str.find("/", loc + 1);
            }
        }
        cout << "Case #" << (TT+1) << ": " << cnt << endl;
    }

    return 0;
}
