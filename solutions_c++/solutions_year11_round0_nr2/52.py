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
int C;
char base1[36];
char base2[36];
char result[36];
int D;
char opos1[28];
char opos2[28];
int N;
string spells;


string solve() {
    string contents = "";
    char transition[26][26];
    memset(transition, '#', sizeof(transition));
    bool opposed[26][26];
    memset(opposed, 0, sizeof(opposed));
    
    for (int i=0; i<C; i++) {
        int a = base1[i]-'A';
        int b = base2[i]-'A';
        transition[a][b] = transition[b][a] = result[i];
    }
    for (int i=0; i<D; i++) {
        int a = opos1[i]-'A';
        int b = opos2[i]-'A';
        opposed[a][b] = opposed[b][a] = true;
    }
    for(int i = 0; i<spells.size(); i++) {
        if (contents == "" ) {
            contents += spells[i];
        } else {
            //transition?
            char cur = spells[i];
            int x = cur-'A';
            char ls =  *contents.rbegin();
            char & r = transition[ls-'A'][x];
            if ( r != '#' ) {
                contents.resize( contents.size()-1);
                contents += r;
            } else {
                //opposed?
                bool op = false;
                for_each(ch, contents) {
                    op |= opposed[*ch-'A'][x];
                }
                if (op) {
                    contents = "";
                } else {
                    //not opposed
                    contents += cur;
                }
            }
        }
    }
    
    
    return contents;
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
        cin >> C;
        for (int i=0; i<C; i++) {
            cin >> base1[i] >> base2[i] >> result[i];
        }
        cin >> D;
        for (int i=0; i<D; i++) {
            cin >> opos1[i] >> opos2[i];
        }
        int n;
        cin >> n;
        cin >> spells;
        
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            string x = solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<": ";
            cout<<"[";
            for (int i=0; i<x.size(); i++) {
                if(i!=0) {
                    cout<<", ";
                }
                cout<<x[i];
            }
            cout<<"]"<<endl;
            
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
