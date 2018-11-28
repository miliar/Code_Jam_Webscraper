#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;

char trans[250];
int tcase;
string str;
int main()
{
    freopen ("inputa.in","r",stdin);
    freopen ("outputa.out","w",stdout);
    trans['a'] = 'y';
    trans['b'] = 'h';
    trans['c'] = 'e';
    trans['d'] = 's';
    trans['e'] = 'o';
    trans['f'] = 'c';
    trans['g'] = 'v';
    trans['h'] = 'x';
    trans['i'] = 'd';
    trans['j'] = 'u';
    trans['k'] = 'i';
    trans['l'] = 'g';
    trans['m'] = 'l';
    trans['n'] = 'b';
    trans['o'] = 'k';
    trans['p'] = 'r';
    trans['q'] = 'z';
    trans['r'] = 't';
    trans['s'] = 'n';
    trans['t'] = 'w';
    trans['u'] = 'j';
    trans['v'] = 'p';
    trans['w'] = 'f';
    trans['x'] = 'm';
    trans['y'] = 'a';
    trans['z'] = 'q';
    cin >> tcase;
    getchar();
    FORN(t,tcase){
        getline(cin,str);
        cout << "Case #" << t+1 << ": ";
        FORN(i,str.length()){
            if (str[i] >= 'a' && str[i] <= 'z') {
                cout << trans[str[i]];
            }
            else cout << str[i];
        }
        cout << endl;
    }
    //system("pause");
    return 0;
}
//ASK Template Modified
