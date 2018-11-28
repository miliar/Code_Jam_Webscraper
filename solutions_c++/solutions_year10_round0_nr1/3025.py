#include<stdio.h>
//#include<conio.h>
long int power(int i)
{if(i==0)
return 1;
else
return 2*(power(i-1));
}
int main()
{
    long int k,i,j;
    int case_id,t;
    FILE *fp,*qp;
    fp=fopen("a-large.in","r");
    qp=fopen("a-largesol.in","w");
    fscanf(fp,"%d",&t);
    for(case_id=1;case_id<=t;case_id++)
    {
                                       fprintf(qp,"Case #%d: ",case_id);
                                       fscanf(fp,"%d%d",&i,&k);
                                       if(k)
                                       {
                                            if((k+1)%power(i))
                                            fprintf(qp,"OFF\n");
                                            else 
                                            fprintf(qp,"ON\n");
                                            }
                                            else
                                            fprintf(qp,"OFF\n");
                                            }
                                            return 0;
                                            }
                                            
                                       
