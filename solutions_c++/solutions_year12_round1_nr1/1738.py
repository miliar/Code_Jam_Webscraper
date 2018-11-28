#include<cstdlib>
#include<iostream>

using namespace std;

int main()
{
  FILE *fp;
  FILE *wfp;
  fp=fopen("A-small-attempt0.in","r");
  wfp=fopen("A-small-attempt0.out","w");
  int case_number;
  int typed;
  int length;
  double result[4];
  fscanf(fp,"%d \n",&case_number);
  while(!feof(fp))  
  {
    for(int time=0;time<case_number;time++)  
      {  
         float all_right=1;
         int p_case=1;
         fscanf(fp,"%d %d \n",&typed,&length);
         float *prob =new float[typed];     
         for(int idx=0;idx<typed;idx++)          
           fscanf(fp,"%f",&prob[idx]);         
         fscanf(fp,"\n");
         for(int idx=0;idx<typed;idx++)
         {
           all_right=all_right*prob[idx];
           p_case=p_case*2;
         }
         float opt_2=(all_right+all_right*(1-prob[typed-1])/prob[typed-1]);
         if(typed>=3)
         {
           float opt_3=(all_right+all_right*(1-prob[typed-1])/prob[typed-1]
                   +all_right*(1-prob[typed-2])*(1-prob[typed-1])/prob[typed-1]/prob[typed-2]
                   +all_right*(1-prob[typed-3])*(1-prob[typed-2])*(1-prob[typed-1])/prob[typed-1]/prob[typed-2]/prob[typed-3]);
           result[2]=(length-typed+1+2+2)*opt_3+(2+2+length-typed+1+1+length)*(1-opt_3);
         } 
         else
         result[2]=2+length+1;
         
         result[0]=(length-typed+1)*all_right+(length-typed+1+length+1)*(1-all_right);
         result[1]=(length-typed+1+2)*opt_2+(1+length-typed+1+1+length+1)*(1-opt_2);    
         result[3]=length+2;
         float min=result[0];
         for(int idx=0;idx<4;idx++)
         {
           if(result[idx]<min)       
             min=result[idx];
         } 
         fprintf(wfp,"Case #%d: ",time+1);
         fprintf(wfp,"%f \n",min);
         /*
         cout<<"length="<<length<<endl;
         cout<<"typed="<<typed<<endl;
         cout<<"all_right="<<all_right<<endl;
         cout<<"p_case="<<p_case<<endl;         
         cout<<"result[0]="<<result[0]<<endl;
         cout<<"result[1]="<<result[1]<<endl;
         cout<<"result[2]="<<result[2]<<endl;
         cout<<"result[3]="<<result[3]<<endl;*/
         delete [] prob;
    
      }

  } 
  fclose(fp);
  fclose(wfp); 
  system("pause");   
}
