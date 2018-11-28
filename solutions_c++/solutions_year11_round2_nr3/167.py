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
int N, M;
int U[3600];
int V[3600];


int polyn;
int poly[1<<8];

int currentcolors = 0;
int res[8];

int vec[8];
void backtrack(int x, int cn) {
    if ( x == N) {
        
        for (int i=0; i<polyn; i++) {
            set<int> st;
            for (int j = 0; j < N; j++) {
                if ( poly[i] & (1<<j) ) {
                    st.insert( vec[j] );
                }
            }
            if ( st.size() != cn ) {
                return;
            }
        }
        // good !
        if ( cn > currentcolors ) {
            currentcolors = cn;
            for (int i=0; i<N; i++) {
                res[i] = vec[i];
            }
        }
        return;
    }
    for (int i=1; i<=cn; i++) {
        vec[x] = i;
        assert(vec[x] != 0);
        backtrack(x+1, cn);
    }
    vec[x] = cn+1;
    assert(vec[x] != 0);
    backtrack(x+1, cn+1);
    
}

void solve() {
    for (int i=0; i<N; i++) {
        U[M] = i;
        V[M++] = (i+1) % N;
    }
    int m = 0;
    for (int i=0; i<m; i++) {
        U[M] = U[i];
        V[M++] = V[i];
    }
    
    currentcolors = 0;
    polyn = 0;
    for (int mask=0; mask<(1<<N); mask++) {
        //does a room exist between the points in mask?
        int t = 0;
        for (int i=0; i<N; i++) {
            if ( mask & (1<<i) ) {
                t++;
            }
        }
        if(t<3) continue;
        //cout<<"*"<<endl;
        for (int i=0; i<M; i++) {
            if ( (mask&(1<<U[i])) && (mask&(1<<V[i])) ) {
                //cout<<U[i]<<" -> "<<V[i]<<endl;
                t--;
            }
        }
        if ( t== 0 ) {
            poly[polyn++] = mask;
        }
    }
    //cout<<"polyn = "<<polyn<<endl;
    backtrack(0, 0);
    assert(currentcolors != 0);
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
        cin >> N >> M;
        int x[M], y[M];
        for (int i=0; i<M; i++) {
            cin >> x[i];
        }
        for (int i=0; i<M; i++) {
            cin >> y[i];
        }
        for (int i=0; i<M; i++) {
            U[i] = x[i]-1;
            V[i] = y[i]-1;
        }
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<": "<<currentcolors<<endl;
            for (int i=0; i<N; i++) {
                if ( i ) cout<<" ";
                cout<<res[i];
            }
            cout<<endl;
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
