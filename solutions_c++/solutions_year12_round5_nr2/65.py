#ifdef VX_PRECOMPILED
#include "precomp.h"
typedef mpz_class big;
#else
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
#include<numeric>
#include<cstdio>
#include<cstdlib>
#include<cstring>
// http://gmplib.org/ (uncomment if solution does not use big nums)
#include "gmpxx.h"
#define big mpz_class
#endif

#define for_each(q,s) for(typeof(s.begin()) q=s.begin(); q!=s.end(); q++)
typedef long long int64;
#define long int64
const bool ENABLE_MULTI_PROCESS = true;
using namespace std;

//=========================================================
// program:
//
int S;
int M;
int x[100], y[100];

int T;
char board[199][199];
int border[199][199];

int dx[6] = {-1,-1, 0,0, 1,1 };
int dy[6] = {0, -1,-1,1, 0,1 };

bool isRing()
{
    int visited[T][T];
    memset(visited,0 , sizeof(visited));
    queue<int> Q;
    for (int i=0; i<T; i++) {
        for (int j=0; j<T; j++) {
            if ( (border[i][j] != 0) && (board[i][j] == '.') ) {
                visited[i][j] = true;
                Q.push(i);
                Q.push(j);
            }
        }
    }
    while (! Q.empty()) {
        int x = Q.front(); Q.pop();
        int y = Q.front(); Q.pop();
        for (int d=0; d<6; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            if ( nx>=0  && ny >= 0 && nx < T && ny < T && (board[nx][ny]=='.') && !visited[nx][ny]) {
                visited[nx][ny] = true;
                Q.push(nx);
                Q.push(ny);
            }
        }
    }
    bool ring = false;
    for (int i=0; i<T; i++) {
        for (int j=0; j<T; j++) {
            if ( (border[i][j] == 0) && (board[i][j] == '.') && ! visited[i][j]) {
                board[i][j] = '%';
                ring = true;
            }
        }
    }
    if (ring) {
        return true;
    }
    return false;    
}
bool bridgevisited[200][200];
void bridgedfs(int x, int y)
{
    bridgevisited[x][y] = true;
    for (int d=0; d<6; d++) {
        int nx = x + dx[d];
        int ny = y + dy[d];
        if ( nx>=0  && ny >= 0 && nx < T && ny < T && (board[nx][ny]=='*') && !bridgevisited[nx][ny]) {
            bridgedfs(nx,ny);
        }
    }
}
bool isBridge()
{
    memset(bridgevisited, 0, sizeof(bridgevisited));
    for (int i=0; i<T; i++) {
        for (int j=0; j<T; j++){
            if ( (__builtin_popcount(border[i][j]) >= 2) && (board[i][j]=='*') ) {
                if (bridgevisited[i][j]) {
                    return true;
                }
                bridgedfs(i,j);
            }
        }
    }
    return false;
}
bool forkvisited[200][200];
void forkdfs(int x, int y)
{
    forkvisited[x][y] = true;
    for (int d=0; d<6; d++) {
        int nx = x + dx[d];
        int ny = y + dy[d];
        if ( nx>=0  && ny >= 0 && nx < T && ny < T && (board[nx][ny]=='*') && !forkvisited[nx][ny]) {
            forkdfs(nx,ny);
        }
    }
}

bool isFork(bool debug = false)
{
    memset(forkvisited, 0, sizeof(forkvisited));
    bool ignore[200][200];
    memset(ignore, 0, sizeof(ignore) );
    vector<int> borderPos[6];
    for (int i=0; i<T; i++) {
        for (int j=0; j<T; j++)  {
            if (board[i][j] == '*') {
                if (__builtin_popcount(border[i][j]) != 1) {
                    continue;
                }
                for (int b=0; b<6; b++) if (border[i][j] &( 1<<b)) {
                    borderPos[b].push_back(i);
                    borderPos[b].push_back(j);
                }
            }
        }
    }
    for (int b=0; b<6; b++) {
        for (int i=0; i<borderPos[b].size(); i+=2) {
            forkdfs( borderPos[b][i], borderPos[b][i+1] );
            int c = 0;
            
            vector<int> meh;
            for (int a=b+1; a<6; a++) {
                bool counta = true;
                for (int i=0; i<borderPos[a].size(); i+=2) {
                    int x = borderPos[a][i];
                    int y = borderPos[a][i+1];
                    if ( !ignore[x][y] && forkvisited[ x ][ y ] ) {
                        ignore[x][y] = true;
                        c += counta;
                        counta = false;
                    }
                }
            }
            if (c >= 2) {
                return true;
            }
        }
        /*if (debug) {
            for (int i=0; i<T; i++) {
                            for (int j=0; j<T; j++) {
                                cout << ( forkvisited[T-j-1][i] ? (b+1) :0 );
                            }
                            cout << endl;
                        }
                        cout<<endl;
        }*/

    }
    return false;

}

