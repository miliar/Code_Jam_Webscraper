#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <numeric>
#include <functional>
#include <algorithm>
#include <cstring>
#include <cassert>
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef set<int> si;
typedef long long ll;
#define pb push_back
#define For(i,a,b) for(int i =(a);i<(b);++i)
#define Rep(i,b) For(i,0,b)
#define ForAll(it,set) for(typeof(set.begin()) it =set.begin();it!=set.end();++it)
#define all(set) set.begin(),set.end()
#define debug(a) (cerr<<#a" = "<<(a)<<endl)
using namespace __gnu_cxx;
#include <ext/hash_set>
#include <ext/hash_map>
namespace __gnu_cxx{
    template<>struct hash<string>{size_t operator () (const string&s)const
    {return hash<char*>()(s.c_str());}};
    template<class A,class B>struct hash<pair<A,B> >{size_t operator () (const pair<A,B>&p)const
        {return hash<A>()(p.first)*0x32671225+hash<B>()(p.second);}};
};
template<class A> string toString(A x){ stringstream ss;ss<<x;return ss.str();}
#define read(a) scanf("%d",&a)


int main()
{
    freopen("test4.in","r",stdin); freopen("test4.out","w",stdout);

    int tt=0;
    cin>>tt;
    for(int caseNo=1;caseNo<=tt;++caseNo){
        int N;
        cin>>N;
        map<int,int> sizes;
        Rep(i,N){
            int a,b;cin>>a>>b;
            sizes[a]=b;
        }
        queue<int> toVisit;
        ForAll(it,sizes)if(it->second>=2)toVisit.push(it->first);
        int total=0;
        while(toVisit.size()){
            int cur = toVisit.front();toVisit.pop();

            //debug(cur);debug(sizes[cur]);
            if(sizes[cur]>=2){
                int x = sizes[cur]/2;
                sizes[cur+1]+=x;
                sizes[cur-1]+=x;
                total+=x;
                sizes[cur]%=2;
                toVisit.push(cur+1);
                toVisit.push(cur-1);
            }

        }

        cout<<"Case #"<<caseNo<<": "<<   total<< endl;
        cerr<<"Case #"<<caseNo<<": "<< total<<   endl;
    }

    return 0;
}
