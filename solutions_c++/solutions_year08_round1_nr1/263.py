#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

#define MAX_N   (1000)
using namespace std;

long long aP[MAX_N], aN[MAX_N], bP[MAX_N], bN[MAX_N];
int naP, naN, nbP, nbN, naZ, nbZ;


int main() {
    int N;
    scanf("%d", &N);
    int tc;
    
    int i, j;
    for (tc = 0; tc < N; tc++) {
        printf("Case #%d: ", tc+1);
        int NV = 0;
        scanf("%d", &NV);
        naP = naN = nbP = nbN = naZ = nbZ = 0;
        for (i = 0; i < NV; i++) {
            scanf("%d", &j);
            if (j > 0) aP[naP++] = j;
            else if (j < 0) aN[naN++] = -j;
            else naZ++;
        }
        for (i = 0; i < NV; i++) {
            scanf("%d", &j);
            if (j > 0) bP[nbP++] = j;
            else if (j < 0) bN[nbN++] = -j;
            else nbZ++;
        }
        sort(aP, aP + naP);
        sort(aN, aN + naN);
        sort(bP, bP + nbP);
        sort(bN, bN + nbN);
        
        long long res = 0;
        //match aP with bN
        j = (naP < nbN) ? naP : nbN;
        for (i = 0; i < j; i++) {
            res += -aP[--naP] * bN[--nbN];
        }
        
        //match aN with bP
        j = (naN < nbP) ? naN : nbP;
        for (i = 0; i < j; i++) {
            res += -aN[--naN] * bP[--nbP];
        }
        
        if (!naP && !naN) { //left with bN and bP
            //all multiplied with zeros, no change
            naP = naN = 0;
        } else if (!naP && !nbP) { //left with aN and bN
            while (nbZ--) {
                naN--;
            }
            while (naZ--) {
                nbN--;
            }
            
            for (i = 0; i < naN; i++) {
                res += aN[i] * bN[nbN - i - 1]; 
            }
        } else if (!nbN && !naN) { //left with bP and aP
            while (nbZ--) {
                naP--;
            }
            while (naZ--) {
                nbP--;
            }

            for (i = 0; i < naP; i++) {
                res += aP[i] * bP[nbP - i - 1]; 
            }
        } else if (!nbN && !nbP) { //left with aN and aP
            //all multiplied with zeros, no change
            nbN = nbP = 0;
        }
        
        printf("%lld\n", res);
    }
    return 0;
}
