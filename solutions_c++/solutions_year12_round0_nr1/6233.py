#include <stdio.h>
#include <stdlib.h>
#include <string.h>

main(void)
{
    FILE *fin, *fout, *fina;
    
    fin = fopen ("in.txt" , "r");
    fina = fopen ("A-small-attempt4.in" , "r");
    fout = fopen ("out.txt" , "w");
    
    
    char line[105],a1[101],a2[101],a3[101],b1[101],b2[101],b3[101];
    char kodas[256];
    fgets(line, sizeof line, fin);
    int t=atoi(line),i;
    
    fgets(a1, sizeof line, fin);
    fgets(a2, sizeof line, fin);
    fgets(a3, sizeof line, fin);
    fgets(b1, sizeof line, fin);
    fgets(b2, sizeof line, fin);
    fgets(b3, sizeof line, fin);
    for(i=0;i<=256;i++)
    {
        kodas[i]=i;
    }
    kodas['a']='y';
    kodas['o']='e';
    kodas['z']='q';
    kodas['q']='z';
    
    for(i=0;i<=strlen(a1);i++)
        kodas[a1[i]]= b1[i];
    for(i=0;i<=strlen(a2);i++)
        kodas[a2[i]]= b2[i];
    for(i=0;i<=strlen(a3);i++)
        kodas[a3[i]]= b3[i];

    fgets(line, sizeof line, fina);
    t=atoi(line);
    int j,y;
    for(i=1;i<=t;i++)
    {
        fprintf(fout,"Case #%d: ", i);
        fgets(line, sizeof line, fina);
        for(j=0;j<=strlen(line)-2;j++)
        fprintf(fout, "%c", kodas[line[j]]);
        fprintf(fout, "\n");
    }
    system("pause");
    fclose(fout);
}
