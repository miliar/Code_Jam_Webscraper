#include <cmath>
#include <cstdio>
#include <algorithm>
//#include <map>
//#include <numeric>
//#include <queue>
//#include <set>
//#include <string>
//#include <utility>
//#include <vector>

using namespace std;

typedef signed long long    int64;
typedef unsigned long long  uint64;
typedef signed int          int32;
typedef unsigned int        uint32;
typedef signed short        int16;
typedef unsigned short      uint16;
typedef signed char         int8;
typedef unsigned char       uint8;

#define T_MAX   (20)
#define A_MAX   (99999)
#define B_MAX   (100000)


int main(void) {
    uint32 T;
    uint32 A, B;
    float P[A_MAX];
    
    scanf("%d", &T);
    //fgets(line, sizeof(line), stdin);
    //sscanf(line, "%d", &T);
    //printf("T = %d\n", T);
    
    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        float pAllRight = 1.0;
        float pLastWrong = 0.0;
        float eKeepTyping = 0.0;
        float eBackOnce = 0.0;
        float eRightAlway = 0.0;
        float eMin = 0.0;

        /* Test Case run once */
        //fgets(str, sizeof(str), stdin);
        scanf("%d %d", &A, &B);
        //printf("A=%u, B=%u\n", A, B);
        for (uint32 Ai = 1; Ai <= A; Ai++)
        {
            scanf("%f", &P[Ai - 1]);
            //printf("P[%u] = %f\n", (Ai - 1), P[Ai - 1]);
            pLastWrong = (pAllRight) * (1.0 - P[Ai - 1]);
            pAllRight *= P[Ai - 1];
        }

        /* Expected of `Keep Typing` */
        eKeepTyping = (pAllRight * (B - A + 1)) + ((1.0 - pAllRight) * ((B - A + 1) + (B + 1)));
        
        /* Expected of `Backspace Once` */
        eBackOnce = ((pAllRight + pLastWrong) * (1 + 1 + (B - A) + 1)) + ((1.0 - (pAllRight + pLastWrong)) * (1 + 1 + (B - A) + 1 + B + 1));
        
        /* Expected of `Right Alway` */
        eRightAlway = 1 + B + 1;

        /* keep typing */
        //printf("pAllRight = %f\n", pAllRight);
        //printf("eKeepTyping = %f\n", eKeepTyping);
        //printf("eBackOnce = %f\n", eBackOnce);
        //printf("eRightAlway = %f\n", eRightAlway);

        /* check */
        if (eKeepTyping <= eBackOnce)
        {
            eMin = eKeepTyping;
        }
        else
        {
            eMin = eBackOnce;
        }

        if (eRightAlway < eMin)
        {
            eMin = eRightAlway;
        }

        /* Print */
        printf("Case #%d: %f\n", Ti, eMin);
    }

    return 0;
}


