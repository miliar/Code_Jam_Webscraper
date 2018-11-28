#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;

main()
{
    int i, j,  t, n, bot[100], tempo = 0, auxtempo = 0, posO = 1, posB = 1;
    char rob[100];

    scanf("%d", &t);

    for(i=0; i<t; i++)
        {scanf("%d", &n);

        for(j=0; j<n; j++)
            {scanf(" %c", &rob[j]);
            scanf("%d", &bot[j]);}
            j = 0;



            while(j < n)
                    {while(rob[j] == 'O' || rob[j] == 'o')
                        {auxtempo += (fabs(posO - bot[j])+ 1);
                        posO = bot[j];
                        j++;}
                    tempo += auxtempo;
                    if(j >= n)
                    break;

                    if(fabs(posB - bot[j]) > auxtempo)
                        { auxtempo = (fabs(bot[j] - posB) - auxtempo + 1);
                        posB = bot[j];
                        j++;}
                    else
                        {auxtempo = 0;
                        posB = bot[j];}

                         if(j >= n)
                         {tempo += auxtempo;
                         posB = bot[j];
                        break;}

                    while(rob[j] == 'B' || rob[j] == 'b')
                        {auxtempo += (fabs(posB - bot[j]) + 1);
                        posB = bot[j];
                        j++; }
                    tempo += auxtempo;
                    if(j >= n)
                    break;

                    if(fabs(posO - bot[j]) > auxtempo)
                        { auxtempo = (fabs(bot[j] - posO) - auxtempo + 1);
                        posO = bot[j];
                        j++; }
                    else
                        {auxtempo = 0;
                        posO = bot[j];}
                         if(j >= n)
                         {tempo += auxtempo;
                            break;}
                    }
                cout << "Case #" << i+1 << ": " << tempo << "\n";
                tempo = 0;
                j = 0;
                auxtempo = 0;
                posO = 1;
                posB = 1;
                                        for(j=0; j<100; j++)
                rob[j] = ' ';}

            return 0;
}




