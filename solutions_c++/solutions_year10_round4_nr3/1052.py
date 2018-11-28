#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define SMALL_DIFF  0.0000001

typedef struct Rect
{
    int x1, y1, x2, y2;
} Rect;

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

    for (int i=0; i<caseNum; i++)
    {
        fprintf(fout, "Case #%d: ", i+1);

        int R;
        Rect rect;
        vector <Rect> vRect;
        vector < vector <int> > map;
        fscanf(fin, "%d", &R);
        int maxX = 0;
        int maxY = 0;
        for (int j=0; j<R; j++)
        {
            fscanf(fin, "%d %d %d %d", &rect.x1, &rect.y1, &rect.x2, &rect.y2);
            vRect.push_back(rect);
            maxX = maxX < rect.x2 ? rect.x2 : maxX;
            maxY = maxY < rect.y2 ? rect.y2 : maxY;
        }
        map.resize(maxY+1);
        for (unsigned j=0; j<map.size(); j++)
        {
            map[j].resize(maxX+1);
            for (unsigned k=0; k<map[j].size(); k++)
            {
                map[j][k] = 0;
            }
        }

        int count = 0;

        for (unsigned j=0; j<vRect.size(); j++)
        {
            for (int m=vRect[j].y1; m<=vRect[j].y2; m++)
            {
                for (int n=vRect[j].x1; n<=vRect[j].x2; n++)
                {
                    if (0 == map[m][n])
                    {
                        map[m][n] = 1;
                        count++;
                    }
                }
            }
        }
        
        int time = 0;
        while (count)
        {
            time++;
            for (int m=maxY; m>=1; m--)
            {
                for (int n=maxX; n>=1; n--)
                {
                    if (map[m][n-1] && map[m-1][n] && !map[m][n])
                    {
                        map[m][n] = 1;
                        count++;
                    }
                }
            }
            for (int m=maxY; m>=1; m--)
            {
                for (int n=maxX; n>=1; n--)
                {
                    if (map[m][n] && !map[m][n-1] && !map[m-1][n])
                    {
                        map[m][n] = 0;
                        count--;
                    }
                }
            }
        }
        fprintf(fout, "%d\n", time);
    }

    /* 关闭文件 */
    fclose(fin);
    fclose(fout);
    return 0;
}
