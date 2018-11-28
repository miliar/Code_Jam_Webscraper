/* 
 * File:   main.cpp
 * Author: lolo
 *
 * Created on May 22, 2010, 8:05 AM
 */

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define MAX 55

int T,N,K;
char grid[MAX][MAX];
char rotated[MAX][MAX];
char fallen[MAX][MAX];

int main(int argc, char** argv) {
    freopen("A-large.in","r",stdin);
    freopen("output_large.txt","w",stdout);
    scanf("%d",&T);
    int caseID = 0;
    while (T--){
        scanf("%d %d",&N, &K);
        for (int i = 0; i < N; i++)
            scanf("%s",grid[i]);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++){
                rotated[i][j] = grid[N-1-j][i];
                fallen[i][j] = '.';
            }
        /*for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++)
                printf("%c",rotated[i][j]);
                    printf("\n");
        }*/
        //printf("sep\n");
        //fall
        //for each column
        for (int col = 0; col < N; col++){
            int fRow = N-1;
            for (int row = N-1; row >= 0; row--)
                if (rotated[row][col] != '.')
                    fallen[fRow--][col] = rotated[row][col];
        }
        //done
        /*for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++)
                printf("%c",fallen[i][j]);
                    printf("\n");
        }*/
        bool red = false, blue = false;
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (fallen[i][j] != '.'){
                    int k = 1;
                    int di = i, dj = j;
                    char cmp = fallen[i][j];
                    while (di+1 < N && fallen[di+1][j] == cmp) di++,k++;
                    if (k >= K){
                        if (cmp == 'R') red = true;
                        else blue = true;
                    }
                    di = i, dj = j, k = 1;
                    while (dj + 1 < N && fallen[di][dj+1] == cmp) dj++,k++;
                    if (k >= K){
                        if (cmp == 'R') red = true;
                        else blue = true;
                    }
                    di = i, dj = j, k = 1;
                    while (dj + 1 < N && di + 1 < N && fallen[di+1][dj+1] == cmp) dj++,di++,k++;
                    if (k >= K){
                        if (cmp == 'R') red = true;
                        else blue = true;
                    }
                    di = i, dj = j, k = 1;
                    while (dj - 1 >= 0 && di + 1 < N && fallen[di+1][dj-1] == cmp) dj--,di++,k++;
                    if (k >= K){
                        if (cmp == 'R') red = true;
                        else blue = true;
                    }
                }
        if (red && blue)
            printf("Case #%d: Both\n",++caseID);
        else if (!red && !blue)
            printf("Case #%d: Neither\n",++caseID);
        else if (red)
            printf("Case #%d: Red\n",++caseID);
        else printf("Case #%d: Blue\n",++caseID);

    }
    return (EXIT_SUCCESS);
}

