#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <map>
using namespace std;

typedef vector<int> VI;
int mark[1010];
typedef int LL;
const LL INF = (1<<30);
VI cells;
typedef pair<int,int> pi;
map<pi,int> memo;
LL doit(int start, int end)
{
    if(start>end||end<start) return 0;

    if(memo.find(pi(start,end))!=memo.end()) return memo[pi(start,end)];
    LL ret=INF;
    int ok=1;
    for(int i=0;i<cells.size();i++) {
        if(cells[i]>=start&&cells[i]<=end) {
            ok=0;
            ret=min(ret,doit(start,cells[i]-1)+doit(cells[i]+1,end)+abs(cells[i]-start)
            +abs(cells[i]-end));
        }
    }
    if(ok) ret=0;
    memo[pi(start,end)]=ret;
    return ret;

}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;cin>>T;
    for(int t=1;t<=T;t++) {
        int P,Q;
        cin>>P>>Q;
        cells.clear();
        for(int i=0;i<Q;i++) {
            int v;
            cin>>v;
            cells.push_back(v);
        }
    //    sort(cells.begin(),cells.end());
        memo.clear();
 //       memset(memo,-1,sizeof(memo));

        LL ret = doit(1,P);
        cout<<"Case #"<<t<<": "<<ret<<endl;

    }
    return 0;
}

