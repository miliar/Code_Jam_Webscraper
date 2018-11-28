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
int N;
char bot[100];
int  button[100];

int solve() {
    int ox = 1, ot = 0;
    int bx = 1, bt = 0;
    int t = 0;
    for (int i=0; i<N; i++) {
        if (bot[i] == 'O' ) {
            ot += abs(button[i] - ox)+1;
            ox = button[i];
            ot = std::max(ot, t+1);
            t = ot;
        } else {
            bt += abs(button[i] - bx)+1;
            bx = button[i];
            bt = std::max(bt, t+1);
            t = bt;
        }
        //cerr<<t<<"*"<<endl;
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
        cin >> N;
        for (int i=0; i<N; i++) {
            cin >> bot[i] >> button[i];
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
