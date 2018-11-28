#include<cstdlib>
#include<iostream>
#include<math.h>
using namespace std;

int main()
{
   FILE *fp;
   int times;
   fp=fopen("B-large.in","r");
   FILE *wfp;
   wfp=fopen("B-large.out","w");
   fscanf(fp,"%d\n",&times);
   int case_number=1;
   while(!feof(fp))
   {
    while(times>0)
    { 
      int n_googlers;
      int surprising;
      int points;
      int output=0;
      fscanf(fp,"%d %d %d\n",&n_googlers,&surprising,&points);
      fprintf(wfp,"Case #%d: ",case_number);
      //cout<<"n_googlers="<<n_googlers<<endl;
      int *pScore= new int[n_googlers];
      for(int rd_idx=0;rd_idx<n_googlers;rd_idx++)
        fscanf(fp,"%d ",&pScore[rd_idx]);
      
      for(int idx=0;idx<n_googlers;idx++)
      {
       
       int avg=(floor(pScore[idx]/3));
       //cout<<"pScore["<<idx<<"]="<<pScore[idx]<<endl;
       int rem=pScore[idx]-3*avg;
       if(avg>=points)
        output++;
       else if(rem>=1 && avg+1>=points) 
        output++;
       else if(rem==2 && avg+2>=points && surprising!=0)     
       {
         surprising--;
         output++;
        }
       else if(rem==0 && avg+1>=points && surprising!=0 && pScore[idx]!=0)
       {
         surprising--;   
         output++;   
       }
      }
      fprintf(wfp,"%d",output);
      delete [] pScore;
      fprintf(wfp,"\n");
      case_number++;
      times--;
    }
   }
   fclose(fp);
   fclose(wfp);
   system("pause");
   return 0;
}
