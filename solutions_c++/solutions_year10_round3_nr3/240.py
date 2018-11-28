#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef struct MatCnt
{
    int size;
    int count;
} MatCnt;

int FoundMax(vector < vector <int> > & mat, vector < vector <int> > & matSize)
{
    int maxSize = 0;
    int maxi, maxj;

    for (unsigned i=0; i<mat.size(); i++)
    {
        for (unsigned j=0; j<mat[0].size(); j++)
        {
            while (matSize[i][j] > 1)
            {
                bool isOK = (mat[i][j] != -1);
                for (int k=1; isOK && k<matSize[i][j]; k++)
                {
                    if (mat[i][j+k] == -1 ||
                        mat[i][j+k] == mat[i][j+k-1])
                    {
                        isOK = false;
                    }
                }
                for (int k=1; isOK && k<matSize[i][j]; k++)
                {
                    for (int l=0; isOK && l<matSize[i][j]; l++)
                    {
                        if (mat[i+k][l+j] == -1 ||
                            mat[i+k][l+j] == mat[i+k-1][l+j])
                        {
                            isOK = false;
                        }
                    }
                }
                if (isOK == true)
                {
                    break;
                }
                matSize[i][j]--;
            }
            if (maxSize < matSize[i][j])
            {
                maxSize = matSize[i][j];
                maxi = i;
                maxj = j;
            }
        }
    }

    for (int k=0; k<maxSize; k++)
    {
        for (int l=0; l<maxSize; l++)
        {
            mat[maxi+k][maxj+l] = -1;
        }
    }

    return maxSize;
}

void AddList(int size, vector <MatCnt> & res)
{
    for (unsigned i=0; i<res.size(); i++)
    {
        if (res[i].size == size)
        {
            res[i].count++;
            return;
        }
    }
    MatCnt mc;
    mc.size = size;
    mc.count = 1;
    res.push_back(mc);
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
        int M, N;
        vector < vector <int> > mat;
        vector < vector <int> > matSize;
        vector <int> line;
        vector <MatCnt> res;
        char sLine[200];
        fscanf(fin, "%d %d", &M, &N);
        for (int j=0; j<M; j++)
        {
            line.clear();
            fscanf(fin, "%s", sLine);
            for (int k=0; k<N/4; k++)
            {
                int tmp = sLine[k] - '0';
                if (tmp > 9)
                {
                    tmp = sLine[k] - 'A' + 10;
                }
                line.push_back(tmp / 8);
                tmp %= 8;
                line.push_back(tmp / 4);
                tmp %= 4;
                line.push_back(tmp / 2);
                tmp %= 2;
                line.push_back(tmp);
            }
            mat.push_back(line);
        }
        matSize.resize(M);
        for (int j=0; j<M; j++)
        {
            matSize[j].resize(N);
            int leftRow = M - j;
            for (int k=0; k<N; k++)
            {
                int leftCol = N - k;
                matSize[j][k] = leftRow < leftCol ? leftRow : leftCol;
            }
        }

        /* Show-Begin */
        /*
        for (int j=0; j<M; j++)
        {
            for (int k=0; k<N; k++)
            {
                cout << mat[j][k];
            }
            cout << endl;
        }
        */
        /* Show-End */

        int area = M * N;
        int cur;
        while (area && (cur = FoundMax(mat, matSize)) >= 2)
        {
            AddList(cur, res);
            area -= cur * cur;
        }
        if (area > 0)
        {
            MatCnt mc;
            mc.size = 1;
            mc.count = area;
            res.push_back(mc);
        }
        

        /* Show-Begin */
        /*
        for (int j=0; j<M; j++)
        {
            for (int k=0; k<N; k++)
            {
                cout << mat[j][k];
            }
            cout << endl;
        }
        */
        /* Show-End */


        fprintf(fout, "%d\n", res.size());
        for (unsigned j=0; j<res.size(); j++)
        {
            fprintf(fout, "%d %d\n", res[j].size, res[j].count);
        }
    }
    

    /* 关闭文件 */
    fclose(fin);
    fclose(fout);
    return 0;
}
