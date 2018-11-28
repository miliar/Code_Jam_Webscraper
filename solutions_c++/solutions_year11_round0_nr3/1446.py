#include <stdio.h>


int solve(FILE *f);

int main()
{
    FILE *f=fopen("d:/Google_codejam/task3/data/input.txt","r");
    FILE *fOut=fopen("d:/Google_codejam/task3/data/output.txt","w");
    if(f==NULL)
        return 1;
    int total=4;
    fscanf(f,"%d",&total);
    for(int h=0; h<total; h++)
    {
        int result=solve(f);
        if(result==-1)
            fprintf(fOut,"Case #%d: NO\n",h+1);
        else
            fprintf(fOut,"Case #%d: %d\n",h+1, result);
    }
    fclose(f);
    fclose(fOut);
}


int solve(FILE *f)
{
    int count, x, smallest, sum;
    int numbers[1024];
    int binNumbers[1024][32];

    fscanf(f,"%d\n",&count);
    for(int h=0; h<count; h++)
    {
        fscanf(f,"%d ",&numbers[h]);

        binNumbers[h][0]=numbers[h]&1;
        binNumbers[h][1]=numbers[h]&2;
        binNumbers[h][2]=numbers[h]&4;
        binNumbers[h][3]=numbers[h]&8;
        binNumbers[h][4]=numbers[h]&16;
        binNumbers[h][5]=numbers[h]&32;
        binNumbers[h][6]=numbers[h]&64;
        binNumbers[h][7]=numbers[h]&128;
        binNumbers[h][8]=numbers[h]&256;
        binNumbers[h][9]=numbers[h]&512;
        binNumbers[h][10]=numbers[h]&1024;
        binNumbers[h][11]=numbers[h]&2048;
        binNumbers[h][12]=numbers[h]&4096;
        binNumbers[h][13]=numbers[h]&8192;
        binNumbers[h][14]=numbers[h]&16384;
        binNumbers[h][15]=numbers[h]&32768;
        binNumbers[h][16]=numbers[h]&65536;
        binNumbers[h][17]=numbers[h]&131072;
        binNumbers[h][18]=numbers[h]&262144;
        binNumbers[h][19]=numbers[h]&524288;
        binNumbers[h][20]=numbers[h]&1048576;
    }


    //Is it possbile
    for(x=0; x<21; x++)
    {
        sum=0;
        for(int h=0; h<count; h++)
            if(binNumbers[h][x])
                sum++;

        if(sum%2)
        {
            return -1;
        }
    }


    //Sum -1
    sum=0;
    smallest=numbers[0];
    for(int h=0; h<count; h++)
    {
        sum+=numbers[h];
        if(smallest>numbers[h])
            smallest=numbers[h];
    }


    return (sum-smallest);
}
