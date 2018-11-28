
#include <stdio.h>
#include <string.h>
#include <map>
#include <list>
#include <set>
#include <string>
#include <vector>

#define MAX_H 100
#define MAX_W 100

int H, W;
int attitude[MAX_H][MAX_W] = {0};
char parent[MAX_H][MAX_W] = {0};
char id;


char findParent(int h, int w)
{
    int min_attitude = attitude[h][w];    
    int min_direction = 0;
    int j = h, i = w;

    if (parent[j][i])
    {
        return parent[j][i];
    }

     //four directions:1,North; 2,West; 3,East; 4,South
    //north
    if (j > 0 && min_attitude > attitude[j-1][i])
    {
        min_direction = 1;
        min_attitude = attitude[j-1][i];
    }
    //west
    if (i > 0 && min_attitude > attitude[j][i-1])
    {
        min_direction = 2;
        min_attitude = attitude[j][i-1];
    }
    //east
    if (i < W - 1 && min_attitude > attitude[j][i+1])
    {
        min_direction = 3;
        min_attitude = attitude[j][i+1];
    }
    //south
    if (j < H - 1 && min_attitude > attitude[j+1][i])
    {
        min_direction = 4;
        min_attitude = attitude[j+1][i];
    }

    switch(min_direction)
    {
    case 0:
        parent[j][i] = id ++;
        break;
    case 1:
        parent[j][i] = findParent(j-1, i);
        break;
    case 2:
        parent[j][i] = findParent(j, i-1);
        break;
    case 3:
        parent[j][i] = findParent(j, i+1);
        break;
    case 4:
        parent[j][i] = findParent(j+1, i);
        break;
    }

    return parent[j][i];
}

void GCJ_2009Qulification2(const char*input, const char*output)
{
    FILE* fin = freopen(input, "rb", stdin);
    FILE* fout = freopen(output, "wb", stdout);

    int N, ncase = 0;
    scanf("%d", &N);

    while (ncase ++ < N)
    {
        //run one test case
        scanf("%d %d", &H, &W);
        for (int j = 0; j < H; j ++)
        {
            for (int i = 0; i < W; i ++)
            {
                scanf("%d", &attitude[j][i]);
                parent[j][i] = 0;
            }
        }

        //search using union set searching
        id = 'a';
        for (int j = 0; j < H; j ++)
        {
            for (int i = 0; i < W; i ++)
            {
                findParent(j, i);
            }
        }

        //output the results
        printf("Case #%d:\n", ncase);
        for (int j = 0; j < H; j ++)
        {
            for (int i = 0; i < W; i ++)
            {
                printf("%c ", parent[j][i]);
            }
            printf("\n");
        }
    }

    fclose(fin);
    fclose(fout);


}
int main(int argc, char** argv)
{
    char*in_file = "gcj.in";
    char*out_file = "gcj.out";

    GCJ_2009Qulification2(in_file, out_file);


    return 0;
}