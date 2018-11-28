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
int D,I,M,N;
int vec[100];
int mem[256][100][3];
const int INF = 255500000;

const int NOT_ADDED = 0;
const int ADDED_INC = 1;
const int ADDED_DESC = 2;
int rec(int x, int p, int added) {
    int & res  = mem[x][p][added];
    if( res != -1) {
        return res;
    }
    res = INF;
    //note: do not have any more returns:
    if( p == N) {
        //hmnn, we want this number to be x... but there is no number!, but in
        // fact, "" is smooth, so...
        res = 0;
    } else {
        //try removing the current number
        res = std::min( res , D + rec(x,p+1, NOT_ADDED) );
        
        //pick the wanted next value:
        for (int nx=0; nx<=255; nx++) {
            if( std::max(x-nx, nx-x) <= M) {
                //try modifying the current number at p to be x
                res = std::min(res, std::max(x - vec[p], vec[p] - x) + rec(nx, p+1, NOT_ADDED) );
                
                //try inserting x instead. This is tricky.
                if( added == NOT_ADDED ) {
                    if(nx > x) {
                        res = std::min(res, I + rec(nx, p, ADDED_INC) );
                    } else if (nx < x ) {
                        res = std::min(res, I + rec(nx, p, ADDED_DESC) );
                    }
                    //makes no sense to add x again and then expect another x...
                } else if( (added == ADDED_INC) && (nx > x) ) {
                    res = std::min(res, I + rec(nx, p, ADDED_INC) );
                } else if( (added == ADDED_DESC) && (nx < x) ) {
                    res = std::min(res, I + rec(nx, p, ADDED_DESC) );
                }
            }
        }
    }
    
    return res;
}

int solve() {
    memset( mem, -1, sizeof(mem) );
    int res = D * N; //remove all elements.
    for (int i=0; i<256; i++) {
        res = std::min(res,rec(i,0, NOT_ADDED));
    }
    
    
    return res;
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
        cin >> D >> I >> M >> N;
        for (int j=0; j<N; j++) {
            cin >> vec[j];
        }
        cerr<<"["<<i<<" / "<<C<<"]"<<endl;
        cout<<"Case #"<<i<<": " <<solve()  << endl;
        
    }
    return 0;
}
