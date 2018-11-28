#include <iostream>
#include <algorithm>
#include <vector>
using namespace __gnu_cxx;
#include <ext/hash_map>
using namespace std;
#define read(a) scanf("%d",&a)
#define For(i,a,b) for(int i =(a);i<(b);++i)
#define ForAll(it,set) for(typeof(set.begin()) it = set.begin();it!=set.end();++it)
typedef pair<int, int> pii;
namespace __gnu_cxx{template<>struct hash<pii>{
    size_t operator () (const pii&a) const{return a.first*15125123+a.second;}
    };};
typedef vector<int> vi;

hash_map<pii,bool> memoized;
bool canWin(int A, int B){
    //cout<<A<<" "<<B<<endl;
    if(A<B)swap(A,B);
    pii state = pii(A,B);
    hash_map<pii,bool>::iterator it = memoized.find(state);
    if(it != memoized.end())return it->second;

    if(B==0)return memoized[state]=true;

    int X = A%B;
    bool willWin = (not canWin(B,X));

   // cout<<A<<" "<<B<<" "<<willWin<<endl;
    if((not willWin) && X+B < A)
        willWin = true;//not canWin(X+B,B);
   // cout<<A<<" "<<B<<" "<<willWin<<endl;
    return memoized[state] = willWin;



}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int n;read(n);
    for(int times=1;times<=n;++times){
        int X1,X2,Y1,Y2;
        read(X1);read(X2);read(Y1);read(Y2);
        int total = 0;
        X2++,Y2++;
        For(y,Y1,Y2)
            For(x,X1,X2)
                if(canWin(x,y))++total;

        printf("Case #%d: %d\n",times,total);

    }
    return 0;
}
