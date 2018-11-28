#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <bitset>
#include <assert.h>

using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))

#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second

typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;
S getString(int a)
{
    stringstream ss;
    ss<<a;
    return ss.str();
}
int getnum(S s)
{
    stringstream ss;
    ss<<s;
    int a;
    ss>>a;
    return a;
}
int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    freopen("C-large.in","r",stdin);
    freopen("o","w",stdout);
    int t,a;
    set<int> st;
    unsigned long long ans;
    S str;
    cin>>t;
    REP(cases,t)
    {
        ans=0;
        int a,b;
        cin>>a>>b;
        FOR(i,a,b+1)
        {
            st.clear();
            str=getString(i);
            REP(len,str.length()-1)
            {
                //getnum(str);
                rotate(str.begin(),str.begin()+1,str.end());
                int x=getnum(str);
                if(st.find(x)==st.end())
                    st.insert(x);
                else
                    continue;
                if(x>i&&x<=b)
                {
                    ans++;
                    //cout<<i<<" "<<x<<endl;
                }
            }
        }
        
        printf("Case #%d: %d\n",cases+1,ans);
    }
    return 0;
}
