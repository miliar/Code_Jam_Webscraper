#include <cstdio>

using namespace std;


struct s_fils
{
    int left;
    int right;
};


int nbTests, nbFils;
s_fils fils[16][1000];

int reponse;
int curLeft, curRight;



int main()
{
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);

    scanf("%d", &nbTests);

    for (int test = 1; test <= nbTests; test++)
    {
        reponse = 0;
        scanf("%d", &nbFils);
        //printf("%d\n", nbFils);

        for (int lu = 0; lu < nbFils; lu++)
            scanf("%d %d", &fils[test][lu].left, &fils[test][lu].right);

        for (int cur = 0; cur < nbFils; cur++)
        {
            curLeft = fils[test][cur].left;
            curRight = fils[test][cur].right;
            for (int autre = 0; autre < nbFils; autre++)
            {
                if (curLeft < fils[test][autre].left && curRight > fils[test][autre].right)
                    reponse++;
            }

        }

        printf("Case #%d: %d\n", test, reponse);
    }


    return 0;
}
