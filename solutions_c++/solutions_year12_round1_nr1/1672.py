//---------------------------------------------------------------------------
//---------------------------------------------------------------------------
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <stack>
#include <utility>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
        freopen("A-small-attempt0.in","rt",stdin);
        freopen("out.txt","wt",stdout);

        int T,ntest=1,A,B;
        double M[10][10];
        vector<double> prob;
        double minexpected;
        scanf("%d\n",&T);
        while(T--)
        {
                prob.clear();
                for(int i=0; i<10; i++) for(int j=0; j<10; j++) M[i][j] = 0.0;
                scanf("%d %d\n",&A,&B); prob.resize(A);
                for(int i=0; i<A; i++)
                        scanf("%lf",&prob[i]);

                if(A == 1)
                {
                        // 0 falla
                        M[0][0] = (prob[0]);
                        // 1 falla
                        M[0][1] = (1.0 - prob[0]);

                        // Keep going
                        M[1][0] = B;
                        M[1][1] = ((B + 1) + B);

                        // Press enter and retype
                        M[2][0] = B + 2;
                        M[2][1] = B + 2;

                        // Back Once
                        M[3][0] = (B + 1) + 1;
                        M[3][1] = (B + 1) + 1;
                }
                if(A == 2)
                {
                        // 0 falla
                        M[0][0] = prob[0] * prob[1];
                        // 1 falla
                        M[0][1] = (prob[0]) * (1.0 - prob[1]);
                        M[0][2] = (1.0 - prob[0]) * (prob[1]);
                        // 2 falla
                        M[0][3] = (1.0 - prob[0]) * (1.0 - prob[1]);

                         // Keep going
                        M[1][0] = (B - 1);
                        M[1][1] = ((B + 1) + (B - 1));
                        M[1][2] = ((B + 1) + (B - 1));
                        M[1][3] = ((B + 1) + (B - 1));

                        // Press enter and retype
                        M[2][0] = B + 2;
                        M[2][1] = B + 2;
                        M[2][2] = B + 2;
                        M[2][3] = B + 2;

                        // Back Once
                        M[3][0] = (B + 1);
                        M[3][1] = (B + 1);
                        M[3][2] = (B + 1) + (B + 1);
                        M[3][3] = (B + 1) + (B + 1);

                        // Back Twice
                        M[4][0] = (B + 1) + 2;
                        M[4][1] = (B + 1) + 2;
                        M[4][2] = (B + 1) + 2;
                        M[4][3] = (B + 1) + 2;
                }
                if(A == 3)
                {
                        // 0 falla
                        M[0][0] = prob[0] * prob[1] * prob[2];
                        // 1 falla
                        M[0][1] = (prob[0]) * (prob[1]) * (1.0 - prob[2]);
                        M[0][2] = (prob[0]) * (1.0 - prob[1]) * (prob[2]);
                        M[0][3] = (1.0 - prob[0]) * (prob[1]) * (prob[2]);
                        // 2 fallan
                        M[0][4] = (prob[0]) * (1.0 - prob[1]) * (1.0 - prob[2]);
                        M[0][5] = (1.0 - prob[0]) * (prob[1]) * (1.0 - prob[2]);
                        M[0][6] = (1.0 - prob[0]) * (1.0 - prob[1]) * (prob[2]);
                        // 3 falla
                        M[0][7] = (1.0 - prob[0]) * (1.0 - prob[1]) * (1.0 - prob[2]);

                         // Keep going
                        M[1][0] = (B - 2);
                        M[1][1] = ((B + 1) + (B - 2));
                        M[1][2] = ((B + 1) + (B - 2));
                        M[1][3] = ((B + 1) + (B - 2));
                        M[1][4] = ((B + 1) + (B - 2));
                        M[1][5] = ((B + 1) + (B - 2));
                        M[1][6] = ((B + 1) + (B - 2));
                        M[1][7] = ((B + 1) + (B - 2));

                        // Press enter and retype
                        M[2][0] = B + 2;
                        M[2][1] = B + 2;
                        M[2][2] = B + 2;
                        M[2][3] = B + 2;
                        M[2][4] = B + 2;
                        M[2][5] = B + 2;
                        M[2][6] = B + 2;
                        M[2][7] = B + 2;

                        
                        // Back Once
                        M[3][0] = (B);
                        M[3][1] = (B);
                        M[3][2] = (B) + (B + 1);
                        M[3][3] = (B) + (B + 1);
                        M[3][4] = (B) + (B + 1);
                        M[3][5] = (B) + (B + 1);
                        M[3][6] = (B) + (B + 1);
                        M[3][7] = (B) + (B + 1);

                        // Back twice
                        M[4][0] = (B + 2);
                        M[4][1] = (B + 2);
                        M[4][2] = (B + 2);
                        M[4][3] = (B + 2) + (B + 1);
                        M[4][4] = (B + 2);
                        M[4][5] = (B + 2) + (B + 1);
                        M[4][6] = (B + 2) + (B + 1);
                        M[4][7] = (B + 2) + (B + 1);

                        // Back three times
                        M[5][0] = (B + 1) + 3;
                        M[5][1] = (B + 1) + 3;
                        M[5][2] = (B + 1) + 3;
                        M[5][3] = (B + 1) + 3;
                        M[5][4] = (B + 1) + 3;
                        M[5][5] = (B + 1) + 3;
                        M[5][6] = (B + 1) + 3;
                        M[5][7] = (B + 1) + 3;
                }


                int size;
                if(A == 1) size = 2;
                if(A == 2) size = 4;
                if(A == 3) size = 8;

                for(int i=1; i < 3 + A; i++)
                {
                        double suma = 0;
                        for(int j=0; j<size; j++)
                                suma += (M[i][j] * M[0][j]);
                        M[i][size] = suma;
                }

                minexpected = 20000000;
                for(int i=1; i < 3 + A; i++)
                        minexpected = min(minexpected, M[i][size]);
                printf("Case #%d: %.6lf\n",ntest++,minexpected);
        }
        return 0;
}



 