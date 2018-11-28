/*
 *      alpha.cpp
 */

using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define EPS 1e-11
#define inf ( 1LL << 31 ) - 1
#define LL long long

#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )
#define rrep( i, a, b ) for( __typeof(b) i = ( a ); i >= ( b ); --i )
#define xrep( i, a, b ) _rep( i, a, b, 1 )
#define foreach(it,a) for( typeof(( a ).begin()) it=( a ).begin();it!=( a ).end();it++)

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

typedef vector <int> vi;

//string S[3], T[3];
char sub[26];
char line[1024];


int main()
{
    #ifdef Local
        freopen("/home/wasi/Desktop/input.txt", "r", stdin);
        freopen("/home/wasi/Desktop/output.txt", "w", stdout);
    #endif    
    
    sub[0] = 'y';
    sub[1] = 'h';
    sub[2] = 'e';
    sub[3] = 's';
    sub[4] = 'o';
    sub[5] = 'c';
    sub[6] = 'v';
    sub[7] = 'x';
    sub[8] = 'd';
    sub[9] = 'u';
    sub[10] = 'i';
    sub[11] = 'g';
    sub[12] = 'l';
    sub[13] = 'b';
    sub[14] = 'k';
    sub[15] = 'r';
    sub[16] = 'z';
    sub[17] = 't';
    sub[18] = 'n';
    sub[19] = 'w';
    sub[20] = 'j';
    sub[21] = 'p';
    sub[22] = 'f';
    sub[23] = 'm';
    sub[24] = 'a';
    sub[25] = 'q';


    /*char sub[26];
    char line[1024];
    rep(i,3) 
    {
        gets(line);
        S[i] = line;
    }
    rep(i,3) 
    {
        gets(line);
        T[i] = line;
    }
    
    rep(i,3)
    {
        int len = sz(S[i]);
        rep(j,len) sub[S[i][j]-'a'] = T[i][j];
    }
    sub[16] = 'z';
    sub[25] = 'q';
    rep(i,26) cout<<"sub[" << i << "] = "<<sub[i] << ";" << endl;*/
    
    
    int t;
    gets(line);
    t = atoi(line);
    xrep(caseno, 1, t)
    {
        gets(line);
        int len = strlen(line);
        rep(i,len) 
        {
            if (line[i] == ' ') continue;
            line[i] = sub[line[i] - 'a'];
        }
        printf("Case #%d: %s\n", caseno, line);
    }
    
    return 0;
}
