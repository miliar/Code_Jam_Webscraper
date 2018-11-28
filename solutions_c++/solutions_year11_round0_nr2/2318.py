#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <math.h>

using namespace std;

int in_list[30];
char w[105], spell[105];

bool oppo[30][30];
char comb[30][30];

int main(){

    freopen("B-large.IN", "r", stdin );
    freopen("sol.txt", "w", stdout );

    int test;
    scanf("%d", &test );

    for(int t = 1; t <= test; ++t ){

        for(int i = 0; i < 30; ++i )
          for(int j = 0; j < 30; ++j )
            comb[i][j] = '?';

        memset( oppo, 0, sizeof( oppo ) );
        memset( in_list, 0, sizeof(in_list) );

        int c;
        scanf("%d", &c );

        for(int i = 0; i < c; ++i ){
            scanf("%s", w );
            comb[w[0]-'A'][w[1]-'A'] = w[2];
            comb[w[1]-'A'][w[0]-'A'] = w[2];
        }

        int d;
        scanf("%d", &d );
        for(int i = 0; i < d; ++i ){
            scanf("%s", w );
            oppo[w[0]-'A'][w[1]-'A'] = 1;
            oppo[w[1]-'A'][w[0]-'A'] = 1;
        }

        int n;
        scanf("%d %s", &n, spell);

        stack <char> S;

        for(int i = 0; i < n; ++i ){
          if( !S.empty() && comb[S.top()-'A'][spell[i]-'A'] != '?' ){
              int k = S.top()-'A'; S.pop();
              --in_list[k];
              S.push( comb[k][spell[i]-'A'] );
              ++in_list[comb[k][spell[i]-'A']-'A'];
          }else{
              ++in_list[spell[i]-'A'];
              S.push( spell[i] );
          }
          for(int j = 0; j < 26; ++j )
             if( in_list[j] > 0 && oppo[j][S.top()-'A'] ){
                memset( in_list, 0, sizeof(in_list ) );
                while( !S.empty() ) S.pop();
             }
        }

        vector <char> sol;
        while( !S.empty() ){ sol.push_back( S.top() ); S.pop(); }

        int sz = sol.size()-1;
        if( sz < 0 ){ printf("Case #%d: []\n", t ); continue; }

        printf("Case #%d: [%c", t, sol[sz] );
        for(int i = sz-1; i >= 0; --i )
          printf(", %c", sol[i] );

        putchar(']');
        putchar('\n');

    }

    return 0;
}






