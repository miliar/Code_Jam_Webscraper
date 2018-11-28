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
const bool ENABLE_MULTI_PROCESS = false;
using namespace std;

//=========================================================
// program:
//
char board[101][101];

int solve() {
    bool alive = true;
    int t = 0;
    char board2[101][101];
    while(alive) {
        alive = false;
        for (int i=0; i<101; i++) {
            for (int j=0; j<101; j++) {
                board2[i][j] = board[i][j];
                if(board[i][j]) {
                    alive = true;
                }
            }
        }
        if(! alive) break;

        for (int i=0; i<101; i++) {
            for (int j=0; j<101; j++) {
                bool up = ( (j>0) && board2[i][j-1] );
                bool left = ( (i>0) && board2[i-1][j] );
                if(up && left) {
                    board[i][j] = true;
                } else if ( (!up) && (!left) ) {
                    board[i][j] = false;
                } else {
                    board[i][j] = board2[i][j];
                }
            }
        }
        t++;

    }
    return t;
   
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
        int R;
        cin >> R;
        for (int i=0;i<101;i++) {
            for (int j=0;j<101;j++) {
                board[i][j] = false;
            }

        }
        for (int i=0; i<R; i++) {
            int x1,y1,x2,y2;
            cin >> x1 >> y1 >> x2 >> y2;
            assert(x2>=x1);
            assert(y2>=y1);
            for (int x=x1;x<=x2; x++) {
                for (int y=y1;y<=y2; y++) {
                    board[x][y] = true;
                }

            }
        }
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            int x = solve();
            
            /* output result goes here */
            cout<<"Case #"<<_i<<": "<<x<<endl;            
        }
        else if(mode!=2) break;
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
