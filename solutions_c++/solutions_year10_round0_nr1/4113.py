#include<stdio.h>
#include<math.h>
#define ON 1
#define OFF 0
int execute_test_case(int n,long int k);
int main()
{
 FILE *fpin,*fpout;
 int no_of_test_cases;
 fpin=fopen("input.txt","r");
 fpout=fopen("output.txt","w");
 fscanf(fpin,"%d\n",&no_of_test_cases);
 for(int i=0;i<no_of_test_cases;i++)
 {
  int n;
  long k;
  fscanf(fpin,"%ld %ld",&n,&k);
  if(execute_test_case(n,k)==ON)
   fprintf(fpout,"Case #%d: ON",i+1);
  else
   fprintf(fpout,"Case #%d: OFF",i+1);
  fprintf(fpout,"\n");
 }
}
int execute_test_case(int n,long int k)
{
 long int power;
 if(n>=27)return OFF;
 power=(long int)pow(2,n);
 k=k%power; 

 if(k==power-1)
  return ON;
 else
  return OFF;
}
