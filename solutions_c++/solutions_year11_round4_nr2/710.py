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
#include<sys/stat.h> 

#define for_each(q,s) for(typeof(s.begin()) q=s.begin(); q!=s.end(); q++)
const bool ENABLE_MULTI_PROCESS = false;
using namespace std;

//=========================================================
// program:
//
char board[10][10];
int R, C, D;



int solve() {
    int best = 0;
    for (int a=0; a<R; a++) {
        for (int b=0; b<C; b++) {
            for (int k=3; k+a<=R && k+b<=C; k++) {
                int K = k;
                int weights[k][k];
                for (int x=0; x<K; x++) {
                    for (int y=0; y<K; y++) {
                        weights[x][y] = (board[a+x][b+y]-'0')+D;
                    }
                }
                weights[0][0] = 0;
                weights[k-1][0] = 0;
                weights[k-1][k-1] = 0;
                weights[0][k-1] = 0;
                if(K%2 == 1) {
                    int c = k/2;
                    int sy = 0;
                    int sx = 0; 
                    for (int x=0; x<K; x++) {
                        for (int y=0; y<K; y++) {
                            sy += weights[x][y]*(y-c);
                            sx += weights[x][y]*(x-c);
                        }
                    }
                    if( (sy==0) && (sx==0) ) {
                        best = max(best,k);
                    }
                } else {
                    int c = k - 1;
                    int sy = 0;
                    int sx = 0; 
                    for (int x=0; x<K; x++) {
                        for (int y=0; y<K; y++) {
                            sy += weights[x][y]*(2*y-c);
                            sx += weights[x][y]*(2*x-c);
                        }
                    }
                    if( (sy==0) && (sx==0) ) {
                        best = max(best,k);
                        /*if(k==2) {
                            for(int x=0; x<K; x++) {
                                for (int y=0; y<K; y++) {
                                    cout<<weights[x][y]<<" ";
                                }
                                cout<<endl;
                            }
                        }
                        cout<<endl;*/
                    }
                }
            }
        }
    }
    return best;
}

inline void init(){}
//=========================================================
// I/O:
//
int main(int argc, const char* argv[])
{
    int mode = 0;
    if(argc >= 2) sscanf(argv[1],"%d",&mode);
    if ( ( mode == 0 ) && ENABLE_MULTI_PROCESS )
    {
        string inputfile = ".input";
        system("cat > .input");
        /* I use a dual core CPU, so for long solutions I might use this
         multi-process thing, splitting the input in halves effectively
         halving execution time of slow solutions. But due to overhead it
         increases the time of fast solutions, so it is optional... */
        mode = 1;
        remove(".finished");
        cerr<<"--Multi process mode--"<<endl;
        //string inputfile = argv[2];
        string command = argv[0];
        command += " 2 < "+inputfile+" > .tem &";
        system(command.c_str());
        freopen(inputfile.c_str(),"r",stdin);
    }
    
    init();
    int TestCases;
    cin>>TestCases;

    for (int _i=1;_i<=TestCases;_i++)
    {
        /* read input goes here */
        cin >> R >> C >> D;
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                cin>>board[i][j];
            }
        }
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            int s = solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<": ";
            if (s==0) {
                cout<<"IMPOSSIBLE";
            } else {
                cout<<s;
            }
            cout<<endl;
        }
        else if(mode!=2) break;
        
        assert(cin);
    }
    if(mode==2) system("echo done > .finished");
    else if(mode==1)
    {
        struct stat stFileInfo;
        while( stat(".finished",&stFileInfo)!=0);
        system("cat .tem");

    }
    return 0;
}
