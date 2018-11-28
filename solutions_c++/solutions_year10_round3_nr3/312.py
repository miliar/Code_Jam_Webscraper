#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <set>
#include <cmath>

using namespace std;

int getSize(int i, int j, int M, int N, int Board[35][35])
{
    int size=1;
    bool bisa = true;
    
    while (bisa)
    {
        size++;
        if (j+size-1>=N || i+size-1>=M)
        {
            size--;
            bisa = false;
            break;
        }
        if (bisa)
        {
            for (int x=i; x<(i+size-1) && bisa; x++)
                if (!( (Board[x][j+size-1]==0 && Board[x][j+size-2]==1) ||
                       (Board[x][j+size-1]==1 && Board[x][j+size-2]==0)
                    ))
                    bisa = false;
            
            if (bisa)
            {
                for (int x=j; x<(j+size) && bisa; x++)
                    if (!( (Board[i+size-1][x]==0 && Board[i+size-2][x]==1) ||
                           (Board[i+size-1][x]==1 && Board[i+size-2][x]==0)
                        ))
                        bisa = false;
            ;
            }
            if (!bisa) size--;
        }
    }
    
    //printf("%d %d %d\n", i, j, size);
    return size;
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for (int test=1; test<=T; test++)
    {
        int M, N;
        int Board[35][35];
        
        scanf("%d%d", &M, &N);
        for (int i=0; i<M; i++)
        {
            char temp[50] = {};
            int ct=N-1;
            scanf("%s", temp);
            for (int j=(N/4)-1; j>=0; j--)
            {
                int x;
                if (temp[j]>='0' && temp[j]<='9') x = temp[j]-'0';
                else if (temp[j]>='A' && temp[j]<='Z') x = temp[j]-'A'+10;
                
                int haha=0;
                while (x>0)
                {
                    Board[i][ct] = (x%2);
                    x/=2;
                    ct--;
                    haha++;
                }
                while(haha<4)
                {
                    Board[i][ct] = 0;
                    ct--;
                    haha++;
                }
            }
        }
        
        /*
        for (int i=0; i<M; i++)
        {
            for (int j=0; j<N; j++)
                printf("%d", Board[i][j]);
            printf("\n");
        }
        printf("-\n");
        */
        
        int Size[270000] = {};
        
        int ada=true;
        while (ada)
        {
            ada=false;
            int MxSize=0;
            int a, b;
            for (int i=0; i<M; i++)
            {
                for (int j=0; j<N; j++)
                {
                    if (Board[i][j]<2)
                    {
                        ada = true;
                        int szTemp = getSize(i,j,M,N, Board);
                        if (MxSize<szTemp)
                        {
                            a=i;
                            b=j;
                            MxSize=szTemp;
                        }
                        /*for (int a=0; a<M; a++)
                        {
                            for (int b=0; b<N; b++)
                                printf("%d", Board[a][b]);
                            printf("\n");
                        }
                        printf("-\n");*/
                    }
                }
            }
            if (ada)
            {
                for (int x=a; x<(a+MxSize); x++)
                    for (int y=b; y<(b+MxSize); y++)
                        Board[x][y] = 2;
                (Size[MxSize])++;
            }
            
            /*
            for (int a=0; a<M; a++)
            {
                for (int b=0; b<N; b++)
                    printf("%d", Board[a][b]);
                printf("\n");
            }
            printf("-\n");
            */
        }
        int Ans = 0;
        for (int i=(M*N); i>=1; i--)
            if (Size[i]>0) Ans++;
            
        printf("Case #%d: %d\n", test, Ans);
        for (int i=(M*N); i>=1; i--)
            if (Size[i]>0)
                printf("%d %d\n", i, Size[i]);
                
    }
    
    return 0;
}
