
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

const int inf = (1<<28);
const double pi = (2.0*acos(0.0));
const double eps = 1e-9;

#define _rep( i, a, b, x ) for( i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )

#define pb push_back

string s[3],t[3];
char mp[30];

char line[200];
int main(void)
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k,kase=0;
    int t;
    mp[0] = 'y';
    mp[1] = 'h';
    mp[2] = 'e';
    mp[3] = 's';
    mp[4] = 'o';
    mp[5] = 'c';
    mp[6] = 'v';
    mp[7] = 'x';
    mp[8] = 'd';
    mp[9] = 'u';
    mp[10] = 'i';
    mp[11] = 'g';
    mp[12] = 'l';
    mp[13] = 'b';
    mp[14] = 'k';
    mp[15] = 'r';
    mp[16] = 'z';
    mp[17] = 't';
    mp[18] = 'n';
    mp[19] = 'w';
    mp[20] = 'j';
    mp[21] = 'p';
    mp[22] = 'f';
    mp[23] = 'm';
    mp[24] = 'a';
    mp[25] = 'q';

    scanf("%d",&t);gets(line);
    while(t--)
    {
        printf("Case #%d: ",++kase);
        gets(line);
        int sz = strlen(line);
        rep(i,sz)
        {
            if(line[i]==' ') printf(" ");
            else printf("%c",mp[line[i]-'a']);
        }
        printf("\n");
    }

    /*char line[30];
    rep(i,3)
    {
        gets(line);
        s[i] = (string) line;
    }
    rep(i,3)
    {
        gets(line);
        t[i]=(string) line;
    }
    rep(i,27) mp[i]='.';
    rep(i,3)
    {
        rep(j,(int)s[i].size())
        {
            if(s[i][j] == ' ') continue;
            if(mp[s[i][j]-'a'] == '.')
                mp[s[i][j]-'a'] = t[i][j];
        }
    }
    rep(i,26)
        printf("mp[%d] = '%c';\n",i,mp[i]);*/
    return 0;
}
