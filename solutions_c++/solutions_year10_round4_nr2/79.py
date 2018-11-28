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
int segTree[65536];
int M[65536];
hash_map<pii, int> memoized;

static const int inf = 1000000000;
int P;int teams;

int minCost(int bought,int i=1){
    pii state(bought,i);
    if(memoized.count(state))return memoized[state];
    if(i >= teams){
        int team = i-teams;
        int remaining=M[team]-bought;
        if(remaining<=0)return memoized[state]=0;
        return memoized[state]=inf;
    }
    int sol = inf;
    sol <?= (minCost(bought,i*2)+minCost(bought,i*2+1));
    sol <?= (segTree[i] + minCost(bought+1,i*2)+minCost(bought+1,i*2+1));
//debug(bought);debug(i);debug(sol);
    return memoized[state]= sol;

}

//problem 2
int main()
{
    freopen("test2.in","r",stdin); freopen("test.out","w",stdout);

    int tt=0;cin>>tt;
    for(int caseNo=1;caseNo<=tt;++caseNo){
        cin>>P;
        teams = (1<<P);
        memoized.clear();
        For(i,0,teams){
            cin>>M[i];
            M[i]=P-M[i];
        }
        for(int size=teams; size/=2; ){
            For(i,0,size)cin>>segTree[size+i];
        }

        cout<<"Case #"<<caseNo<<": "<<  minCost(0)<<  endl;
        cerr<<"Case #"<<caseNo<<": "<<  minCost(0)<<  endl;
    }

    return 0;
}
