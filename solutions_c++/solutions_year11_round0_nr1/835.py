#include <cstdio>
#include <cstdlib>

int main()
{
    int T;
    scanf("%d", &T);
    int idx, index, maxStep, bn, bStep, oStep;
    int bCur, oCur, des;
    int oDiff, bDiff;
    int tmp;
    char ch;
    for (idx = 0; idx < T; ++idx)
    {
        scanf("%d", &bn);
        bCur = 1;
        oCur = 1;
        bStep = 0;
        oStep = 0;
        index = 0;
        oDiff = 0;
        bDiff = 0;
        while (index< bn)
        {
            scanf(" %c %d", &ch, &des);

            if (ch == 'B')
            {
                tmp = (int)abs(des - bCur);
                if (tmp - oDiff <= 0)
                    tmp = 1;
                else 
                    tmp = tmp - oDiff + 1;
                bStep += tmp + oDiff;
                bDiff += tmp;
                oDiff = 0;
                bCur = des;
                maxStep = bStep;
            }
            else
            {
                tmp = (int)abs(des - oCur);
                if (tmp - bDiff < 0)
                    tmp = 1;
                else 
                    tmp = tmp - bDiff + 1;
                oStep += tmp + bDiff;
                oDiff += tmp;
                bDiff = 0;
                oCur = des;
                maxStep = oStep;
            }
            ++index;
        }
        printf("Case #%d: %d\n", idx + 1, maxStep);
    }
    return 0;
}
