#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <ctime>
#include <math.h>
#include <algorithm>
#include <iomanip>
#include <assert.h>
#include <map>
#include <queue>
#include <cstring>
#include <set>
using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;
#define vi vector<int>
#define vvi vector< vector<int> >
#define vd vector<double>
#define vb vector<bool>
#define vs vector<string>
#define pi pair<int,int>
#define pb push_back
#define out(a) cout<<(a)<<endl
#define pout(a,b) cout<<(a)<<' '<<(b)<<endl
#define sz(c) (int)(c).size()
#define foreach(n,i) for(int (i)=0;(i)<(n);(i)++)
#define range(s,e,i) for(int (i)=(s);(i)<=(e);(i)++)
#define all(c) (c).begin(),(c).end()
template<typename typ> void vout(vector<typ>& v){for(int vint=0;vint<sz(v);vint++)cout<<(v)[vint]<<' ';cout<<endl;}
template<typename typ> void arrout(typ* arr,int l){for(int i=0;i<l;i++)cout<<arr[i]<<' ';cout<<endl;}

#define debug
#ifdef debug
#define dbg(a) cout << #a << ' ' << a << endl
#endif
#ifndef debug
#define dbg(a)
#endif

int main()
{
    int t;
    cin >> t;
    for(int T = 1 ; T <= t ; ++T)
    {
        printf("Case #%d: ",T);
        string board[4];
        bool end = false;
        for(int i = 0 ; i < 4 ; ++i)
            cin >> board[i];
        for(int i = 0 ; i < 4 ; ++i)
        {
            bool found = true;
            char row = ( (board[i][0] == 'T') ? board[i][1] : board[i][0] );
            if( row == '.' )
                continue;
            for(int j = 0 ; j < 4 ; ++j)
            {
                if( board[i][j] != row && board[i][j] != 'T' )
                    found = false;
            }
            if( found && !end )
            {
                printf("%c won\n",row);
                end = true;
                break;
            }
        }
        if( end )
            continue;
        end = false;
        for(int j = 0 ; j < 4 ; ++j)
        {
            bool found = true;
            char col = ( (board[0][j] == 'T') ? board[1][j] : board[0][j] );
            if( col == '.' )
                continue;
            for(int i = 0 ; i < 4 ; ++i)
                if( board[i][j] != col && board[i][j] != 'T' )
                    found = false;
            if( found && !end )
            {
                printf("%c won\n",col);
                end = true;
                break;
            }
        }
        if( end )
            continue;
        bool found_diag = true,found_anti = true;
        char diag = ( (board[0][0] == 'T') ? board[1][1] : board[0][0]);
        char anti_diag = ( (board[0][3] == 'T') ? board[1][2] : board[0][3] );
        for(int i = 0 ; i < 4 && diag != '.' ; ++i)
        {
            if( board[i][i] != diag && board[i][i] != 'T' )
                found_diag = false;
        }

        for(int i = 0 ; i < 4 && anti_diag != '.' ; ++i)
        {
            if( board[i][3 - i] != anti_diag && board[i][3 - i] != 'T' )
                found_anti = false;
        }
        if( found_diag && diag != '.' )
            printf("%c won\n",diag);
        else if( found_anti && anti_diag != '.' )
            printf("%c won\n",anti_diag);
        else
        {
            end = false;
            for(int i = 0 ; i < 4 ; ++i)
                for(int j = 0 ; j < 4 ; ++j)
                    if( board[i][j] == '.' )
                        end = true;
            if( end )
                printf("Game has not completed\n");
            else
                printf("Draw\n");
        }
    }
}