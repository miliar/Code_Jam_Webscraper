#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define SMALL_DIFF  0.0000001

typedef struct Point
{
    double x, y;
} Point;

int AddPoint(vector <Point> & vPt, Point pt)
{
    for (unsigned i=0; i<vPt.size(); i++)
    {
        if (abs(vPt[i].x - pt.x) < SMALL_DIFF &&
            abs(vPt[i].y - pt.y) < SMALL_DIFF)
        {
            return vPt.size();
        }
    }
    vPt.push_back(pt);
    return vPt.size();
}

Point calcPoint(int x1, int x2, int y1, int y2)
{
    Point pt;
    pt.x = -1;
    pt.y = -1;

    if ((x1 - x2) * (y1 - y2) >= 0)
        return pt;
        
    pt.y = abs((double)(x1 - x2) / (y1 - y2));
    pt.x = x1 + (y1-x1) * pt.y / (pt.y + 1);
    return pt;
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

    for (int i=0; i<caseNum; i++)
    {
        fprintf(fout, "Case #%d: ", i+1);
        int num;
        fscanf(fin, "%d", &num);
        vector <int> A;
        vector <int> B;
        vector <Point> vPt;
        int a, b;
        for (int j=0; j<num; j++)
        {
            fscanf(fin, "%d %d", &a, &b);
            A.push_back(a);
            B.push_back(b);
        }
        
        for (int j=0; j<num-1; j++)
        {
            for (int k=j+1; k<num; k++)
            {
                Point pt = calcPoint(A[j], A[k], B[j], B[k]);
                if (pt.x > 0)
                    AddPoint(vPt, pt);
            }
        }
        fprintf(fout, "%d\n", vPt.size());
    }

    /* 关闭文件 */
    fclose(fin);
    fclose(fout);
    return 0;
}