string solve() {
    T = S*2 - 1;
    memset(border, 0, sizeof(border));
    memset(board, '.', sizeof(board));
    int p=0, q=T-1;
    for (int aa=S-1; aa>=0; aa--) {
        for (int i=0; i<aa; i++) {
            board[q][i] = '#';
            board[p][T-i-1] = '#';
        }
        border[q][aa] |= (1<<2);
        border[p][T-aa-1] |= (1<<5);
        p++;
        q--;
    }
    for (int i=0; i<T; i++) {
        if (board[0][i] != '#') {
            border[0][i] |= (1<<0);
        }
        if (board[T-1][i] != '#') {
            border[T-1][i] |= (1<<3);
        }
        if (board[i][0] != '#') {
            border[i][0] |= (1<<1);
        }
        if (board[i][T-1] != '#') {
            border[i][T-1] |= (1<<4);
        }
    }
            /*for (int i=0; i<T; i++) {
                for (int j=0; j<T; j++) {
                    int t = __builtin_popcount(border[T-j-1][i]);
                    if (t == 2) {
                        cout << "C";
                    } else if (t==1) {
                        for (int b=0; b<6; b++) if (border[T-j-1][i] & (1<<b)) {
                            cout << b;
                        }
                    } else {
                        cout << '.';
                    }
                    
                }
                cout << endl;
            }*/
    
    for (int i=0; i<M; i++) {
        board[ x[i]-1][ y[i] - 1] = '*';
        bool br = isBridge();
        bool fo = isFork( (i==4) );
        bool ri = isRing();
        if (br || fo ||ri) {
            /*board[ x[i]-1][ y[i] - 1] = '@';
            for (int i=0; i<T; i++) {
                for (int j=0; j<T; j++) {
                    cout << board[T-j-1][i];
                }
                cout << endl;
            }*/
            
            
            string res = "";
            ostringstream st;
            
            if (br) {
                st<< "-bridge";
            }
            if (fo) {
                st<< "-fork";
            }
            if (ri) {
                st<< "-ring";
            }
            st << " in move " << (i+1);
            string s = st.str();
            return s.substr(1);
        }
    }
            /*for (int i=0; i<T; i++) {
                for (int j=0; j<T; j++) {
                    cout << board[T-j-1][i];
                }
                cout << endl;
            }*/
    
    return "none";
}

inline void init(){}
//=========================================================
// I/O:
//
void run(const char* x)
{
    int r = system(x);
    cerr<<x<<" "<<"("<<r<<")"<<endl;
}
int main(int argc, const char* argv[])
{
    int mode = 0;
    if(argc >= 2) sscanf(argv[1],"%d",&mode);
    if ( ( mode == 0 ) && ENABLE_MULTI_PROCESS )
    {
        string inputfile = ".input";
        run("cat > .input");
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
        run(command.c_str());
        assert( freopen(inputfile.c_str(),"r",stdin) );
    }
    
    init();
    int TestCases;
    cin>>TestCases;

    for (int _i=1;_i<=TestCases;_i++) {
        /* read input goes here */
        cin >> S >> M;
        for (int i=0; i<M; i++) {
            cin >> x[i] >> y[i];
        }
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) ) {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            string res = solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<": "<<res<<endl;            
        }
        else if(mode!=2) break;
        
        assert(cin);
    }
    if(mode==2) {
        run("echo done > .finished");
    } else if(mode==1) {
        struct stat stFileInfo;
        while( stat(".finished",&stFileInfo)!=0);
        run("cat .tem");
    }
    return 0;
}
