#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

char Opp[27][27];
char Comb[27][27];

bool isOpp(char a, char b)
{
    return Opp[a-'A'][b-'A'];
}

char getComb(char a, char b)
{
    return Comb[a-'A'][b-'A'];
}

int main()
{
    int T;
    scanf("%d", &T);
//    printf("T: %d\n", T);
    for(int k=0;k<T; ++k)
    {
        memset(Opp, 0, sizeof Opp);
        memset(Comb, 0, sizeof Comb);

        int C;
        scanf("%d", &C);
//        printf("C: %d\n", C);

        // read the input
        for(int j=0;j<C;++j)
        {
            char a,b,c;
            scanf(" %c%c%c", &a,&b,&c);
//            printf(" C: %c%c%c\n", a,b,c);
            Comb[a-'A'][b-'A'] = c;
            Comb[b-'A'][a-'A'] = c;
        }

        int D;
        scanf("%d", &D);
//        printf("D: %d\n", D);

        for(int j=0;j<D;++j)
        {
            char a,b;
            scanf(" %c%c", &a,&b);
//            printf(" D: %c%c\n", a,b);
            Opp[a-'A'][b-'A'] = 1;
            Opp[b-'A'][a-'A'] = 1;
        }

        int N;
        scanf("%d", &N);

        char inp[101], out[101];
        memset(inp, 0, sizeof inp);
        memset(out, 0, sizeof out);

        scanf("%s", inp);
//        printf(" inp:%s\n", inp);
        
        for(int i=0;i <strlen(inp); ++i)
        {
            int len = strlen(out);
            if (len == 0)
            {
                out[0] = inp[i]; out[1]=0;
                continue;
            }
            else
            {
                char com = getComb( out[len - 1], inp[i] );
                if ( com )
                {
                    out[len-1] = com; out[len]=0;
                }
                else
                {
                    bool cleared = false;
                    for(int j=len-1; j>=0; --j)
                    {
                        if ( isOpp(out[j], inp[i]) )
                        {
                            memset(out, 0, sizeof out);
                            cleared = true;
                            break;
                        }
                    }

                    if (!cleared)
                    {
                        out[len] = inp[i]; out[len+1]=0;
                    }
                }
            }
        }


        printf("Case #%d: [", k+1);
        for(int i=0;i<strlen(out); ++i)
        {
            if (i == 0)
                printf("%c", out[i]);
            else
                printf(", %c", out[i]);
        }
        printf("]\n");
    }

    return 0;
}
