#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <string>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>

#define NAME_VAL(a) cerr<<#a<<" = "<<(a)<<endl;
#define SWAPi(a,b) { int t=a;a=b;b=t; }
#define SWAPd(a,b) { double t=a;a=b;b=t; }
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define FORab(i,a,b) for(i=(a);i<=(b);i++)
#define FOR(i,n) FORab(i,0,(n)-1)
#define FOR1(i,n) FORab(i,1,n)

using namespace std;

void preprocess()
{

}

void main2(int cc) {
    int r,c,i,j,k;
    char board[60][60];
    cin>>r>>c;
    FOR(i,r)
    {
        cin>>board[i];
    }

    bool flag=true;

    FOR(i,r)
    {
        FOR(j,c)
        {
            if(board[i][j]=='#')
            {
                if(i<r-1 && j<c-1 && board[i][j+1]=='#'
                   && board[i+1][j]=='#'
                   && board[i+1][j+1]=='#')
                {
                    board[i][j]='/';
                    board[i][j+1]='\\';
                    board[i+1][j]='\\';
                    board[i+1][j+1]='/';
                }
                else
                {
                    flag=false;
                    break;
                }
            }
        }
        if(flag==false) break;
    }
    cout<<endl;
    if(flag)
    {
        FOR(i,r) cout<<board[i]<<endl;
    }
    else
    {
        cout<<"Impossible"<<endl;
    }
}

int main() {
    int c,cases;
    preprocess();
    cin>>cases;
    FOR1(c,cases) {
        cout<<"Case #"<<c<<": ";
        main2(c);
    }
    return 0;
}
