#include <iostream>
#include <math.h>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <memory.h>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <stdio.h>
#include <assert.h>

using namespace std;
#define SET(a,n) memset(a,n,sizeof(a));
#define FOR(a,b,c) for(int a=b;a<c;++a)
#define GN(a) scanf("%d",&a)

typedef long long int LL;

using namespace std;

int main()
{
    freopen("i","r",stdin);
//    freopen("o.txt","w",stdout);

    map<char,char> m;
    m['A'] = 'Y';
    m['B'] = 'H';
    m['C'] = 'E';
    m['D'] = 'S';
    m['E'] = 'O';
    m['F'] = 'C';
    m['G'] = 'V';
    m['H'] = 'X';
    m['I'] = 'D';
    m['J'] = 'U';
    m['K'] = 'I';
    m['L'] = 'G';
    m['M'] = 'L';
    m['N'] = 'B';
    m['O'] = 'K';
    m['P'] = 'R';
    m['Q'] = 'Z';
    m['R'] = 'T';
    m['S'] = 'N';
    m['T'] = 'W';
    m['U'] = 'J';
    m['V'] = 'P';
    m['W'] = 'F';
    m['X'] = 'M';
    m['Y'] = 'A';
    m['Z'] = 'Q';

    m['a'] = 'y';
    m['b'] = 'h';
    m['c'] = 'e';
    m['d'] = 's';
    m['e'] = 'o';
    m['f'] = 'c';
    m['g'] = 'v';
    m['h'] = 'x';
    m['i'] = 'd';
    m['j'] = 'u';
    m['k'] = 'i';
    m['l'] = 'g';
    m['m'] = 'l';
    m['n'] = 'b';
    m['o'] = 'k';
    m['p'] = 'r';
    m['q'] = 'z';
    m['r'] = 't';
    m['s'] = 'n';
    m['t'] = 'w';
    m['u'] = 'j';
    m['v'] = 'p';
    m['w'] = 'f';
    m['x'] = 'm';
    m['y'] = 'a';
    m['z'] = 'q';

    char buffer[102];
    int t;
    cin>>t;
    getchar();
    FOR(test, 1, t + 1)
    {   cout<<"Case #"<<test<<": ";
        fgets(buffer, 102, stdin);
        int len = strlen(buffer);
        FOR(j,0,len)
        {
            if(buffer[j] == ' ')cout<<' ';
            else cout<<m[buffer[j]];
        }
        cout<<endl;
    }

    return 0;
}
