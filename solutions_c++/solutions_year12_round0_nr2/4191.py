#include <iostream>
#include <string.h>
#include <windows.h>
#include <stdio.h>

using namespace std;


int N,S,p,R;
int G[1000];

int find(char* str,char chr);

int main()
{
    	FILE *fin  = fopen ("in", "r");

	FILE *fout = fopen ("out", "w");

int T;
	fscanf( fin, " %d", &T);

	for (int i=0;i<T;i++)
        {
            R=0;
            fscanf( fin, " %d", &N);
            fscanf( fin, " %d", &S);
            fscanf( fin, " %d", &p);
            for (int i=0;i<N;i++)
                {
                   fscanf( fin, " %d", &G[i]);
                }
            for (int i=0;i<N;i++)
                {
                    if (G[i] >= p)
                       {
                             if  ((G[i]-p) >= (p*2 )-2 )
                                 {
                                     R++;
                                 }
                             else if ( (G[i]-p) >= (p*2 )-4    && S!=0 )
                                     {
                                          R++;
                                          S--;
                                     }
                       }
                }

            fprintf (fout, "Case #%d: %d\n",i+1,R);
        }
    return 0;
}
int find(char* str,char chr)
{
    int len=lstrlen(str);
    for(int i=0;i<len;i++)
       {
           if (str[i]==chr)
              {
                  return i;
              }
       }
    return -1;
}
