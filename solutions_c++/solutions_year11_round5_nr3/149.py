#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <climits>
//#include <ext/hash_map>


using namespace std;
using namespace __gnu_cxx;



#define REP(i,n) for(int i = 0; i < int(n); ++i)

#define REPV(i, n) for (int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define FORV(i, a, b) for(int i = (int)(a); i >= (int)(b); --i)

#define FE(i,t) for (typeof((t).begin())i=(t).begin();i!=(t).end();++i)
#define FEV(i,t) for (typeof((t).rbegin())i=(t).rbegin();i!=(t).rend();++i)

#define SZ(a) (int((a).size()))
#define two(x) (1 << (x))
#define twoll(x) (1LL << (x))
#define ALL(a) (a).begin(), (a).end()
#define CLR(a) (a).clear()


#define pb push_back
#define PF push_front
#define ST first
#define ND second
#define MP(x,y) make_pair(x, y)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef queue<int> qi;

template<class T> void checkmin(T &a, T b){if (b<a)a=b;}
template<class T> void checkmax(T &a, T b){if (b>a)a=b;}
template<class T> void out(T t[], int n){REP(i, n)cout<<t[i]<<" "; cout<<endl;}
template<class T> void out(vector<T> t, int n=-1){for (int i=0; i<(n==-1?t.size():n); ++i) cout<<t[i]<<" "; cout<<endl;}
inline int count_bit(int n){return (n == 0)?0:1+count_bit(n&(n-1));}
inline bool bit_set(int a, int b){return (a&two(b));}
inline int low_bit(int n){return (n^n-1)&n;}
inline int ctz(int n){return (n==0?-1:(n&1?0:ctz(n>>1)+1));}
int toInt(string s){int a; istringstream(s)>>a; return a;}
string toStr(int a){ostringstream os; os<<a; return os.str();}

const int maxr=4;
const int mod=1000003;

int r, c;
int mp[maxr][maxr];
pii nxt[maxr][maxr];
int sim[2][maxr][maxr];
int vr[]={1, 0, 1, 1};
int vc[]={0, 1, 1, -1};
map<char, int> rmp;

int main(){
    int tn;
    rmp['/']=3; rmp['|']=0; rmp['-']=1;
    rmp['\\']=2;
    cin>>tn;
    FOR(ti, 1, tn){
        cin>>r>>c;
        getchar();
        REP(i, r){
            string s;
            getline(cin, s);
            REP(j, c) mp[i][j]=rmp[s[j]];
        }

        int cnt=0;
        //string test="1000111010100010";
        REP(m, two(r*c)){

            int ok=1;
            REP(i, r) REP(j, c){
         //       if (test[i*c+j]-'0'!=bool(m&two(i*c+j))){  ok=0;goto out;}
                int sgn=(m&two(i*c+j)?1:-1);
                int k=mp[i][j];
                nxt[i][j].ST=(i+vr[k]*sgn+r)%r;
                nxt[i][j].ND=(j+vc[k]*sgn+c)%c;
            }
         //   printf("<< hre\n");
         //   REP(i, r) REP(j, c) printf("%d %d => %d %d\n", i, j, nxt[i][j].ST, nxt[i][j].ND);

            REP(i, r) REP(j, c) sim[0][i][j]=1;
            REP(k, 20){
                int p=k&1;
                int np=p^1;
                REP(i, r) REP(j, c) sim[np][i][j]=0;
                REP(i, r) REP(j, c) if (++sim[np][nxt[i][j].ST][nxt[i][j].ND]==2){ok=0; goto out;}

            }
out:
            cnt+=ok;


        }


        printf("Case #%d: %d", ti, cnt);
        printf("\n");

    }
    return 0;

}



