#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <deque>
#include <vector>
#include <cstdlib>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <stack>
#include <set>
#include <functional>
#include <map>
#define eps 1e-8
using namespace std;

int main ()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    map <char, char> M;
    M[ 'a' ] = 'y';
    M[ 'b' ] = 'h';
    M[ 'c' ] = 'e';
    M[ 'd' ] = 's';
    M[ 'e' ] = 'o';
    M[ 'f' ] = 'c';
    M[ 'g' ] = 'v';
    M[ 'h' ] = 'x';
    M[ 'i' ] = 'd';
    M[ 'j' ] = 'u';
    M[ 'k' ] = 'i';
    M[ 'l' ] = 'g';
    M[ 'm' ] = 'l';
    M[ 'n' ] = 'b';
    M[ 'o' ] = 'k';
    M[ 'p' ] = 'r';
    M[ 'q' ] = 'z';
    M[ 'r' ] = 't';
    M[ 's' ] = 'n';
    M[ 't' ] = 'w';
    M[ 'u' ] = 'j';
    M[ 'v' ] = 'p';
    M[ 'w' ] = 'f';
    M[ 'x' ] = 'm';
    M[ 'y' ] = 'a';
    M[ 'z' ] = 'q';
    M[ ' ' ] = ' ';
    
    int N;
    while ( scanf("%d\n",&N)!=EOF )
    {
        for ( int Case = 1; Case<=N; Case++ )
        {
            string s;
            getline(cin,s);
            cout<<"Case #"<<Case<<": ";
            for ( int i=0; i<s.size(); i++ )
                cout<<M[ s[i] ];
            cout<<endl;
                
        }
    }
    return 0;
}

