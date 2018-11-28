#include <stdio.h>
#include <string.h>

int main()
{
    char dic[5000][16], test[5000];
    int l, n, d, p, npal;

    FILE *in, *out;
    in = fopen("alien.in","r");
    out = fopen("alien.out","w");

    /*input*/
    fscanf(in,"%d %d %d",&l, &d, &n);
    for(int i = 0; i < d; i++)
        fscanf(in,"%s",dic[i]);

    /*análise das palavras*/
    for(int i = 1; i <= n; i++)
    {
        fscanf(in,"%s",test);
        npal = 0;
        for(int j = 0, flag; j < d; j++)  /*ve se alguma das palavrasa do dicionário se encaixa*/
        {
            flag = 1;
            for(int k = 0, p = 0; k < l && flag; k++, p++)
            {
                if(test[p] == '(')
                {
                    flag = 0;
                    while(!flag && test[p] != ')')
                    {
                        p++;
                        if(dic[j][k] == test[p])
                            flag = 1;
                    }
                    while(test[p] != ')')
                        p++;
                }
                else if(test[p] != dic[j][k])
                    flag = 0;
            }
            if(flag)
                npal++;
        }
        fprintf(out,"Case #%d: %d\n",i,npal);
    }
    fclose(in);
    fclose(out);
    return 0;
}
