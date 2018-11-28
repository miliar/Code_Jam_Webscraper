#include<cstdio>
#include<iostream.h>
#include<conio.h>
using namespace std;
int main()
{
    int t;
    int n[110];
    long int array[110][1100];
    long int c;
    long long int sum;
    long int min;
    char string[10000];
    
    FILE *fd,*fd3;
    int count=0;
    int i,j;
    
    void *fd1;
    char *str,*token;
    
    fd=fopen("input.in","r");
    fd3=fopen("output.out","w");
    
    fd1=fgets(string,10000,fd);
        
    while(fd1!=NULL)
    {
        if(count==0)t=atoi(string);
        else if((count%2)==1)n[count/2]=atoi(string);
        else if((count%2)==0)
        {
                  for(str=string,i=0;;str=NULL,i++)
                  {
                                 
                                 token=strtok(str," \n");
                                 if(token==NULL)break;
                                 array[count/2-1][i]=atoi(token);
                                 
                  }
                  
                                 
                     
        }
         
        fd1=fgets(string,10000,fd);
        count++;
    }    
    fclose(fd);

for(i=0;i<t;i++)
{
                c=array[i][0]^array[i][1];
                
                for(j=2;j<n[i];j++)
                c=c^array[i][j];
                
                if(c==0)
                {
                sum=0;
                min=array[i][0];
                for(j=0;j<n[i];j++)
                {
                                   sum=sum+array[i][j];
                                   if(array[i][j]<min)min=array[i][j];
                }
                sum=sum-min;
                sprintf(string,"%d",sum);                        
                }
                else
                {
                    sprintf(string,"NO");
                }
fprintf(fd3,"Case #%d: %s\n",i+1,string) ;                  
}
fclose(fd3);    
//getch();    
}
