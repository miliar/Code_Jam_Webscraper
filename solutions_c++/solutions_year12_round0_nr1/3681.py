#include <stdio.h>


char tran[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r',
               'z','t','n','w','j','p','f','m','a','q'};

int main()
{
    FILE *in, *out;
    int T, i, j;
    char buf[128], c;
    
    in = fopen("E:\\input.txt","r");
    out = fopen("E:\\output.txt","w");
    
    fscanf(in,"%d",&T);
    fgetc(in);
    
    for(i=1; i<=T; i++)
    {
        //memset(buf, 0, 128);
        for(j=0; j<128; j++)
        {
            buf[j] = 0;
        }
        
        //fscanf(in, "%[^ a-c]s", buf);
        j = 0;
        while(1)
        {
            c = fgetc(in);
            
            if(c=='\n' || c==EOF)
                break;
            buf[j++] = c;
        }
        
        j = 0;
        
        while(buf[j])
        {
            if(buf[j] >= 'a' && buf[j] <= 'z')
            {
                /* Translation logic here*/
                buf[j] = tran[buf[j]-'a'];
            }
            
            j++;
        }
        
        fprintf(out, "Case #%d: %s", i, buf);
        
        if(i<T)
            fprintf(out, "\n");
    }
}
