#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <algorithm>
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define REP(i, a, b) \
    for(int i=int(a); i<int(b); ++i)

int main()
{
    FILE *fout = fopen ("test.out", "w");

    char c;
    int tc,cn=1,rowx[5],rowy[5],colx[5],coly[5],ldijagx,ldijagy,rdijagx,rdijagy;
    bool full;
    scanf("%d", &tc);
    getchar();
    while(tc--){
        memset(rowx,0,sizeof(rowx));
        memset(rowy,0,sizeof(rowy));
        memset(colx,0,sizeof(colx));
        memset(coly,0,sizeof(coly));
        ldijagx=ldijagy=rdijagx=rdijagy=0;
        full=true;
        REP(i,1,5){
            REP(j,1,5){
                c=getchar();
                if(c=='X' || c=='T'){
                    ++rowx[i];
                    ++colx[j];
                    if(i==j)
                        ++ldijagx;
                    if(i+j==5)
                        ++rdijagx;
                }
                if(c=='O' || c=='T'){
                    ++rowy[i];
                    ++coly[j];
                    if(i==j)
                        ++ldijagy;
                    if(i+j==5)
                        ++rdijagy;
                }
                if(c=='.')
                    full=false;
            }
            getchar();
        }
        if(ldijagx==4 || rdijagx==4 || rowx[1]==4 || rowx[2]==4 || rowx[3]==4 || rowx[4]==4 ||
           colx[1]==4 || colx[2]==4 || colx[3]==4 || colx[4]==4){
                fprintf(fout,"Case #%d: X won\n", cn);
           }
        else if(ldijagy==4 || rdijagy==4 || rowy[1]==4 || rowy[2]==4 || rowy[3]==4 || rowy[4]==4 ||
           coly[1]==4 || coly[2]==4 || coly[3]==4 || coly[4]==4){
                fprintf(fout,"Case #%d: O won\n", cn);
           }
        else if(full){
            fprintf(fout,"Case #%d: Draw\n", cn);
        }
        else{
            fprintf(fout,"Case #%d: Game has not completed\n", cn);
        }

        ++cn;
        getchar();
    }

    return 0;
}
