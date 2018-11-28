#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_SIZE = 51;

char tablero[MAX_SIZE][MAX_SIZE];

//---------------------------------------------------------------------------
int main(int argc, char* argv[])
{
        FILE *entrada=fopen("A-large.in","r");
        FILE *salida=fopen("salida.txt","w");
        int T;
        char basura;
        fscanf(entrada,"%d%c",&T,&basura);
        char *results[]={"Neither","Red","Blue","Both"};
        for (int t=1;t<=T;t++)
        {
                int N,K;
                int result=0;
                fscanf(entrada,"%d %d%c",&N,&K,&basura);
                for (int i=0;i<N;i++)
                {
                        fscanf(entrada,"%s\n",tablero[i]);
                        int current=N-1;
                        for (int j=N-1;j>=0;j--)
                        {
                                bool moved=false;
                                while (current>=0)
                                {
                                        if (tablero[i][current]!='.')
                                        {
                                                tablero[i][j]=tablero[i][current];
                                                current--;
                                                moved=true;
                                                break;
                                        }
                                        current--;
                                }
                                if (!moved)
                                {
                                        tablero[i][j]='.';
                                }
                        }
                }
                //-
                for (int r=0;r<N;r++)
                {
                        for (int c=K-1;c<N;c++)
                        {
                                if (tablero[r][c]=='.')
                                {
                                        continue;
                                }
                                bool full=true;
                                for (int e=1;e<K;e++)
                                {
                                        if (tablero[r][c-e]!=tablero[r][c])
                                        {
                                                full=false;
                                                break;
                                        }
                                }
                                if (full)
                                {
                                        if (tablero[r][c]=='R')
                                        {
                                                result|=1;
                                        }
                                        else
                                        {
                                                result|=2;
                                        }
                                }
                        }
                }
                //|
                for (int c=0;c<N;c++)
                {
                        for (int r=K-1;r<N;r++)
                        {
                                if (tablero[r][c]=='.')
                                {
                                        continue;
                                }
                                bool full=true;
                                for (int e=1;e<K;e++)
                                {
                                        if (tablero[r-e][c]!=tablero[r][c])
                                        {
                                                full=false;
                                                break;
                                        }
                                }
                                if (full)
                                {
                                        if (tablero[r][c]=='R')
                                        {
                                                result|=1;
                                        }
                                        else
                                        {
                                                result|=2;
                                        }
                                }
                        }
                }
                // 
                for (int c=K-1;c<N;c++)
                {
                        for (int r=K-1;r<N;r++)
                        {
                                if (tablero[r][c]=='.')
                                {
                                        continue;
                                }
                                bool full=true;
                                for (int e=1;e<K;e++)
                                {
                                        if (tablero[r-e][c-e]!=tablero[r][c])
                                        {
                                                full=false;
                                                break;
                                        }
                                }
                                if (full)
                                {
                                        if (tablero[r][c]=='R')
                                        {
                                                result|=1;
                                        }
                                        else
                                        {
                                                result|=2;
                                        }
                                }
                        }
                }
                // /
                for (int c=0;(c+K)<=N;c++)
                {
                        for (int r=K-1;r<N;r++)
                        {
                                if (tablero[r][c]=='.')
                                {
                                        continue;
                                }
                                bool full=true;
                                for (int e=1;e<K;e++)
                                {
                                        if (tablero[r-e][c+e]!=tablero[r][c])
                                        {
                                                full=false;
                                                break;
                                        }
                                }
                                if (full)
                                {
                                        if (tablero[r][c]=='R')
                                        {
                                                result|=1;
                                        }
                                        else
                                        {
                                                result|=2;
                                        }
                                }
                        }
                }
                fprintf(salida,"Case #%d: %s\n",t,results[result]);
        }

        fclose(entrada);
        fclose(salida);
        return 0;
}
//---------------------------------------------------------------------------

