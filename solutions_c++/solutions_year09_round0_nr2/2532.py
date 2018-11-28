#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int record[100 * 100][2];
int rd_len;
int N;
int H, W;
char next_ch;


int process(int count);
int mark(int * pData, char *pMark, int i, int j);

int main()
{
    scanf("%d\n", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d %d\n", &H, &W);
        process(i);
    }
    return 0;
}

int process(int count)
{
    int i, j;
    int *pData = NULL;
    char *pMark = NULL;
    
    pData = (int *)malloc(H * W * sizeof(int));
    pMark = (char *)malloc(H * W * sizeof(char));
    
    for (i = 0; i < H * W; i++)
    {
        scanf("%d", &pData[i]);
        pMark[i] = 0;
    }
    memset(pMark, 0, H * W * sizeof(char));
    
    next_ch = 'a';
    for (i = 0; i < H; i++)
        for(j = 0; j < W; j++)
        {
            if (pMark[i * W + j] == 0)
            {
                mark(pData, pMark, i, j); 
            };
        }
    
    printf("Case #%d:\n", count + 1);
    for (i = 0; i < H; i++)
    {
        for(j = 0; j < W; j++)
            printf("%c ", pMark[i * W + j]);
        printf("\n");
    }
    
    free(pData);
    free(pMark);
    
    return 0;
}

int mark(int * pData, char *pMark, int i, int j)
{
    int next_i = i, next_j = j;
    int min = 32767;
    
    if (i - 1 >= 0 && pData[(i - 1) * W + j] < min)
    {
        min = pData[(i - 1) * W + j];
        next_i = i - 1;
        next_j = j;
    }
    
    if (j - 1 >= 0 && pData[i * W + j - 1] < min) 
    {
        min = pData[i * W + j - 1];
        next_i = i;
        next_j = j -1;
    }
    if (j + 1 < W && pData[i * W + j + 1] < min) 
    {
        min = pData[i * W + j + 1];
        next_i = i;
        next_j = j + 1;
    }
    if (i + 1 < H && pData[(i + 1) * W + j] < min) 
    {
        min = pData[(i + 1) * W + j];
        next_i = i + 1;
        next_j = j;
    }
    
    if (min >= pData[i * W + j])
    {
        // it is a sink
        pMark[i * W + j] = next_ch;
        for(int k = rd_len - 1; k >= 0; k--)
        {
            pMark[record[k][0] * W + record[k][1]] = pMark[i * W + j];
        }
        next_ch ++;
        rd_len = 0;
    }
    else
    {
        if (pMark[next_i * W + next_j] != 0)
        {
            pMark[i * W + j] = pMark[next_i * W + next_j];
            for(int k = rd_len - 1; k >= 0; k--)
            {
                pMark[record[k][0] * W + record[k][1]] = pMark[i * W + j];
            }
            rd_len = 0;
        }
        else
        {
            record[rd_len][0] = i;
            record[rd_len][1] = j;
            rd_len++;
            mark(pData, pMark, next_i, next_j);
        }
    }
    
    return 0;
}
