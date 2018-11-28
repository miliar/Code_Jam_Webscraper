#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX 128
char b[MAX][MAX],s[MAX][MAX];

int main(void)
{
    int caso,C;
    int N,K;

    for(caso = 1, scanf("%d",&C); caso <= C; caso++)
    {
        scanf("%d %d",&N,&K);
        for(int i = 0; i < N; i++)
            scanf("%s",b[i]);

        memset(s,0,sizeof(s));
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                s[i][j] = b[N-j-1][i];

        for(int j = 0; j < N; j++)
            for(int i = N-1; i >= 0; i--)
                for (int c = 0; s[i][j] == '.' && c <= N; c++)
                {
                    for(int k = i-1; k >= 0; k--)
                        s[k+1][j] = s[k][j];
                    s[0][j] = '.';
                }

        /*
        for(int i = 0; i < N; i++)
            printf("%s\n",s[i]);
        */

        bool blue,red;
        blue = red = false;

        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                if (s[i][j] == 'B')
                {
                    int c = 0;
                    for(c = 0; j+c < N && s[i][j+c] == 'B'; c++);
                    if (c >= K) blue = true;
                    for(c = 0; i+c < N && s[i+c][j] == 'B'; c++);
                    if (c >= K) blue = true;
                    for(c = 0; i+c < N && j+c < N && s[i+c][j+c] == 'B'; c++);
                    if (c >= K) blue = true;
                    for(c = 0; i+c < N && j-c >= 0 && s[i+c][j-c] == 'B'; c++);
                    if (c >= K) blue = true;
                }
                else if (s[i][j] == 'R')
                {
                    int c = 0;
                    for(c = 0; j+c < N && s[i][j+c] == 'R'; c++);
                    if (c >= K) red = true;
                    for(c = 0; i+c < N && s[i+c][j] == 'R'; c++);
                    if (c >= K) red = true;
                    for(c = 0; i+c < N && j+c < N && s[i+c][j+c] == 'R'; c++);
                    if (c >= K) red = true;
                    for(c = 0; i+c < N && j-c >= 0 && s[i+c][j-c] == 'R'; c++);
                    if (c >= K) red = true;
                }

        printf("Case #%d: %s\n",caso,blue ? (red ? "Both" : "Blue") : (red ? "Red" : "Neither"));
    }

    return(0);
}

