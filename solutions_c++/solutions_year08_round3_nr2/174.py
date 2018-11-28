#include <stdio.h>
#include <string.h>

int main()
{
    FILE *in = fopen("input.txt", "r");
    FILE *out = fopen("output.txt", "w");
    
    int N, test;
    fscanf(in, "%ld", &N);
    
    for (test=1;test<=N;test++)
    {
        int st[20], i, len;
        for (i=0;i<20;i++) st[i]=0;
        char number[256];
        fscanf(in, "%s", number);
        len = strlen(number);


        __int64 x=0, k=10, res=0, y=number[0]-'0';
        int coef=1;
        
        
        do
        {
            y=number[0]-'0';
            x=0;
            coef=1;
            for (i=0;i<len-1;i++)
            {
                if (st[i]==0)
                {
                    x+=coef*y;
                    coef=1;
                    k=1;
                    y=0;
                }
                else if (st[i]==1)
                {
                    x+=coef*y;
                    coef=-1;
                    k=1;
                    y=0;
                }
                else y*=10;
                /*x+=coef*k*((__int64)(number[i+1]-'0'));
                k*=10;*/
                y+= (__int64)(number[i+1]-'0');
//                k*=10;
                
            }
            x+=coef*y;
            if (!(x%2) || !(x%3) || !(x%5) || !(x%7) ) {res++;/*printf("%I64d\n", x);*/}
            
            //printf("%I64d\n", x);
            
            i=0;
            st[i]++;
            while(st[i]==3)
            {
                st[i]=0;
                st[i+1]++;
                i++;
            }
        }
        while (st[len-1]==0);
        fprintf(out, "Case #%ld: %I64d\n", test, res);
    }
    
    fclose(in);
    fclose(out);   
    return 0;
}
