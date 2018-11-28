#include <cstdio>
#include <algorithm>
using namespace std;
int naDep[100], naArr[100];
int nbDep[100], nbArr[100];
void Process(const int &cas)
{
    int timeDiff, na, nb;
    int hour, minute;
    int resa, resb;
    scanf("%d%d%d", &timeDiff, &na, &nb);
    for (int i = 0; i < na; i++) {
        scanf("%d:%d", &hour, &minute);
        naDep[i] = hour * 60 + minute;
        scanf("%d:%d", &hour, &minute);
        naArr[i] = hour * 60 + minute;
    }
    for (int j = 0; j < nb; j++) {
        scanf("%d:%d", &hour, &minute);
        nbDep[j] = hour * 60 + minute;
        scanf("%d:%d", &hour, &minute);
        nbArr[j] = hour * 60 + minute;
    }
    sort(naDep, naDep + na);
    sort(naArr, naArr + na);
    sort(nbDep, nbDep + nb);
    sort(nbArr, nbArr + nb);
    resa = resb = 0;
    for (int i = 0, j = 0; i < na; i++) {
        if (j < nb && nbArr[j] + timeDiff <= naDep[i]) {
            j++;
        }
        else resa++;
    }
    for (int i = 0, j = 0; j < nb; j++) {
        if (i < na && naArr[i] + timeDiff <= nbDep[j]) {
            i++;
        }
        else resb++;
    }
    printf("Case #%d: %d %d\n", cas, resa, resb);
}
int main()
{
    int cas;
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &cas);
    for (int t = 1; t <= cas; t++)
        Process(t);
    return 0;
}
