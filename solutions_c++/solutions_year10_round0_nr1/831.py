#include<cstdio>

#define _out "out.txt"
#define _in  "A-large.in"

int main(int argc, void* argv[])
{
    FILE *fin, *fout;

    fin = fopen(_in, "r");
    fout = fopen(_out, "w");
    
    int count;
    
    fscanf(fin,"%d", &count);

    int N, K;
    for(int i = 1; i<=count; i++)
    {
        fscanf(fin, "%d %d\n", &N, &K);
        int cycleLen = 1<<N;
        if(K % cycleLen == cycleLen - 1)
            fprintf(fout,"Case #%d: ON\n",i);
        else
            fprintf(fout,"Case #%d: OFF\n",i);
    }
    
    fclose(fin);
    fclose(fout);
}