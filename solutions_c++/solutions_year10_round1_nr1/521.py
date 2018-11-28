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
int K, N;
char board[50][51];

int dx[4] = { 1,0,1,1};
int dy[4] = { 0,1,1,-1};

int find(char ch) {
    for (int i=N;i--;) {
        for (int j=N;j--;) {
            for (int t=4; t--;) {
                bool good = true;
                int x = i, y = j;
                for (int r=1; r<=K; r++) {
                    good &= ( (x<N) && (y<N) && (x>=0) && (y>=0) && (board[x][y]==ch) );
                    x += dx[t];
                    y += dy[t];
                }
                if( good) {
                    //cout<<ch<<" good at "<<i<<", "<<j<<endl;
                    return 1;
                }
            }
        }

    }
    return 0;
}

int solve()
{
    for (int i=N; i--;) {
        int t = N-1;
        for (int j = N; j--; ) {
            if( board[i][j] != '.' ) {
                board[i][t--] = board[i][j];
            }
        }
        for (int j = t; j>=0; j--) {
            board[i][j] = '.';
        }
        board[i][N] = '\0';
        //cout<<board[i]<<endl;
        
    }
    return (find('R') | (find('B')<<1) );
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
        cin >> N >> K;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                cin >> board[i][j];
            }
        }
        
        cerr<<"["<<i<<" / "<<C<<"]"<<endl;
        cout<<"Case #"<<i<<": "   ;
        int m = solve();
        
        if( m==1 ) {
            cout<<"Red";
        } else if (m==2) {
            cout<<"Blue";
        } else if( m==3) {
            cout <<"Both";
        } else {
            cout<<"Neither";
        }
        cout<<endl;
        
    }
    return 0;
}
