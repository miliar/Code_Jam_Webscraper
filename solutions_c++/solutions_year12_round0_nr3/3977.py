#include <iostream>
#include <vector>
#include <map>
using namespace std;
const int maxn = 2000001;
int main()
{
    vector<int> l(maxn);
    vector<int> lc(maxn);
    vector<int> r(maxn);
    l[0] = 1;
    lc[0] = 1;
    for(int i=1;i<maxn;i++)
    {
        l[i]=10*l[i/10];
        lc[i] = 1+lc[i/10];
        int v = i;
        int best = v;
        int nv = v/10 + (v%10)*(l[i]/10);
        while(nv != i)
        {
            v = nv;
            best = min(best,v);
            nv = v/10 + (v%10)*(l[i]/10);
        }
        r[i] = best;
    }
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        int A,B;
        cin >> A >> B;
        long long ans=0;
        map<pair<int,int>,int> cnt;
        for(int x=A;x<=B;x++)
        {
            ans += cnt[make_pair(lc[x],r[x])];
            cnt[make_pair(lc[x],r[x])]++;
        }
        cout << "Case #" << i << ": " << ans << endl;
    }


}
