#include<fstream>
#include<string.h>
using namespace std;
ifstream fin("input");
ofstream fout("output");

char s[111][222],t[222];

int i,j,T;
char s1[211]="ejp mysljylc kd kxveddknmc re jsicpdrysi";

char s2[211] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char s3[211] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
char c1[211] = "our language is impossible to understand";
char c2[211] = "there are twenty six factorial possibilities";
char c3[211] = "so it is okay if you want to just give up";
void read()
{
    for(i = 0 ;i <strlen(s1); i++)
    {
        t[s1[i]] = c1[i];
            }
      for(i = 0 ;i <strlen(s2); i++)
    {
        t[s2[i]] = c2[i];
            }
      for(i = 0 ;i <strlen(s3); i++)
    {
        t[s3[i]] = c3[i];
            }
            t[122] = 'q';
            t[113] ='z' ;
    fin >>T;

    for(i = 1; i <= T; i ++)
    {
         fin.get();
         fin.get(s[i],211,'\n');
         //fout<<s[i]<<'\n';
         //fout<<"X" ;
         fout<<"Case #"<< i<<":" <<" ";
         for(j = 0 ;j< strlen(s[i]); j++)
         {
             if(s[i][j]!=' ')
                fout<<t[s[i][j]];
            else
                fout<<" ";

         }
              fout<<'\n' ;
    }

}
int main()
{
    read();
    fin.close();
    return 0;

}
