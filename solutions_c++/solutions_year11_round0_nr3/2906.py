#include<cstdio>

#define _in "C-large.in"
#define _out "out.txt"

int main(int argc, void** argv)
{
    FILE *fin, *fout;

    fin = fopen(_in, "r");
    fout = fopen(_out, "w");
    
    int nCases;
    fscanf(fin,"%d", &nCases);
    for(int i = 1; i<=nCases; i++)
    {
        int nCandys, candy;
        fscanf(fin,"%d", &nCandys);
        
        int sum = 0, patrickSum = 0, patrickHeap = -1;
        for(int j=0; j<nCandys; j++)
        {
            fscanf(fin,"%d", &candy);
            //find total value of candy heap
            sum +=candy;
            //patrick's sum is just bitwise "xor"
            patrickSum ^= candy;
            //smallest member of the sum is equal to the whole sum in terms of bitwise "xor"
            patrickHeap = patrickHeap < 0 ? candy : 
                                candy < patrickHeap ? candy : patrickHeap;
        }
        
        if(patrickSum!=0)
            //if the heap can be split in 2 equal parts, their sum should be 0
            fprintf(fout,"Case #%d: NO\n", i);
        else
            //Sean's heap is all candys short of the one with the smallest value
            fprintf(fout,"Case #%d: %d\n", i, sum - patrickHeap);
    }
    fclose(fin);
    fclose(fout);
}