//---------------------------------------------------------------------------
//-- CJ 2012 - Qualification Round Problem C. Recycled Numbers (Small)
//-- @Carlos Mendoza
//--
//-- Ad hoc
//---------------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
        freopen("C-small-attempt0.in","rt",stdin);
        freopen("out.txt","wt",stdout);

        int T,A,B,ntest=1;
        scanf("%d\n",&T);
        while(T--)
        {
                scanf("%d %d\n",&A,&B);
                int cont = 0, nuevo;
                A = max(A,10);
                for(int i=A; i<B; i++)
                        if(i > 9 && i < 100)
                        {
                                nuevo = (i % 10) * 10 + (i / 10);
                                if(nuevo > i && nuevo <=B)
                                        cont++;
                        }
                        else if(i > 99 && i < 1000)
                        {
                                nuevo = (i % 10) * 100 + (i / 10);
                                if(nuevo > i && nuevo <=B)
                                        cont++;

                                nuevo = (i % 100) * 10 + (i / 100);
                                if(nuevo > i && nuevo <=B)
                                        cont++;
                        }
                printf("Case #%d: %d\n",ntest++,cont);
        }
        return 0;
}



