#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{

  FILE *f = fopen("D-small.in","r");
  int n;

  if(f==NULL)
    printf("no file");
  fscanf(f,"%d",&n);
  
  for(int i=0;i<n;i++)
  {

   long l,ans=50000;
   char s[50000];
   int k;
   fscanf(f,"%d",&k );
   fscanf(f,"%s",s );
   int perm[k];
   for(int j=0;j<k;j++)
    perm[j]=j;
   l=strlen(s);
   do
   {
     char s2[50000];
     for(int p=0;p<l/k;p++)
     {
        for(int q=0;q<k;q++)
            s2[p*k+q]=s[p*k+perm[q]];
     }
     int x=0;
     char curr='\0';
     for(int p=0;p<l;p++)
        if(curr!=s2[p])
        {
            x++;
            curr=s2[p];
        }
     if(x<ans)
        ans=x;
   }
   while(next_permutation(perm,perm+k));

   FILE *fout=fopen("D-small.out","a");
   fprintf(fout,"Case #%d: %d\n",(i+1),ans);
   fclose(fout);
  }

  fclose(f);
  //cin.get();
}
