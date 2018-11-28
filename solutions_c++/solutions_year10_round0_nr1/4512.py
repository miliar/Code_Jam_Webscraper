// link to libraries  : http://sourceforge.net/projects/mingw/


#include<stdio.h>
#include<conio.h>

int main()
{

     int t, n;
    unsigned int k,  num ;
    FILE *fin, *fout;
    fin = fopen("c:\\A-small-attempt1.in","r");
    fout = fopen("c:\\out1","w");
    fscanf(fin,"%d",&t);
    for( int p = 1; p <= t; p++)
 {
    fscanf(fin,"%d %d",&n,&k);
    num = 1;
    for( int i = 1; i <= n; i++)
    num = 2 * num;
   if(( k - ( num - 1) ) % num == 0)
    fprintf(fout,"Case #%d: %s\n",p,"ON");
    else
    fprintf(fout,"Case #%d: %s\n",p,"OFF");
}
fclose(fin);
fclose(fout);
printf("\n done ");
   getch();
   return 0;
}

