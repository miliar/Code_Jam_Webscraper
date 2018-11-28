// Much better than B, which blows, because big nums blow.

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
int R, k;
int N;
int group[1000];

long long sim_to  [28][1000];
long long sim_wins[28][1000];

long long solve() {
    //fill sim_to[0], sim_wins[0]
    for (int i=0; i<N; i++) {
        int x = 0;
        int y = i;
        int e = (i-1+N)%N;
        
        sim_wins[0][i] = 0;
        while (true) {
            //cout<<"\t"<<sim_wins[0][i]<<endl;
            if( sim_wins[0][i] + group[y] > k ) {
                //can't enter
                break;
            }
            sim_wins[0][i] += group[y];
            if( y == e ) {
                y = (y+1) % N;
                break;
            } else {
                y = (y+1) % N;
            }            
        }
        sim_to[0][i] = y;
    }
    for (int i=1; i<28; i++) {
        for (int j=0; j<N; j++) {
            int to1 = sim_to[i-1][j];
            long long w = sim_wins[i-1][j];
            sim_to[i][j] = sim_to[i-1][to1];
            sim_wins[i][j] = w + sim_wins[i-1][to1];
            //if( (1<<i) <= R ) cout<<"*From "<<j<<" to "<<sim_to[i][j]<<" = "<<sim_wins[i][j]<<" in "<<(1<<i)<<" steps"<<endl;
        }
    }
    //position:
    int x = 0, t = 0;
    long long w = 0;
    while(R > 0) {
        if( R % 2 ) {
            //cout<<"From "<<x<<" to "<<sim_to[t][x]<<" = "<<sim_wins[t][x]<<" in "<<(1<<t)<<" steps"<<endl;
            w += sim_wins[t][x];
            x = sim_to[t][x];
        }
        R >>= 1;
        t ++;
    }
    return w;
    
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
        cin >> R >> k >> N;
        for (int i=0; i<N; i++) {
            cin >> group[i];
        }
        cout<<"Case #"<<i<<": " << solve() << endl; 
        
    }
    return 0;
}
