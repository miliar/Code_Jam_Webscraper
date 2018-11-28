//---------------------------------------------------------------------------
//-- CJ 2012 - Qualification Round Problem B. Dancing With the Googlers (Small)
//-- @Carlos Mendoza
//--
//-- Math
//---------------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>

struct Reg
{
        int mayorNS;
        int mayorS;
};

using namespace std;

int main()
{
        freopen("B-small-attempt0.in","rt",stdin);
        freopen("out.txt","wt",stdout);

        int T,ntest=1,N,S,p,v;
        int n1,n2,n3;
        int r1,r2,r3;
        vector<Reg> vec;
        Reg aux;
        scanf("%d\n",&T);
        while(T--)
        {
                vec.clear();
                scanf("%d%d%d",&N,&S,&p);
                for(int i=0;i<N;i++)
                {
                        scanf("%d",&v);
                        if(v % 3 == 0)
                        {
                                aux.mayorNS = v / 3;
                                aux.mayorS = ((v - 3) / 3) + 2;

                                n1 = ((v - 0) / 3); n2 = n1    ; n3 = n1;
                                r1 = ((v - 3) / 3); r2 = r1 + 1; r3 = r1 + 2;

                                if(n1 < 0 || n2 < 0 || n3 < 0)
                                        aux.mayorNS = -1;
                                if(r1 < 0 || r2 < 0 || r3 < 0)
                                        aux.mayorS = -1;

                        }
                        else if(v % 3 == 1)
                        {
                                aux.mayorNS = ((v - 1) / 3) + 1;
                                aux.mayorS = ((v - 4) / 3) + 2;

                                n1 = ((v - 1) / 3); n2 = n1    ; n3 = n1 + 1;
                                r1 = ((v - 4) / 3); r2 = r1 + 2; r3 = r1 + 2;

                                if(n1 < 0 || n2 < 0 || n3 < 0)
                                        aux.mayorNS = -1;
                                if(r1 < 0 || r2 < 0 || r3 < 0)
                                        aux.mayorS = -1;
                        }
                        else if(v % 3 == 2)
                        {
                                aux.mayorNS = ((v - 2) / 3) + 1;
                                aux.mayorS = ((v - 2) / 3) + 2;

                                n1 = ((v - 2) / 3); n2 = n1 + 1; n3 = n1 + 1;
                                r1 = ((v - 2) / 3); r2 = r1    ; r3 = r1 + 2;

                                if(n1 < 0 || n2 < 0 || n3 < 0)
                                        aux.mayorNS = -1;
                                if(r1 < 0 || r2 < 0 || r3 < 0)
                                        aux.mayorS = -1;
                        }
                        vec.push_back(aux);
                }

                int contador = 0;
                if(N == 1)
                {
                        if(S == 0)
                        {
                                if(vec[0].mayorNS >= p)
                                        contador++;
                        }
                        else if(S == 1)
                        {
                                if(vec[0].mayorS >= p)
                                        contador++;
                        }
                }
                else if(N == 2)
                {
                        if(S == 0)
                        {
                                for(int i=0; i<(int)vec.size(); i++)
                                        if(vec[i].mayorNS >= p)
                                                contador++;
                        }
                        else if(S == 1)
                        {
                                int contador1 = 0;
                                if(vec[0].mayorNS >= p)
                                        contador1++;
                                if(vec[1].mayorS >= p)
                                        contador1++;
                                if(vec[0].mayorNS == -1 || vec[1].mayorS == -1)
                                        contador1 = 0;

                                int contador2 = 0;
                                if(vec[0].mayorS >= p)
                                        contador2++;
                                if(vec[1].mayorNS >= p)
                                        contador2++;
                                if(vec[0].mayorS == -1 || vec[1].mayorNS == -1)
                                        contador2 = 0;

                                contador = max(max(contador,contador1), contador2);
                        }
                        else if(S == 2)
                        {
                                for(int i=0; i<(int)vec.size(); i++)
                                        if(vec[i].mayorS >= p)
                                                contador++;
                        }
                }
                else if(N == 3)
                {
                        if(S == 0)
                        {
                                for(int i=0; i<N; i++)
                                        if(vec[i].mayorNS >= p)
                                                contador++;
                        }
                        else if(S == 1)
                        {
                                int contador1 = 0;
                                if(vec[0].mayorNS >= p)
                                        contador1++;
                                if(vec[1].mayorNS >= p)
                                        contador1++;
                                if(vec[2].mayorS >= p)
                                        contador1++;

                                if(vec[0].mayorNS == -1 || vec[1].mayorNS == -1 || vec[2].mayorS == -1)
                                        contador1 = 0;

                                int contador2 = 0;
                                if(vec[0].mayorNS >= p)
                                        contador2++;
                                if(vec[1].mayorS >= p)
                                        contador2++;
                                if(vec[2].mayorNS >= p)
                                        contador2++;

                                if(vec[0].mayorNS == -1 || vec[1].mayorS == -1 || vec[2].mayorS == -1)
                                        contador2 = 0;

                                int contador3 = 0;
                                if(vec[0].mayorS >= p)
                                        contador3++;
                                if(vec[1].mayorNS >= p)
                                        contador3++;
                                if(vec[2].mayorNS >= p)
                                        contador3++;

                                if(vec[0].mayorS == -1 || vec[1].mayorNS == -1 || vec[2].mayorNS == -1)
                                        contador3 = 0;

                                contador = max(contador1, max(contador2, contador3));
                        }
                        else if(S == 2)
                        {
                                int contador1 = 0;
                                if(vec[0].mayorS >= p)
                                        contador1++;
                                if(vec[1].mayorS >= p)
                                        contador1++;
                                if(vec[2].mayorNS >= p)
                                        contador1++;

                                if(vec[0].mayorS == -1 || vec[1].mayorS == -1 || vec[2].mayorNS == -1)
                                        contador1 = 0;

                                int contador2 = 0;
                                if(vec[0].mayorS >= p)
                                        contador2++;
                                if(vec[1].mayorNS >= p)
                                        contador2++;
                                if(vec[2].mayorS >= p)
                                        contador2++;

                                if(vec[0].mayorS == -1 || vec[1].mayorNS == -1 || vec[2].mayorS == -1)
                                        contador2 = 0;

                                int contador3 = 0;
                                if(vec[0].mayorNS >= p)
                                        contador3++;
                                if(vec[1].mayorS >= p)
                                        contador3++;
                                if(vec[2].mayorS >= p)
                                        contador3++;

                                if(vec[0].mayorNS == -1 || vec[1].mayorS == -1 || vec[2].mayorS == -1)
                                        contador3 = 0;

                                contador = max(contador1, max(contador2, contador3));
                        }
                        else if(S == 3)
                        {
                                for(int i=0; i<N; i++)
                                        if(vec[i].mayorS >= p)
                                                contador++;
                        }
                }
                printf("Case #%d: %d\n",ntest++,contador);
        }
        return 0;
}



