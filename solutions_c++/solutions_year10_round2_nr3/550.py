#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<cstring>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

bool get(vector<int>& tmp)
{
    int ind=tmp.size();
    bool go=true;
    while(go)
    {

        if(ind==1) return true;
        bool ok=false;
        for(int i=0;i<sz(tmp);i++) if(tmp[i]==ind)
        {
            ok=true;
            ind=i+1;
            break;
        }
        if(!ok) return false;

    }
    return false;

}

int main()
{
    int t; cin>>t; int cn=0;
    map<int,int> memo;  vector<int> tmp;
    while(t--)
    {
        cn++;
        int n; cin>>n;
        if(memo.count(n))
        {
            printf("Case #%d: %d\n",cn,memo[n]);
            continue;
        }
        vector<int> v;
        for(int i=2;i<=n;i++)
        {
            v.push_back(i);
        }
        int elem=v.size()-1;
        int rv=0;
        for(int mask=0;mask<(1<<elem);mask++)
        {
           // cout<<mask<<endl;
            tmp.clear();
            for(int i=0;i<elem;i++) if(mask&(1<<i)) tmp.push_back(v[i]);
            tmp.push_back(n);
            sort(all(tmp));

            bool ok=get(tmp);
            if(ok) rv++;
            rv%=100003;
        }
        memo[n]=rv;
        printf("Case #%d: %d\n",cn,rv);
    }
    return 0;
}
