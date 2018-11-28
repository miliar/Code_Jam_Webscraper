#include <cstdio>
#include <cstring>
using namespace std;

const int SIZE = 10009;

int mask[SIZE][26];
char str[SIZE][16];

int group[16][SIZE];
int total[16];
int ans;
int N, M;
int table[SIZE];
int maxdeep;


struct Node
{
    int v;
    Node* next;

    Node* get(int vv, Node* nn)
    {
        v = vv;
        next = nn;
        return this;
    }
}nodes[1024 * 1024];
int loc;

void go(char* q, int s, int e, int deep)
{
//printf("%c %d %d %d\n", *q, s, e, deep);
//fflush(stdout);
    if(deep > maxdeep || (deep == maxdeep && ans > table[s]))
    {
        maxdeep = deep;
        ans = table[s];
    }

    if(e - s <= 1)
        return;

    int idx = *q - 'a';
    Node* table2[1024] = {};

    for(int i = s; i < e; i++)
    {
        int w = table[i];
        int t = mask[w][idx];
        table2[t] = nodes[loc++].get(w, table2[t]);
    }   
    
    int now = 0;
    for(int i = 0; i < 1024; i++)
        if(table2[i])
        {
            int alc = 0;
            for(Node* p = table2[i]; p; p = p->next)
                table[s + now + alc++] = p->v;
//            printf("??%d %d\n", i, alc);

  //          if(alc < e - s)
                go(q + 1, s + now, s + now + alc, deep + (i == 0 && alc != e - s));

            now += alc;
        }
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum  <= T; testnum++)
    {
        scanf("%d%d", &N, &M);

        memset(total, 0, sizeof(total));

        for(int i = 0; i < N; i++)
        {
            scanf("%s", str[i]);

            int len = strlen(str[i]);
            group[len][total[len]++] = i;

            for(int j = 0; j < 26; j++)
            mask[i][j] = 0;
            for(int j = 0; str[i][j]; j++)
                mask[i][str[i][j] - 'a'] |= 1 << j;
        }

        printf("Case #%d:", testnum);

        char query[32];
        while(M--)
        {
            scanf("%s", query);

            maxdeep = -1;
            loc = 0;
            
            for(int len = 1; len <= 10; len++)
                if(total[len])
                {
//                printf("####%d\n", len);
                    for(int i = 0; i < total[len]; i++)
                        table[i] = group[len][i];//, printf("%s\n", str[group[len][i]]);


                    go(query, 0, total[len], 0);
                }
            printf(" %s", str[ans]);
        }
        printf("\n");
    }
    return 0;
}
