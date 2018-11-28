#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>
#include<functional>
#include<set>
#include<stack>
#include<cstdlib>
#include<cstring>


using namespace std;

//=========================================================
// program:
//
bool solve2(long long N, long long K) {
    long long cyc = (1ll<<(N) );
    return ( K % cyc >= (cyc/2) );
}

bool solve(long long N, long long K) {
    for (int i=1; i<=N; i++) {
        if( ! solve2(i,K) ) {
            return false;
        }
    }
    return true;
}


inline void init(){}
//=========================================================
// I/O:
//
int main()
{
    init();
    int C; cin>>C;
    for (int i=1;i<=C;i++)
    {
        cerr<<"["<<i<<" / "<<C<<"]"<<endl;
        
        int N, K;
        cin >> N >> K;
        cout<<"Case #"<<i<<": " <<( solve(N,K) ? "ON" : "OFF" )  << endl; 
        
    }
    return 0;
}
