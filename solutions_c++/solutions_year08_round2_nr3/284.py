#include <stdio.h>

int main()
{
    FILE *in, *out;
    in = fopen("inc.txt","r");
    out = fopen("c.txt","w");
    
    int t, k, count, index, i, j, z;
    fscanf(in,"%d\n",&t);
    for (i=0; i<t; i++)
    {
        fscanf(in,"%d\n",&k);
        int num[k], visit[k];
        
        for (j=0; j<k; j++)
            visit[j] = 1;
        index = -1;
        for( count = 1; count <=k ; count++)
        {
            for (j = count; j>0; j--)
            {
                while(1){
                    index++;
                    if (index >= k)
                        index = 0;
                    if (visit[index])
                        break;
                }
            }
            num[index] = count;
            visit[index] = 0;
            //printf("index = %d co = %d",index,count);
            //getchar();
        }
        
        fscanf(in,"%d",&z);
        fprintf(out,"Case #%d:",i+1);
        for (j=0 ; j<z; j++)
        {
            fscanf(in," %d",&index);
            fprintf(out," %d",num[index-1]);
        }
        fscanf(in,"\n");
        fprintf(out,"\n");
        printf(" %d",i+1);
    }
    
    fclose(in);
    fclose(out);
}
