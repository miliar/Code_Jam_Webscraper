#include <stdio.h>
#include <string.h>

int resp, tam;
char test[5000];
char* ref = "welcome to code jam";

void acharResp(int, int);

int main()
{
    int n;
    FILE *in, *out;
    in = fopen("welcome.in","r");
    out = fopen("welcome.out","w");

    fscanf(in, "%d",&n);
    fgetc(in);

    for(int k = 1; k <= n; k++)
    {
         fgets(test,1000,in);
         resp = 0;
         tam = strlen(test);
         test[tam - 1] = '\0';
         tam--;

         if(tam >= strlen(ref))
            acharResp(0,0);

         /*output*/
         fprintf(out,"Case #%d: ",k);
         if(resp < 10)  fprintf(out,"000");
         else if(resp < 100)    fprintf(out,"00");
         else if(resp < 1000)   fprintf(out,"0");
         fprintf(out,"%d",resp);
         if(k<n)    fprintf(out,"\n");
    }
    return 0;
}

void acharResp(int letra, int pos)
/*letra diz em qual letra de ref estamos, e pos qual a posção em test*/
{
    while(pos < tam)
    {
        while(ref[letra] != test[pos] && pos < tam)
            pos++;
        if(pos < tam)
        {
            if(letra == 18)
                resp = (resp + 1)%10000;
            else
                acharResp(letra + 1, pos + 1);
        }
        pos++;
    }
    return;
}
