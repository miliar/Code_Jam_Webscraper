#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vp;
typedef vector<vi> vvi;

const int N = 100010;
const int M = 55;
const int K = 200010;
const int LIT = 2500;
const int INF = 1 << 30;
const int ABS(int x) {while(x < 0) x = -x; return x;}

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

char dic[] = {
'a','y',
'b','h',
'c','e',
'd','s',
'e','o',
'f','c',
'g','v',
'h','x',
'i','d',
'j','u',
'k','i',
'l','g',
'm','l',
'n','b',
'o','k',
'p','r',
//-------------------
'q','z',
//-------------------
'r','t',
's','n',
't','w',
'u','j',
'v','p',
'w','f',
'x','m',
//-------------------
'y','a',
'z','q'
//-------------------
  
};

map<char, char> d;
char s[333];

void init()
{
    for(int i = 0; i < 52; i += 2)
    {
        d[dic[i]] = dic[i+1];
    }
}

void solve(int tcase)
{
    
    printf("Case #%d: ", tcase);
    for(int i = 0; i < strlen(s); i++)
    {
        char c = s[i];
        if(d.find(c) == d.end()) printf("%c", c);
        else printf("%c", d[c]);
    }
    printf("\n");
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    init();
    
    int T;
    cin>>T; getchar();
    
    for(int i = 1; i <= T; i++)
    {
        gets(s);
        solve(i);
    }
    
    /*while(cin>>s1>>s2)
    {
        getmap();
    }
    for(map<char, char>::iterator itr = dic.begin(); itr != dic.end(); itr++)
    {
        printf("%c %c\n", itr->fst, itr->snd);    
    }*/
    
    //while(1);
}
