#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

char words[11000][15];
int wordslen[11000];
int codes[11000][26];
int cost[11000];
int index[11000];
int bestindex;
int bestvalue;
int n, m;
char buffer[30];
int seq[30];
int currentLetterIndex;

int sortsize(const void *a, const void *b)
{
    return wordslen[*((int*)a)] - wordslen[*((int*)b)];
}

int sortletter(const void *a, const void *b)
{
    return codes[*((int*)a)][currentLetterIndex] - codes[*((int*)b)][currentLetterIndex];
}

void recur(int start, int end, int pos)
{
    //printf("rec(%d, %d, %d)\n", start, end, pos);
    if (end - start == 1)
    {
        if (bestvalue < cost[index[start]])
        {
            bestvalue = cost[index[start]];
            bestindex = index[start];
        }
        else if (bestvalue == cost[index[start]] && bestindex > index[start])
        {
            bestindex = index[start];
        }
        return;
    }
    int i;
    int letter = seq[pos];
    while(true)
    {
        letter = seq[pos];
        for (i = start; i < end; i++)
        {
            if (codes[index[i]][letter] != 0)
            {
                break;
            }
        }
        if (i != end)
            break;
        pos++;
    }
    letter = seq[pos];
    //printf("%c\n", seq[pos] + 'a');
    for (i = start; i < end; i++)
    {
        if (codes[index[i]][letter] == 0)
        {
            cost[index[i]]++;
        }
    }
    currentLetterIndex = letter;
    qsort(&index[start], end - start, sizeof(int), sortletter);
    int beg = start;
    for (i = start + 1; i < end; i++)
    {
        if (codes[index[i-1]][letter] != codes[index[i]][letter])
        {
            recur(beg, i, pos+1);
            beg = i;
        }
    }
    recur(beg, end, pos+1);
}

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        scanf("%d %d", &n, &m);

        int i, j;
        int a;
        for (i = 0; i < n; i++)
        {
            scanf("%s", words[i]);
            int len = strlen(words[i]);
            wordslen[i] = len;
            for (a = 0; a < 26; a++)
            {
                int code = 0;
                for (j = 0; j < len; j++)
                {
                    code = code << 1;
                    if (words[i][j] == a + 'a')
                    {
                        code++;
                    }
                    codes[i][a] = code;
                }
            }
        }

        printf("Case #%d:", t+1);
        for (i = 0; i < m; i++)
        {
            scanf("%s", buffer);
            for (j = 0; j < 26; j++)
            {
                seq[j] = buffer[j] - 'a';
            }
            bestindex = -1;
            bestvalue = -1;
            for (j = 0; j < n; j++)
            {
                cost[j] = 0;
                index[j] = j;
            }
            qsort(index, n, sizeof(int), sortsize);
            int start = 0;
            for (j = 1; j < n; j++)
            {
                if (wordslen[index[j-1]] != wordslen[index[j]])
                {
                    recur(start, j, 0);
                    start = j;
                }
            }
            currentLetterIndex = 0;
            recur(start, n, 0);

            //printf(" %d %s", bestvalue, words[bestindex]);
            printf(" %s", words[bestindex]);
        }
        printf("\n");
    }
    return 0;
}
