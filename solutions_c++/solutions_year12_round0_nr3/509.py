#include <cstdio>
#include <set>
#include <iostream>
using namespace std;

int main()
{
    int T, A, B;
    scanf("%d", &T);

    for(int t = 1; T--; ++t)
    {
        set < pair<int, int> > ans;
        scanf("%d%d", &A, &B);

        for(int i = A; i <= B; i++)
        {
            int temp = i, cnt = 0, tempv, ten = 10, p = 1, ccnt;
            while(temp)
                ++cnt, temp /= 10, p *= 10;
//            printf("WHY %d - %d %d\n", i, cnt, p); 
            for(int j = 1; j < cnt; j++)
            {
                tempv = (i/ten)+(i%ten)*(p/ten);
                ccnt = 0, temp = tempv;
                while(temp) temp /= 10, ++ccnt;
                if(tempv < i && ccnt==cnt && tempv >= A && tempv <= B ) ans.insert( make_pair(i, tempv) );
//                printf("GG %d - %d\n", i, tempv);
                ten *= 10;
            }
        }

        printf("Case #%d: %d\n", t, ans.size());
    }

    return 0;
}
