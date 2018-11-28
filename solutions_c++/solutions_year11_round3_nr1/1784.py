#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>


using namespace std;

int main(void)
    {
        FILE *ifile;
        FILE *ofile;
        ifile = fopen("A-large.in","r+");
        ofile = fopen ("Output.txt","w+");

        long int n,i=0;
        fscanf(ifile,"%d",&n);

    while(i<n)
    {
        int a=0,b=0,c=0,d=0,e=0,j=0,k=0,ch=1,chck=0;
        char data1[100][100]={'\0'};
          char ch1;
         fscanf(ifile,"%d %d",&a,&b);

        for (c=0;c<a;c++)
        {fscanf(ifile,"%s",&data1[c]);
                }

        for (c=0;c<a;c++)
        {for (d=0;d<b;d++)
        {
            if (data1[c][d]=='#' && data1[c][d+1]=='#')
            {if (data1[c+1][d]=='#'&& data1[c+1][d+1]=='#')
            {data1[c][d]='/';
            data1[c+1][d]='\\';
            data1[c][d+1]='\\';
            data1[c+1][d+1]='/';
            }
            }
        }
        }

        for (c=0;c<a;c++)
        {for (d=0;d<b;d++)
        {
            if (data1[c][d]=='#')
            {e++;
                    }
        }
        }
        if ( e != 0)
        {fprintf(ofile,"Case #%d:\nImpossible\n",i+1);}
        else
        {fprintf(ofile,"Case #%d:\n",i+1);

        for (c=0;c<a;c++)
        {for (d=0;d<b;d++)
        {fprintf(ofile,"%c",data1[c][d]);}
        fprintf(ofile,"\n");
        }
                }
        i++;
    }


fclose(ifile);
fclose(ofile);
return 0;
}


