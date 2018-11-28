#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <iterator>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define FOR(x,b,e) for(x=b; x<e; ++x)

#define SUBMIT
#ifdef SUBMIT
#   define _DSP(X)
#else
#   define _DSP(X) X
#   define DV(Var) #Var<<"="<<Var<<' '
#endif

const int N=4;
char m[N][N];
char c[N];

bool check0_(const char a[], char ch)
{
    for(int i=0; i<N;++i)
        if(a[i]!=ch && a[i]!='T') return false;
    return true;
}
bool check0(const char a[], char ch)
{
    bool chk=check0_(a,ch);
    _DSP(cerr<<DV(chk)<<endl;)
    return chk;
}
bool check(char ch)
{int i,j;
    for(i=0;i<N;++i)
        if(check0(m[i],ch))return true;
    for(j=0;j<N;++j)
    {
        FOR(i,0,N)
            c[i]=m[i][j];
        if(check0(c,ch)) return true;
    }
    FOR(i,0,N)c[i]=m[i][i];
    if(check0(c,ch))return true;
    FOR(i,0,N)c[i]=m[N-i-1][i];
    if(check0(c,ch))return true;
    return false;
}
bool full()
{
    int i,j;
    FOR(i,0,N)
        FOR(j,0,N)
            if(m[i][j]=='.')return false;
    return true;
}

int main()
{
    int T;cin>>T;cin.ignore();
    for(int t=1;t<=T;++t)
    {int i;
        for(i=0;i<N;++i)
            scanf("%s",m+i);
        bool xwin=check('X');
        bool owin=check('O');
        const char *ans=
            xwin?
                owin?
                    "CNM"
                    :"X won"
                :owin?
                    "O won"
                    :full()?
                        "Draw"
                        :"Game has not completed";

        cout<<"Case #"<<t<<": "
            <<ans
            <<endl;
    }

    return 0;
}

