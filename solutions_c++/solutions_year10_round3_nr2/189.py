#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std;

inline long long Power(long long C, int n)
{
    long long res = 1;
    while (n > 0)
    {
        res *= C;
        n--;
    }
    return res;
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
        long long L, P, C;
        fscanf(fin, "%lld %lld %lld", &L, &P, &C);
        long long t = L * C;
        int power = 0;
        while (t < P)
        {
            t *= C;
            power++;
        }
        int cnt = 0;
        while (power > 0)
        {
            cnt++;
            power /= 2;
        }
        fprintf(fout, "%d\n", cnt); 
    }
    

    /* 关闭文件 */
    fclose(fin);
    fclose(fout);
    return 0;
}
