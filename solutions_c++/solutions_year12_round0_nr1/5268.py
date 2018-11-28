#include <stdio.h>
#include <string.h>

int main()
{
 char rever_conv[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
 FILE *fin, *fout;
 int i,j,n,m;
 char line[200];

 fin = fopen("input.txt", "r");
 fout = fopen("output.txt", "w");
 fscanf(fin, "%d", &n);
 fgets(line, 200, fin);
 for (i = 0;i < n;i++)
 {
   fgets(line, 200, fin); 
   m = strlen(line);

   fprintf(fout, "Case #%d: ", i+1);
   for (j = 0;j < m;j++)
   {
    char c = line[j];
    int index = c - 'a';
    if (index >=0 && index < 26)
    {
     c = rever_conv[index];
    }
    fprintf(fout, "%c", c);
   }
 } 
 fclose(fin);
 fclose(fout);
 return 0;
}
