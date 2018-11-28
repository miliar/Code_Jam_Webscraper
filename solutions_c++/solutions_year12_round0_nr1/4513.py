#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
     char str[1000];
     char Entrada[] =
                "ejp mysljylc kd kxveddknmc re jsicpdrysi"
                "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
                "de kr kd eoya kw aej tysr re ujdr lkgc jvqz";
     char Saida[] =
                "our language is impossible to understand"
                "there are twenty six factorial possibilities"
                "so it is okay if you want to just give upzq";
     char map[255];

     int i,n,j,qtd;
     n = strlen(Entrada);
     for(i=0;i<n;i++)
        map[(int)Entrada[i]] = Saida[i];

     scanf("%i\n",&n);
     for(i=0;i<n;i++)
     {
         gets(str);
         qtd=strlen(str);
         for(j=0; j<qtd;j++)
            str[j] = map[str[j]];
         printf("Case #%i: %s\n",i+1,str);
     }
  return 0;
}