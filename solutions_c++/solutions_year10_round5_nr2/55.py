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
    template<>struct hash<ll>{size_t operator () (const ll&p)const
        {return size_t(p);}};
};
template<class A> string toString(A x){ stringstream ss;ss<<x;return ss.str();}
#define read(a) scanf("%d",&a)
static const ll oo = 1LL<<62;
string solve(){
    ll totalLen;int n;cin>>totalLen>>n;
    set<ll> intermediate;
    vector<ll> boards;

    Rep(i,n) {
        ll a;cin>>a;
        if(intermediate.count(a)==0){
            intermediate.insert(a);
            boards.pb(a);
        }
    }

    int maxI = 0;
    For(i,1,n)if(boards[i]>boards[maxI])maxI=i;
    const int maxBoard = boards[maxI];
    boards.erase(boards.begin()+maxI);

    n=boards.size();

    set<ll> minLength;// for effective boards used
    minLength.insert(0);
    int prevCount=0;
    //debug(maxBoard);
    int goal = totalLen%maxBoard;

    int oldSize=0;
        set <ll> minKeys;
    for(int boardsUsed=0; ; ++boardsUsed){
        int total=0;
        set<ll> newLengths;
        //debug(boardsUsed);
        while(minLength.size()){
            ll cur = *minLength.begin();minLength.erase(minLength.begin());
           // debug(cur);
            if(cur>totalLen)break;
            ll key = cur%maxBoard;
            if(minKeys.count(key)){
                continue;
            }minKeys.insert(key);
            if(key==goal){
                return toString(totalLen/maxBoard + boardsUsed);
            }
            For(j,0,n){
                ll newLen = cur+boards[j];
                ((newLen%maxBoard <= key)?minLength:newLengths).insert(newLen);

            }
        }
        if(minKeys.size()<=oldSize)return "IMPOSSIBLE";
        oldSize=minKeys.size();
        minLength=newLengths;
    }
}

int main()
{
    freopen("test2.in","r",stdin); freopen("test2.out","w",stdout);

    int tt=0;cin>>tt;
    for(int caseNo=1;caseNo<=tt;++caseNo){

        string sol = solve();
        cout<<"Case #"<<caseNo<<": "<<sol<<    endl;
        cerr<<"Case #"<<caseNo<<": "<<sol<<    endl;
    }

    return 0;
}
