#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
using namespace std;

int main() {

    int numberCase;
    int googlers;
    int surprising;
    int p, pmin, psmin;
    int total;
    int triplet;

    scanf("%d", &numberCase);

    for(int i = 1; i <= numberCase; i++) {
        scanf("%d %d %d", &googlers, &surprising, &p);
        total = 0;
        //getchar();
        //int listg[googlers];
       // printf("g: %d s: %d p: %d\n", googlers, surprising, p);
        for(int j = 0; j <  googlers; j++) {
            //scanf("%d", &listg[j]);
           scanf("%d", &triplet);
           pmin = p + 2 * (p - 1);
           psmin = p + 2 * (p - 2);
           if( triplet >= pmin) {
                total++;
           }else if(triplet == 0) {
               continue;
           } else if( triplet >= psmin and surprising >= 1) {
               surprising--;
               total++;
           }
        }

        cout << "Case #" << i << ": " << total << endl;

    }

    return 0;
}
