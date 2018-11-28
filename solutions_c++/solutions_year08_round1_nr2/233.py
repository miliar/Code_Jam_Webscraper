#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>

using namespace std;


char hex(int value)
{
  switch(value)
  {
    case 10:
      return 'a';
    case 11:
      return 'b';
    case 12:
      return 'c';
    case 13:
      return 'd';
    case 14:
      return 'e';
    case 15:
      return 'f';
    default:
      return (value+48);
  }
}

int main()
{

  FILE *f = fopen("B-large.in","r");
  int n;

  if(f==NULL)
    printf("no file");
  fscanf(f,"%d",&n);
  for(int i=0;i<n;i++)
  {
   int types,cust=0;
   fscanf(f,"%d",&types);
   fscanf(f,"%d",&cust);
   //FILE *fff=fopen("done.txt","a");
   //fprintf(fff,"%d %d %d\n",(i+1),types,cust);
   //fclose(fff);
   vector< vector< vector <int> > > pref;
   for(int j=0;j<cust;j++)
   {
    vector< vector <int> > x;

    for(int k=0;k<types;k++)
    {
        vector<int> y;
        y.push_back(0);
        y.push_back(0);
        x.push_back(y);
    }
    pref.push_back(x);
   }
   int final[types];
   for(int j=0;j<types;j++)
    final[j]=0;

   for(int j=0;j<cust;j++)
   {
    int x;

    fscanf(f,"%d",&x);
    for(int k=0;k<x;k++)
    {
        int flav,malt;
        fscanf(f,"%d %d",&flav,&malt);
        pref[j][flav-1][malt]=1;
        if(malt==1&&x==1)
         final[flav-1]=1;
    }
   }

   int sat[cust];
   for(int j=0;j<cust;j++)
    sat[j]=0;
   int can=1;
   for(int j=0;j<cust;j++)
   {
        for(int k=0;k<types;k++)
        {
            if(pref[j][k][0]==1&&final[k]==0)
            {
                sat[j]=1;
                break;
            }
        }
        if(sat[j]==0)
        {
          for(int k=0;k<types;k++)
          {
            if(pref[j][k][1]==1)
            {
                if(final[k]==1)
                {
                    sat[j]=1;
                    break;
                }
                else
                {
                    final[k]=1;
                    for(int x=0;x<cust;x++)
                        sat[x]=0;
                    j=-1;
                    break;
                }
            }
          }
        }
        else
           continue;
        if(j!=-1&&sat[j]==0)
        {
           can=0;
           j=cust;
        }
   }
   FILE *fout=fopen("B-large.out","a");
   if(can==0)
    fprintf(fout,"Case #%d: IMPOSSIBLE\n",(i+1));
   else
   {
    fprintf(fout,"Case #%d:",(i+1));
    for(int j=0;j<types;j++)
       fprintf(fout," %d",final[j]);
    fprintf(fout,"\n");
   }

   fclose(fout);
  }
  fclose(f);

}
