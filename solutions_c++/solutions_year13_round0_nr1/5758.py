// Author : Mohd. Imranul Hoque Limon
// INST : Daffodil Internation University
// ID : 102-15-1036

#include <stdlib.h>
#include <cmath>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <cctype>
#include <deque>
#include <queue>

#define black 0
#define white 1
#define tru -1
#define fals -2
#define siz 1000000
using namespace std;

int main(){

    #ifdef localhost
    freopen("new.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int i, j, cnt, Cases, Case = 0, X, O, k, l, K, L;
    char a[50][50];

    scanf("%d",&Cases);
    while(Cases--){

        vector <char> v;
        memset(a,0,sizeof(a));

        //cin.ignore();

        for(i=0; i<4; i++){
            scanf("%s",a[i]);
        }

        O = 0;
        X = 0;
        int f = 0;
        for(K=0; K<4; K++){
            for(L=0; L<4; L++){

                //printf("X = %d O = %d\n",X,O);

                i = K;
                j = L;


                if(a[i][j]=='X' && a[i][j+1]=='X' && a[i][j+2]=='X'){
                    X++;

                    if(a[i][j+3] == 'X' || a[i][j+3] == 'T' ){

                        X+=100;
                        v.push_back('X');
                        //printf("%d X = limon\n",X);
                        //f = 1;
                        L = K = 4;
                        //break;
                    }

                }

                 if(a[i][j]=='O' && a[i][j+1]=='O' && a[i][j+2]=='O'){
                    O++;
                    if(a[i][j+3] == 'O' || a[i][j+3] == 'T' ){

                        O+=100;
                        v.push_back('O');
                        //printf("%d O = limon\n",O);
                        //f = 1;
                        //L = K = 4;
                        //break;
                    }

                }

                if(a[i][j]=='O' && a[i+1][j]=='O'&&a[i+2][j]=='O'){
                    O++;
                    if(a[i+3][j] == 'O' || a[i+3][j] == 'T')
                    {
                        O+=100;
                        v.push_back('O');
                        //f = 1;
                        //L = K = 4;
                        //break;
                    }

                }

                if(a[i][j]=='X' && a[i+1][j]=='X' && a[i+2][j]=='X'){
                    X++;
                    if(a[i+3][j] == 'X' || a[i+3][j] == 'T')
                    {
                        X+=100;
                        v.push_back('X');
                        //f = 1;
                        //L = K = 4;
                        //break;
                    }

                }

                  if( a[i][j]=='O'&&a[i+1][j+1]=='O'&&a[i+2][j+2]=='O'){
                    O++;
                    if(a[i+3][j+3] == 'O' || a[i+3][j+3] == 'T')
                    {

                        v.push_back('O');
                        O+=100;
                        //f = 1;
                        //L = K = 4;
                        //break;
                    }

                }

                if(a[i][j]=='X'&&a[i+1][j+1]=='X'&&a[i+2][j+2]=='X'){
                    X++;
                    if(a[i+3][j+3] == 'X' || a[i+3][j+3] == 'T')
                    {
                        v.push_back('X');
                        X+=100;
                        //f = 1;
                        //L = K = 4;
                        //break;
                    }

                }


                if(a[i][j]=='X'&&a[i+1][j-1]=='X'&&a[i+2][j-2]=='X'){
                    X++;
                    if(a[i+3][j-3] == 'X' || a[i+3][j-3] == 'T')
                    {
                        v.push_back('X');
                        X+=100;
                        //f = 1;
                        //L = K = 4;
                        //break;
                    }

                }

                if(a[i][j]=='O'&&a[i+1][j-1]=='O'&&a[i+2][j-2]=='O'){
                    O++;
                    if(a[i+3][j-3] == 'O' || a[i+3][j-3] == 'T')
                    {
                        v.push_back('O');
                        O+=100;
                        //f = 1;
                        //L = K = 4;
                        //break;
                    }
                }

            }
        }

        int x = 0;
        int o = 0;

        for(i=0; i<v.size(); i++){
            if(v[i] == 'X') x++;

            else if(v[i] == 'O') o++;
        }

        if(x>o) printf("Case #%d: X won\n",++Case);
        else if(x<o) printf("Case #%d: O won\n",++Case);
        else if(X>O) printf("Case #%d: X won\n",++Case);
        else if(O>X) printf("Case #%d: O won\n",++Case);
        else if(X == 0 && O == 0) printf("Case #%d: Game has not completed\n",++Case);

        else printf("Case #%d: Draw\n",++Case);

        //printf("\n");

        v.clear();

    }

    return 0;
}



