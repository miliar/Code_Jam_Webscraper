#include <cstdio>

using namespace std;

char change[26] = {'y','h', 'e', 's', 'o', 'c', 'v', 'x', 'd'
            , 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't',
            'n','w','j','p','f','m','a', 'q'};
            
int main()
{
    int   t, i;
    FILE *fin, *fout;
    fin = fopen("A-small-attempt0.in", "r");
    fout = fopen("out.txt", "w");
    fscanf(fin ,"%d", &t);
    char c1;
    fscanf(fin ,"%c", &c1);
    if(t > 0)
         for(i = 1; i <= t; i++)
         {
               fprintf(fout ,"Case #%d: ", i);
               char cc;
               fscanf(fin ,"%c", &cc);
               while(cc != '\n')
               {
                      if(cc == ' ')
                            fprintf(fout ," ");
                      else 
                           fprintf(fout ,"%c", change[cc - 'a']);   
                      fscanf(fin, "%c", &cc);  
               }
              fprintf(fout, "\n");
         }
    fclose(fin);
    fclose(fout);
    return 0;
}
