#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char strD[5000][16];
char strN[28 * 15 + 1];
char symbol[15][26];
int L, D, N;
int count;

struct Node
{
    struct Node *child[26];
};

int analyze();
struct Node * create_tree();
int destroy_tree(struct Node *pNode);
int find(int i, struct Node *pNode);

int main()
{
    int i;
    
    scanf("%d %d %d\n", &L, &D, &N);
    for (i = 0; i < D; i++)
    {
        gets(strD[i]);
    }
    
    struct Node *pRoot = create_tree();
    
    for (i = 0; i < N; i++)
    {
        gets(strN);
        analyze();
        count = 0;
        find(0, pRoot);
        printf("Case #%d: %d\n", i + 1, count);
    }
    
    destroy_tree(pRoot);
    pRoot = NULL;
    
    return 0;
}

struct Node * create_tree()
{
    struct Node *pRoot = NULL;
    struct Node *pCur = NULL;
    pRoot =(struct Node *)malloc(sizeof(struct Node));
    memset(pRoot, 0, sizeof(struct Node));
    
    for (int i = 0; i < D; i++)
    {
        pCur = pRoot;
        int j = 0;
        while (strD[i][j] != 0)
        {
            if (pCur->child[strD[i][j] - 'a'] == NULL)
            {
                pCur->child[strD[i][j] - 'a'] = (struct Node *)malloc(sizeof(struct Node));
                memset(pCur->child[strD[i][j] - 'a'], 0, sizeof(struct Node));  
            };
            pCur = pCur->child[strD[i][j] - 'a'];
            j++;
        }
    }
    
    return pRoot;
}

int destroy_tree(struct Node *pNode)
{
    for (int i = 0; i < 26; i++)
    {
        if (pNode->child[i] != NULL)
        {
            destroy_tree(pNode->child[i]);
            pNode->child[i] = 0;
        }
    }
    
    free(pNode);
    
    return 0;
}

int analyze()
{
    int index = 0, count = 0;
    int i = 0;
    
    for (i = 0; i < L; i++)
        symbol[i][0] = 0;

    i = 0;
    while (strN[i] != 0)
    {
        if (strN[i] == '(')
        {
            i++;
            while (strN[i] != ')')
            {
                symbol[index][count] = strN[i];
                count++;
                i++;
            }
            symbol[index][count] = 0;
            count = 0;
        }
        else
        {
            symbol[index][0] = strN[i];
            symbol[index][1] = 0;
        }
        index++;
        i++;
    }
    
//    for (int i = 0; i < L; i++)
//    {
//        int j = 0;
//        while (symbol[i][j] != 0)
//        {
//            printf("%c ", symbol[i][j]);
//            j++;
//        }
//        printf("\n");
//    }

    return 0;
}

int find(int i, struct Node *pNode)
{
    if (i == L)
    {
        count++;
    }
    else
    {
        int j = 0;
        while (symbol[i][j] != 0)
        {
            if (pNode->child[symbol[i][j] - 'a'] != NULL)
            {
                find(i + 1, pNode->child[symbol[i][j] - 'a']);
            }
            j++;
        }
    }
}
