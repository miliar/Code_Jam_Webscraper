#include <stdio.h>
#include <string.h>

#define M 19

struct Info
{
    char ch;
    int len;
    int pos[100];
    int num[100];
};

int N;
char str[100][500];
struct Info info[M];

int process(char *str);
int sum(int index, int from);

int main()
{
    int i;
    char tmp[] = "welcome to code jam";
    for (i = 0; i < M; i++)
    {
        info[i].ch = tmp[i];
    }
    
    scanf("%d\n", &N);
    for (i = 0; i < N; i++)
    {
        gets(str[i]);
    }
    
    for(i = 0; i < N; i++)
    {
        int re;
        re = process(str[i]);
        printf("Case #%d: %04d\n", i + 1, re);
    }
    
    return 0;
    
    return 0;
}

int process(char *str)
{
    int i, count;
    for (i = 0; i < M; i++)
    {
        info[i].len = 0;
        memset(info[i].pos, 0, sizeof(info[i].pos));
        memset(info[i].num, 0, sizeof(info[i].num));
    }

    i = 0;
    count = 0;    
    while (str[i] != 0)
    {
        if (str[i] == info[M - 1].ch)
        {
            info[M - 1].pos[count] = i;
            info[M - 1].num[count] = 1;
            count++;
        }
        i++;
    }
    info[M - 1].len = count;
    
    for (int k = M - 2; k >=0; k--)
    {
        i = 0;
        count = 0;
        while (str[i] != 0)
        {
            if (str[i] == info[k].ch)
            {
                for (int j = 0; j < info[k + 1].len; j++)
                {
                    if (i < info[k + 1].pos[j])
                    {
                        info[k].num[count] = sum(k + 1, j);
                        info[k].pos[count] = i;
                        count++;
                        break;
                    }
                }
            }
            i++;
        }
        info[k].len = count;
    }
    
    return sum(0, 0);
}

int sum(int index, int from)
{
    int s = 0;
    for (int i = from; i < info[index].len; i++)
        s += info[index].num[i];
    
    return s % 10000;
}
