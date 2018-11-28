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
#define MAX 1005000
#define mod(a,b) (((a)%(b) +(b))%(b))
bool notPrime[MAX+1];
vector<int> primes;
string solve(){
    int d,n;cin>>d>>n;
    ll vals[n];Rep(i,n)cin>>vals[i];
    if(n<=1)return "I don't know.";
    int curMax = 1;Rep(i,d)curMax*=10;
    set<ll> solutions;
    long long curMin = vals[0];
    For(i,1,n) curMin = max(vals[i],curMin);
    ForAll(it,primes){
        //debug(*it);
        if(*it>=curMax)break;
        if(*it <= curMin)continue;
        Rep(A,*it){
            int sol = mod((vals[1]-vals[0]*A) ,*it);

            bool good = true;
            For(i,2,n)
                if( mod((vals[i]-vals[i-1]*A) ,*it) !=sol){
                    good = false;break;
                }
            //debug(A);debug(good);
            if(good){
               // cerr<<A<<" "<<*it<<" "<<mod(vals[n-1]*A+sol,*it)<<endl;
                solutions.insert(mod(vals[n-1]*A+sol,*it));
                if(solutions.size()>1)return "I don't know.";
            }
        }

    }
            if(solutions.size()==1)return toString(*solutions.begin());
        cerr<<"WHAT???";
        return "I don't know.";
}

int main()
{
    freopen("test1.in","r",stdin); freopen("test1.out","w",stdout);

    for(int i=2; i*i<MAX;++i)
        if(not notPrime[i])
        {
            for(int j=i*i;j<MAX;j+=i){
                notPrime[j]=true;
            }
        }
    for(int i=2;i<MAX;++i)
        if(not notPrime[i])
            primes.pb(i);
    //cout<<primes.size()<<endl;

    int tt=0;cin>>tt;
    for(int caseNo=1;caseNo<=tt;++caseNo){

        cout<<"Case #"<<caseNo<<": ";
        cerr<<"Case #"<<caseNo<<": ";
        string sol = solve();
        cout<<sol<<  endl;
        cerr<<sol<<  endl;
    }

    return 0;
}
