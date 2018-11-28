#include <stdio.h>
#include <assert.h>
#include <string.h>

int T;              // no of test cases

int C;              // no of points
int point[200];     // position of the point
int vendors[200];   // no. of vendors at the point
int D;              // min needed distance between the vendors

float calcMinTime()
{
    // calculate min time needed;
    float time=0;

    for(int i=0;i<C;i++)
    {
        for(int j=i;j<C;j++)
        {

            int totalVendorsInSegment=0;
            float distanceInSegment = point[j] - point[i];
            for (int k=i;k<=j;k++)
                totalVendorsInSegment += vendors[k];

            float segmentTime = (totalVendorsInSegment - 1 - distanceInSegment/D) * D / 2.0f;
            if(segmentTime > time) time = segmentTime;

        }
    }
    return time;
}

int main()
{
    FILE *fp = fopen("c:\\inp.txt", "r+"); // get input data from file
    fscanf(fp, "%d", &T);

    FILE *fpo = fopen("c:\\op.txt", "w+"); // write op data to file

    for(int c=1;c<=T;c++)    // process each test case
    {
        fscanf(fp, "%d %d", &C, &D);
        for(int i=0;i<C;i++)
            fscanf(fp, "%d %d", &point[i], &vendors[i]);

        float time = calcMinTime();

        fprintf(fpo, "Case #%d: %f\n", c, time);
    }

    fclose(fp);
    fclose(fpo);
    return 0;
}

