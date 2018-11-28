#include <iostream>
#include <sstream>
#include <map>
#include <math.h>
#include <string>
#include <stdio.h>
#include <vector>
#include <list>
#include <set>

using namespace std;

int getTriangleCount(FILE *inputFile)
{
    int triangleCount = 0;
    long int n,A, B, C, D, x0, y0, M;

    fscanf(inputFile, "%ld%ld%ld%ld%ld%ld%ld%ld\n", &n, &A, &B, &C, &D, &x0, &y0, &M);

    printf("%ld %ld %ld %ld %ld %ld %ld %ld\n",n, A, B, C, D, x0, y0, M);
    long long int *x = (long long int*) malloc(sizeof(long long int) * n);
    long long int *y = (long long int*) malloc(sizeof(long long int) * n);
    
    x[0] = x0;
    y[0] = y0;

    cout<<"x[0] " << x[0] << " y[0]" << y[0] <<endl;
    for(int i = 1; i < n; i++)
    {
        stringstream newStrStream;

        x[i] = ((long long)A * x[i-1] + B) % M;
        y[i] = ((long long)C * y[i-1] + D) % M;
        cout<<"x[i] " << x[i] << " y[i]" << y[i] <<endl;
    }

    for(int i = 0; i < n - 2; i++)
    {
        for(int j = i + 1; j < n -1; j++)
        {
            for(int k = j +1; k < n; k++)
            {
                long int cenX = (x[i] + x[j] + x[k]) /3;
                long int cenY = (y[i] + y[j] + y[k]) /3;
                
                long int redX = (x[i] + x[j] + x[k]) %3;
                long int redY = (y[i] + y[j] + y[k]) %3;
                if(redY == 0 && redX == 0)
                {
                    triangleCount++;
                }
            }
        }
    }

    delete x;
    delete y;
    return triangleCount;
}

void runTestCase(FILE *inputFile, FILE* outFile)
{
    int i = 0;

    int testCaseCount = 0;
    fscanf(inputFile, "%d", &testCaseCount);
    //printf("Testcase count is %d\n", testCaseCount);

    i = 1;
    for(;i <= testCaseCount; i++)
    {
        int triangleCount= 0;

        //printf("-------Handling testcase %d--------\n", i);
        
        triangleCount = getTriangleCount(inputFile);
        //cout<< "TargetNumber = " << targetNumber<< "\n";

        fprintf(outFile, "Case #%d: %d\n", i, triangleCount);
    }

}

int main(int argc, const char** argv)
{
    if(argc < 3)
    {
        printf("Wrong number of arguments. Usage: universe input_filename output_filename \n");
    }

    FILE* inputFile = fopen(argv[1], "r");
    FILE *outFile = fopen(argv[2], "w");

    if(NULL != inputFile )
    {
        if(NULL != outFile)
        {
            runTestCase(inputFile, outFile);
            fclose(outFile);
        }

        fclose(inputFile);
    }
    else if(NULL != outFile)
    {
            fclose(outFile);
    }

    return 0;
}
