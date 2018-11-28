#include <stdio.h>
#include <string.h>

int main()
{
    char n, x, a, b, numlen, srclen, tgtlen;
    int val, pwr;
    char num[20], src[94], tgt[94], ans[20];
    FILE *in, *out;
    
    in = fopen("A-large-practice.in", "r");
    out = fopen("out.txt", "w");

    if(in == 0 || out == 0)
        return -1;

    fscanf(in, "%d%c", &n, &x);
    for(x = 0; x < n; x++)
    {
        fscanf(in, "%s%s%s", num, src, tgt);
        numlen = strlen(num);
        srclen = strlen(src);
        tgtlen = strlen(tgt);
        
        fprintf(out, "Case #%d: ", x + 1);
        
        val = 0;
        pwr = 1;
        for(a = numlen - 1; a >= 0; a--)
        {
            for(b = 0; b < srclen; b++)
                if(num[a] == src[b])
                    val += pwr * b;
            pwr *= srclen;
        }
        
        for(a = 0; val >= 1; a++)
        {
            ans[a] = tgt[val % tgtlen];
            val /= tgtlen;
        }
        
        for(a--; a >= 0; a--)
            fprintf(out, "%c", ans[a]);
        fprintf(out, "\n");
    }

    fclose(in);
    fclose(out);
    
    return 0;
}
