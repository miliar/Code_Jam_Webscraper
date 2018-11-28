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
    ifile = fopen("C-large.in","r+");
    ofile = fopen ("Output3.out","w+");
    long int n,i=0;
    fscanf(ifile,"%d",&n);

  while(i<n)
  {
        long int intm=0,tot=0,num=0,j=0,k=0,m=0,l=0,sum=0,p=0,pval=0,sval=0,vval=0,qval=0;
        long int val[1000]={'\0'};
        fscanf(ifile,"%d",&num);

        while(j<num)
        {   fscanf(ifile,"%d ",&val[j]);
             j++;}
        for (j=0;j<num;j++)
       intm += val[j];

            vector<int> myvector (val, val+num-1);
            vector<int>::iterator it;
            sort(myvector.begin(),myvector.begin()+num-1);
            for (it=myvector.begin(); it!=myvector.end(); ++it)
            {val[p]=*it;p++;}

              while(m<num-1)
        {l=0;qval=num-m;
            while(l<qval)
            {sval=0;pval=0;k=0;
                while(k<m+1)
                {  p=l+k; sval = sval^val[p];//XOR bit-mask
                    pval+=val[p];k++;}
                vval=intm-pval-sval;
                if(!vval)
                if (pval>tot)
                      tot= pval;
                      l++;}m++;}

        if (tot==0)
            fprintf(ofile,"Case #%d: NO\n",i+1);
        else
            fprintf(ofile,"Case #%d: %d\n",i+1,tot);
        i++;
  }
  return 0;
}
