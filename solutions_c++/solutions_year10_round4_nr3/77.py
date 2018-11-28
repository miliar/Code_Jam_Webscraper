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
typedef pair<int,int> point;
#define x first
#define y second
typedef hash_set<point> grid;

//problem 3
int main()
{
    freopen("test3.in","r",stdin); freopen("test.out","w",stdout);

    int tt=0;cin>>tt;
    for(int caseNo=1;caseNo<=tt;++caseNo){
        int n;
        cin>>n;
        grid g;
        For(i,0,n){
            int x1,y1,x2,y2;
            cin>>x1>>y1>>x2>>y2;
            if(x1>x2)swap(x1,x2);
            if(y1>y2)swap(y1,y2);
            For(x,x1,x2+1)
                For(y,y1,y2+1)
                    g.insert(point(x,y));

          //  debug(i);
        }
        int solution = 0;
        for(;g.size();++solution){
            //debug(solution);
            grid next;
            ForAll(it,g){
                point p=*it;
                if(g.count(point(p.x,p.y-1))||g.count(point(p.x-1,p.y)))
                    next.insert(p);
                if(g.count(point(p.x+1,p.y-1)))
                    next.insert(point(p.x+1,p.y));
            }
            g=next;
        }

        cout<<"Case #"<<caseNo<<": "<<solution<< endl;
        cerr<<"Case #"<<caseNo<<": "<<solution<< endl;

    }

    return 0;
}
