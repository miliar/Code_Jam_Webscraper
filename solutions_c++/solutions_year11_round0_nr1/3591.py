#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>


using namespace std;

int main(void)
{long int i=0,j=0,a,c,n;
    FILE *ifile;
    FILE *ofile;
    ifile = fopen("A-large.in","r+");
    ofile = fopen ("Output1.out","w+");
    fscanf(ifile,"%d",&n);
    while (i<n)
         {
         char rbk;
          char rb[100]={'\0'};
         int tpo[100]={'\0'},tpb[100]={'\0'},k=0,l=0,m=0,k1=0,l1=0,m1=0,po=1,pb=1,moves=0,check=0,fg=0,b=0;
            fscanf(ifile,"%d ",&a);
      for (j=0;j<a;j++)
      {fscanf(ifile,"%c ",&rbk);
      rb[k]=rbk;
                fscanf(ifile,"%d ",&b);
                                    if (rb[k]=='O')
             {tpo[l]= b;
             l++; }
         else if (rb[k]=='B')
             {tpb[m]= b;
             m++; }
                  k++;
      }

  while (k1<a)
   {
       if (rb[k1]=='O')
   {
       if (po<tpo[l1])
       {po += 1;
       moves++;
       if (pb < tpb[m1])
       {pb +=1;}
        if (pb > tpb[m1])
       {pb -=1;}
       }

 if (po>tpo[l1])
       {po -= 1;
       moves++;
       if (pb < tpb[m1])
       {pb +=1;}
        if (pb > tpb[m1])
       {pb -=1;}
       }

        if (po == tpo[l1])
      {  if (pb < tpb[m1])
       {pb +=1;}
        if (pb > tpb[m1])
       {pb -=1;}
          l1++;
          k1++;
        moves++;
         }
        }

   else if (rb[k1]=='B')
   {       if (pb<tpb[m1])
       {pb += 1;
       moves++;
          if (po < tpo[l1])
       {            po +=1;}
       if (po > tpo[l1])
       {            po -=1;}
       }
 if (pb>tpb[m1])
       {pb -= 1;
       moves++;
          if (po < tpo[l1])
       {            po +=1;}
       if (po > tpo[l1])
       {            po -=1;}
       }

    if (pb == tpb[m1])
   {   if (po < tpo[l1])
       {po +=1;}
        if (po > tpo[l1])
       {po -=1;}
       m1++;
    moves++;
k1++;
   }
     }
     }

    fprintf(ofile,"Case #%d: %d\n",i+1,moves);
    i++;
}

fclose(ifile);
fclose(ofile);
return 0;
}
