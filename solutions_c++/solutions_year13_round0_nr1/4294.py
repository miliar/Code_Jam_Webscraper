/*Google CodeJam
  Problem-A
  Tic-Tac-Toe-Tomek
  */
#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>

#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <iomanip>
#include <ctime>
#include <assert.h>

using namespace std;

string Grid[5];int N = 4;


int main()
{
    freopen("B.txt", "r", stdin);
    freopen("B.out", "w", stdout);
    int i, j, k, t, X, O, T, Dot,cas=1;
    scanf("%d", &t);
    while(t--){
         int cnt  = 0; Dot=0;
         for(i = 0; i<4; i++) cin>>Grid[i];

         for(i = 0; i<4; i++){
                X=O=T=0;
                for(j = 0; j<4; j+=1){
                    if(Grid[i][j] == 'T') T++;
                    else if(Grid[i][j]=='X') X++;
                    else if(Grid[i][j]=='O') O++;
                    else Dot++;
                    }
              if(X==4) {printf("Case #%d: X won\n",cas++); cnt =1;break;}
              else if(O==4)  {printf("Case #%d: O won\n",cas++); cnt =1;break;}
              else if(X==3 && T==1) {printf("Case #%d: X won\n",cas++); cnt =1;break;}
              else if(O==3 && T==1)  {printf("Case #%d: O won\n",cas++); cnt =1;break;}
         }

          if(cnt) continue;
           X=O=T=0;
          for(i = 0; i<4; i++){
                X=O=T=0;
                for(j = 0; j<4; j+=1){
                    if(Grid[j][i] == 'T') T++;
                    else if(Grid[j][i]=='X') X++;
                    else if(Grid[j][i]=='O') O++;
                    else Dot++;
                    }
              if(X==4) {printf("Case #%d: X won\n",cas++); cnt =1;break;}
              else if(O==4)  {printf("Case #%d: O won\n",cas++); cnt =1;break;}
              else if(X==3 && T==1) {printf("Case #%d: X won\n",cas++);cnt =1; break;}
              else if(O==3 && T==1)  {printf("Case #%d: O won\n",cas++); cnt =1;break;}
         }

         if(cnt) continue;
         X=O=T=0;
         for(i=0;i<4;i++){
            if(Grid[i][i] == 'T') T++;
                    else if(Grid[i][i]=='X') X++;
                    else if(Grid[i][i]=='O') O++;
                    else Dot++;
         }
             if(X==4) {printf("Case #%d: X won\n",cas++); cnt =1;}
              else if(O==4)  {printf("Case #%d: O won\n",cas++); cnt =1;}
              else if(X==3 && T==1) {printf("Case #%d: X won\n",cas++);cnt =1;}
              else if(O==3 && T==1)  {printf("Case #%d: O won\n",cas++); cnt =1;}
        if(cnt) continue;
         X=O=T=0;
         for(i=0,j=3;i<4;i++,j--){
            if(Grid[i][j] == 'T') T++;
                    else if(Grid[i][j]=='X') X++;
                    else if(Grid[i][j]=='O') O++;
                    else Dot++;
         }
             if(X==4) {printf("Case #%d: X won\n",cas++); cnt =1;}
              else if(O==4)  {printf("Case #%d: O won\n",cas++); cnt =1;}
              else if(X==3 && T==1) {printf("Case #%d: X won\n",cas++);cnt =1;}
              else if(O==3 && T==1)  {printf("Case #%d: O won\n",cas++); cnt =1;}
        if(cnt) continue;
        if(Dot) printf("Case #%d: Game has not completed\n",cas++);
        else printf("Case #%d: Draw\n",cas++);
    }
    return 0;
}
