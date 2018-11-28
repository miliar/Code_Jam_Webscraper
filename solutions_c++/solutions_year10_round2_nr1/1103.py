#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define LEN 100

typedef struct tag_DIR
{
    struct tag_DIR * first;
    struct tag_DIR * brother;
    char name[LEN];
} Dir_S;

Dir_S g_root;

int Get(char * line, char * cur)
{
    if ('/' != *line)
    {
        return 0;
    }
    line++;
    int res = 0;
    while (line[res] != 0 && line[res] != '/')
    {
        cur[res] = line[res];
        res++;
    }
    cur[res] = 0;
    return res+1;
}

int Add(char * line)
{
    int count = 0;
    char cur[LEN];
    int shift = 0;
    Dir_S * pNode = &g_root;
    while (0 != (shift = Get(line, cur)))
    {
        line += shift;
        Dir_S * p = pNode->first;
        while (p)
        {
            if (0 == strcmp(cur, p->name))
            {
                break;
            }
            p = p->brother;
        }
        if (NULL == p)
        {
            count++;
            p = (Dir_S *) malloc(sizeof(Dir_S));
            strcpy(p->name, cur);
            p->first = 0;
            p->brother = pNode->first;
            pNode->first = p;
        }
        pNode = p;
    }
    return count;
}

void Free(Dir_S * pNode)
{
    Dir_S * p = pNode->first;
    while (p)
    {
        Free(p);
        p = p->brother;
    }
    free(pNode);
}

int main(int argc, char * argv[])
{
    /* 打开输入文件 */
    FILE * fin = NULL;
    if (argc < 2 || NULL == (fin = fopen(argv[1], "r")))
    {
        printf("Input File Not Exist!\n");
        return 1;
    }

    /* 打开输出文件 */
    char output[100];
    sprintf(output, "%s.out", argv[1]);
    FILE * fout = fopen(output, "w");

    /* 读入测试用例数 */
    int caseNum;
    fscanf(fin, "%d", &caseNum);

    strcpy(g_root.name, "/");
    g_root.brother = NULL;

    char line[LEN];
    for (int i=0; i<caseNum; i++)
    {
        g_root.first = NULL;
        int N, M;
        int mkCnt = 0;
        fscanf(fin, "%d %d", &N, &M);
        for (int j=0; j<N; j++)
        {
            memset(line, 0, LEN);
            fscanf(fin, "%s", line);
            Add(line);
        }
        for (int j=0; j<M; j++)
        {
            fscanf(fin, "%s", line);
            mkCnt += Add(line);
        }
        fprintf(fout, "Case #%d: %d\n", i+1, mkCnt);
//      Free(g_root.first);
    }

    /* 关闭文件 */
    fclose(fin);
    fclose(fout);
    return 0;
}
