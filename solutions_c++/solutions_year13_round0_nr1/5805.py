#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <cstring>

using namespace std;

string transition = "yhesocvxduiglbkrztnwjpfmaq";

char tableau[21];
int main(int argc, char *argv[]){
  int finish;
  int nCase=0;
  string line;
 // scanf("%d",&nCase);
  nCase = atoi(argv[1]);
  //getchar();
  int res=0;
  for (int iCase  = 1; iCase <= nCase; iCase++) {
    finish = 0;
    for (int numCar = 0; numCar < 17; numCar++) {
        if (tableau[numCar] != ' ') {
            tableau[numCar] = getchar();
            //printf("%c",tableau[numCar]);
            fflush(stdout);
        } else {
          // printf("LA%d",tableau[numCar]);
           fflush(stdout);
        }
        if (tableau[numCar] == 46) {
            finish = 1;
           // printf("la %d\n",iCase);
        }
    }
    res = 0;
    if (((tableau[0] == 'X' || tableau[0] == 'T') 
     && (tableau[1] == 'X' || tableau[1] == 'T')
     && (tableau[2] == 'X' || tableau[2] == 'T')
     && (tableau[3] == 'X' || tableau[3] == 'T'))
     || ((tableau[4] == 'X' || tableau[4] == 'T')
     && (tableau[5] == 'X' || tableau[5] == 'T')
     && (tableau[6] == 'X' || tableau[6] == 'T')
     && (tableau[7] == 'X' || tableau[7] == 'T'))
     || ((tableau[8] == 'X' || tableau[8] == 'T')
     && (tableau[9] == 'X' || tableau[9] == 'T')
     && (tableau[10] == 'X' || tableau[10] == 'T')
     && (tableau[11] == 'X' || tableau[11] == 'T'))
     || ((tableau[12] == 'X' || tableau[12] == 'T')
     && (tableau[13] == 'X' || tableau[13] == 'T')
     && (tableau[14] == 'X' || tableau[14] == 'T')
     && (tableau[15] == 'X' || tableau[15] == 'T'))

     || ((tableau[0] == 'X' || tableau[0] == 'T')
     && (tableau[4] == 'X' || tableau[4] == 'T')
     && (tableau[8] == 'X' || tableau[8] == 'T')
     && (tableau[12] == 'X' || tableau[12] == 'T'))
     || ((tableau[1] == 'X' || tableau[1] == 'T')
     && (tableau[5] == 'X' || tableau[5] == 'T')
     && (tableau[9] == 'X' || tableau[9] == 'T')
     && (tableau[13] == 'X' || tableau[13] == 'T'))
     || ((tableau[2] == 'X' || tableau[2] == 'T')
     && (tableau[6] == 'X' || tableau[6] == 'T')
     && (tableau[10] == 'X' || tableau[10] == 'T')
     && (tableau[14] == 'X' || tableau[14] == 'T'))
     || ((tableau[3] == 'X' || tableau[3] == 'T')
     && (tableau[7] == 'X' || tableau[7] == 'T')
     && (tableau[11] == 'X' || tableau[11] == 'T')
     && (tableau[15] == 'X' || tableau[15] == 'T'))

     || ((tableau[0] == 'X' || tableau[0] == 'T')
     && (tableau[5] == 'X' || tableau[5] == 'T')
     && (tableau[10] == 'X' || tableau[10] == 'T')
     && (tableau[15] == 'X' || tableau[15] == 'T'))
     || ((tableau[3] == 'X' || tableau[3] == 'T')
     && (tableau[6] == 'X' || tableau[6] == 'T')
     && (tableau[9] == 'X' || tableau[9] == 'T')
     && (tableau[12] == 'X' || tableau[12] == 'T'))) {
         printf("Case #%d: X won\n",iCase);
         res=1;
     } 

    if (((tableau[0] == 'O' || tableau[0] == 'T')
     && (tableau[1] == 'O' || tableau[1] == 'T')
     && (tableau[2] == 'O' || tableau[2] == 'T')
     && (tableau[3] == 'O' || tableau[3] == 'T'))
     || ((tableau[4] == 'O' || tableau[4] == 'T')
     && (tableau[5] == 'O' || tableau[5] == 'T')
     && (tableau[6] == 'O' || tableau[6] == 'T')
     && (tableau[7] == 'O' || tableau[7] == 'T'))
     || ((tableau[8] == 'O' || tableau[8] == 'T')
     && (tableau[9] == 'O' || tableau[9] == 'T')
     && (tableau[10] == 'O' || tableau[10] == 'T')
     && (tableau[11] == 'O' || tableau[11] == 'T'))
     || ((tableau[12] == 'O' || tableau[12] == 'T')
     && (tableau[13] == 'O' || tableau[13] == 'T')
     && (tableau[14] == 'O' || tableau[14] == 'T')
     && (tableau[15] == 'O' || tableau[15] == 'T'))

     || ((tableau[0] == 'O' || tableau[0] == 'T')
     && (tableau[4] == 'O' || tableau[4] == 'T')
     && (tableau[8] == 'O' || tableau[8] == 'T')
     && (tableau[12] == 'O' || tableau[12] == 'T'))
     || ((tableau[1] == 'O' || tableau[1] == 'T')
     && (tableau[5] == 'O' || tableau[5] == 'T')
     && (tableau[9] == 'O' || tableau[9] == 'T')
     && (tableau[13] == 'O' || tableau[13] == 'T'))
     || ((tableau[2] == 'O' || tableau[2] == 'T')
     && (tableau[6] == 'O' || tableau[6] == 'T')
     && (tableau[10] == 'O' || tableau[10] == 'T')
     && (tableau[14] == 'O' || tableau[14] == 'T'))
     || ((tableau[3] == 'O' || tableau[3] == 'T')
     && (tableau[7] == 'O' || tableau[7] == 'T')
     && (tableau[11] == 'O' || tableau[11] == 'T')
     && (tableau[15] == 'O' || tableau[15] == 'T'))

     || ((tableau[0] == 'O' || tableau[0] == 'T')
     && (tableau[5] == 'O' || tableau[5] == 'T')
     && (tableau[10] == 'O' || tableau[10] == 'T')
     && (tableau[15] == 'O' || tableau[15] == 'T'))
     || ((tableau[3] == 'O' || tableau[3] == 'T')
     && (tableau[6] == 'O' || tableau[6] == 'T')
     && (tableau[9] == 'O' || tableau[9] == 'T')
     && (tableau[12] == 'O' || tableau[12] == 'T'))) {
         printf("Case #%d: O won\n",iCase);
         res=1;
     }



     if (finish == 1 and res == 0) {
         printf("Case #%d: Game has not completed\n",iCase);
         res =1;
     } 
     if (res == 0){
         printf("Case #%d: Draw\n",iCase);
     }

     


  }
  return 0;
}
