#include<iostream>
#include<cstdlib>
#include<math.h>

using namespace std;

int _count(int,int);

int main()
{
    FILE *fp;
    fp=fopen("C-small-attempt0.in","r");
    int times;
    int lower_bound;
    int upper_bound;
    int case_number=1;
    fscanf(fp,"%d\n",&times);
    FILE *wfp;
    wfp=fopen("C-small-attempt0.out","w");
    while(!feof(fp))
    {
     while(times>0)
     {
      int counter=0;
      fprintf(wfp,"Case #%d: ",case_number);
      fscanf(fp,"%d %d\n",&lower_bound, &upper_bound);
      counter=_count(lower_bound,upper_bound);
      fprintf(wfp,"%d\n",counter);
      times--;
      case_number++;
      }
     }
    fclose(wfp);
    fclose(fp);
    system("pause");
}


int _count(int lower_bound,int upper_bound)
{
    int counter=0;
    int digit=1;
    int cpy=lower_bound;
    int start;
    int last_r_start=lower_bound;
    start=lower_bound;   
    bool digi_lock=false;
    while(!digi_lock)
    {
        if(cpy/10 > 0)
        {
           cpy=cpy/10;
           digit++;
        }                        
        else
        digi_lock=true;
    }
    while(start!=upper_bound)
    {
     for(int idx=1;idx<digit;idx++)
     {
      int back=1;
      int front=1;
      for(int x=0;x<idx;x++)
      back=back*10;
      for(int y=0;y<digit-idx;y++)
      front=front*10;
      int r_start=front*(start-back*floor(start/back))+floor(start/back);     
      if(r_start<=upper_bound && r_start>start && r_start!=last_r_start)
      {
          last_r_start=r_start;
          counter++;    
      }  
     } 
     start++;  
    }        
    return counter;
}
