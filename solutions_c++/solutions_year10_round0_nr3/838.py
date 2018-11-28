#include<cstdio>

#define _out "out-large.txt"
#define _in  "C-large.in"

int main(int argc, void* argv[])
{
    FILE *fin, *fout;

    fin = fopen(_in, "r");
    fout = fopen(_out, "w");
    
    int count;
    
    fscanf(fin,"%d", &count);
    for(int i = 1; i<=count; i++)
    {
        int R, k, N;
        fscanf(fin, "%d %d %d \n", &R, &k, &N);
        int *gValues = new int[N];
        int *gPos = new int[N];
        long long unsigned *gSums = new long long unsigned[N];
        for(int j = 0; j < N; j++)
        {
            fscanf(fin, "%d", gValues + j);
            gPos[j] = -1;
        }
        
        long long unsigned sum = 0;
        int startPosition  = 0;
        bool muust_do = false;
        for(int j = R; j > 0; j--)
        {
            if(gPos[startPosition]==-1 || muust_do)
            {
                gPos[startPosition] = j;
                int pSum = gValues[startPosition];
                int next = (startPosition + 1)%N;
                while(gValues[next] + pSum <= k && next!=startPosition)
                {
                    pSum += gValues[next];
                    next  = (next + 1)%N;
                }
                gSums[startPosition] = sum;
                sum += pSum;
                startPosition = next;
            }
            else
            {
                int len = gPos[startPosition] - j;
                long long unsigned s = sum - gSums[startPosition];
                sum += s*(j/len);
                j = j % len + 1;
                muust_do = true;
            }
        }
        fprintf(fout,"Case #%d: %lld\n", i, sum);
        delete [] gValues;
    }
    
    fclose(fin);
    fclose(fout);
}