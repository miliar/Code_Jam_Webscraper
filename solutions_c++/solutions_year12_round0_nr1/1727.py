#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
using namespace std;

typedef pair<int,int> ii;
typedef long long LL;
typedef vector <int> vi;

#define INF 2000000000
#define PI 3.14159265

#define FOR(i,a,n) for(int i=a,_n=n; i<_n; ++i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

char conv(char x){
     if ( x == 'a' ) return 'y';
    if ( x == 'b' ) return 'h';
    if ( x == 'c' ) return 'e';
    if ( x == 'd' ) return 's';
    if ( x == 'e' ) return 'o';
    if ( x == 'f' ) return 'c';
    if ( x == 'g' ) return 'v';
    if ( x == 'h' ) return 'x';
    if ( x == 'i' ) return 'd';
    if ( x == 'j' ) return 'u';
    if ( x == 'k' ) return 'i';
    if ( x == 'l' ) return 'g';
    if ( x == 'm' ) return 'l';
    if ( x == 'n' ) return 'b';
    if ( x == 'o' ) return 'k';
    if ( x == 'p' ) return 'r';
    if ( x == 'q' ) return 'z';
    if ( x == 'r' ) return 't';
    if ( x == 's' ) return 'n';
    if ( x == 't' ) return 'w';
    if ( x == 'u' ) return 'j';
    if ( x == 'v' ) return 'p';
    if ( x == 'w' ) return 'f';
    if ( x == 'x' ) return 'm';
    if ( x == 'y' ) return 'a';
    if ( x == 'z' ) return 'q';  
}

int main(){
    freopen("inputa.in", "r", stdin);
    freopen("outputa.out", "w", stdout);
    int tcase = 1;
    int t; scanf("%d", &t);
    
    getchar();
    while (t--){
          char G[105]; gets(G);
          printf("Case #%d: ", tcase++);
          FOR (i, 0, strlen(G)){
              if ( G[i] == ' ' ) printf(" ");
              else printf("%c", conv(G[i]));    
          }      
          puts("");
    }
    return 0;
}
