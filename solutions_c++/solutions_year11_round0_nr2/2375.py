#include <stdio.h>
//#include <map>
//using namespace std;

typedef unsigned int ui32;

const int BASE_ELEMS_CNT = 8;
char CMX[BASE_ELEMS_CNT][BASE_ELEMS_CNT];
char OMX[BASE_ELEMS_CNT][BASE_ELEMS_CNT];

static void PrintCMX() {
    for (int i = 0; i < BASE_ELEMS_CNT; ++i) {
        printf("%d: |", i);
        for (int j = 0; j < BASE_ELEMS_CNT; ++j)
            if (CMX[i][j])
                printf("%c", CMX[i][j]);
            else
                printf(" ");
        printf("|\n");
    }
    printf("\n");
}

static void PrintOMX() {
    for (int i = 0; i < BASE_ELEMS_CNT; ++i) {
        for (int j = 0; j < BASE_ELEMS_CNT; ++j)
            printf("%d", OMX[i][j]);
        printf("\n");
    }
    printf("\n");
}

static void Reset() {
    for (int i = 0; i < BASE_ELEMS_CNT; ++i) {
        for (int j = 0; j < BASE_ELEMS_CNT; ++j) {
            CMX[i][j] = 0;
            OMX[i][j] = 0;
        }
    }
}

static int CharToIdx(char c) {
    switch(c) {
    case 'Q': return 0;
    case 'W': return 1;
    case 'E': return 2;
    case 'R': return 3;
    case 'A': return 4;
    case 'S': return 5;
    case 'D': return 6;
    case 'F': return 7;
    }
    return -1;
}

static void AddCombination(char a, char b, char c) {
    const int idxA = CharToIdx(a);
    const int idxB = CharToIdx(b);
    CMX[idxA][idxB] = c;
    CMX[idxB][idxA] = c;
    //printf("%c %c %c %d %d - %c %c\n", a, b, c, idxA, idxB, CMX[idxA][idxB], CMX[idxB][idxA]);
}

static void AddConflict(char a, char b) {
    const int idxA = CharToIdx(a);
    const int idxB = CharToIdx(b);
    OMX[idxA][idxB] = 1;
    OMX[idxB][idxA] = 1;
    //printf("%c %c %d %d - %d %d\n", a, b, idxA, idxB, OMX[idxA][idxB], OMX[idxB][idxA]);
}

static char CheckCombination(char a, char b) {
    const int idxA = CharToIdx(a);
    if (idxA == -1)
        return 0;
    const int idxB = CharToIdx(b);
    if (idxB == -1)
        return 0;

    return CMX[idxA][idxB];
}

static bool CheckConflict(char a, char b) {
    const int idxA = CharToIdx(a);
    if (idxA == -1)
        return 0;
    const int idxB = CharToIdx(b);
    if (idxB == -1)
        return 0;

    return OMX[idxA][idxB] != 0;
}

int PRESENT[BASE_ELEMS_CNT];

static void ResetPresent() {
    for (int i = 0; i < BASE_ELEMS_CNT; ++i)
        PRESENT[i] = 0;
}

static void AddToPresent(char ch) {
    const int idx = CharToIdx(ch);
    if (idx >= 0)
        ++PRESENT[idx];
}

static void RemoveFromPresent(char ch) {
    const int idx = CharToIdx(ch);
    if (idx >= 0)
        --PRESENT[idx];
}

/*static bool IsPresent(char ch) {
    const int idx = CharToIdx(ch);
    if (idx < 0)
        return false;
    return PRESENT[idx] > 0;
}*/

int main() {
    int T = 0;
    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        Reset();

        int C = 0;
        scanf("%d", &C);
        char buf[150];
        for (int j = 0; j < C; ++j) {
            scanf("%s", buf);
            AddCombination(buf[0], buf[1], buf[2]);
        }

        int D = 0;
        scanf("%d", &D);
        for (int j = 0; j < D; ++j) {
            scanf("%s", buf);
            AddConflict(buf[0], buf[1]);
        }

        //PrintCMX();
        //PrintOMX();

        char res[150];
        int resLen = 0;
        ResetPresent();

        int N = 0;
        scanf("%d", &N);
        if (N > 0) {
            scanf("%s", buf);
            for (int j = 0; j < N; ++j) {
                const char ch = buf[j];
                //printf("\nch=%c\n", ch);
                if (resLen == 0) {
                    ++resLen;
                    res[0] = ch;
                    AddToPresent(ch);
                } else {
                    const char prevCh = res[resLen-1];
                    const char substCh = CheckCombination(prevCh, ch);
                    /*if (substCh)
                        printf("CheckCombination=%c (%d) %c %c\n", substCh, resLen, prevCh, ch);
                    else
                        printf("ChechCombination=0 (%d) %c %c\n", resLen, prevCh, ch);*/

                    if (substCh) {
                        RemoveFromPresent(prevCh);
                        res[resLen-1] = substCh;
                    } else {
                        const int chIdx = CharToIdx(ch);
                        bool conflict = false;
                        for (int k = 0; k < BASE_ELEMS_CNT; ++k) {
                            if (OMX[chIdx][k] && PRESENT[k]) {
                                ResetPresent();
                                resLen = 0;
                                conflict = true;
                                break;
                            }
                        }

                        if (!conflict) {
                            res[resLen] = ch;
                            ++resLen;
                            AddToPresent(ch);
                        }
                    }
                }

                //res[resLen] = 0;
                //printf("r: %d %s\n", resLen, res);
            }
        }

        res[resLen] = 0;
        //printf("Case #%d: [%s]\n", i+1, res);
        printf("Case #%d: [", i+1);
        for (int j = 0; j < resLen; ++j) {
            if (j != (resLen-1))
                printf("%c, ", res[j]);
            else
                printf("%c", res[j]);
        }
        printf("]\n");
    }
}
