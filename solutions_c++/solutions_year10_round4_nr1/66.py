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
typedef hash_map<point,int> grid;
#define dist(x,y,a,b) (abs(a-x)+abs(b-y))
//problem 1

int main()
{
    freopen("test1.in","r",stdin); freopen("test.out","w",stdout);

    int tt=0;cin>>tt;
    for(int caseNo=1;caseNo<=tt;++caseNo){
        int k;cin>>k;//debug(k);
        int width = k-1;
        grid diamond;
        for(int y = -width; y <= width;++y){
            int xBound = (width-abs(y));
            for(int x = -xBound; x <= xBound;x+=2){
                cin>>diamond[point(x,y)];

               // debug(diamond[point(x,y)]);
            }
        }
        int bestW = 0x7fffffff;
        for(int y = -width; y <= width;++y){
            for(int x = -width; x<= width;++x){
                int newW = 0;

                newW>?= dist(x,y,width,0);
                newW>?= dist(x,y,-width,0);
                newW>?= dist(x,y,0,-width);
                newW>?= dist(x,y,0,width);
                grid next = diamond;
                bool good = true;
                if(newW < bestW){
                    for(int dy = -newW; good&&dy <= newW;++dy){
                        int xBound = (newW-abs(dy));
                        for(int dx = -xBound; dx <= xBound;++dx){
                            //debug(dx);debug(dy);
                            For(i,0,2){
                                point a(x+dx,y+dy),b(x+((i==0)?dx:-dx),y+((i==1)?dy:-dy));
                                grid::iterator ait =next.find(a),bit =next.find(b);
                                bool knowA = ait!=next.end(),knowB=bit!=next.end();
                                if(not knowA && not knowB)continue;
                                if(knowA and knowB){
                                    if(ait->second != bit->second){
                                        good=false;
                                    }
                                }
                                else if (knowA){
                                    next[b]= ait->second;
                                }
                                else if(knowB)
                                    next[a]=bit->second;
                            }
                        }
                    }
                    if(good)bestW=newW;
                }
            }
        }

        int realW = k-1;
       // debug(realW);debug(bestW);
        int solution = (bestW+1)*(bestW+1)-(realW+1)*(realW+1);
        cout<<"Case #"<<caseNo<<": "<< solution<<   endl;
        cerr<<"Case #"<<caseNo<<": "<< solution<<   endl;
    }


    return 0;
}
