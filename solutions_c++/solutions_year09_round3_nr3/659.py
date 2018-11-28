#include<iostream.h>
#include<stdio.h>
#include<conio.h>
#include<string.h>

int main()
{
    FILE *in,*out;
    in=fopen("input.txt","r");
    out=fopen("out.txt","w");
    int T,i,j,caseNo=0,loc,loc1;
    char N[25],A[25],c,min,min1;
    fscanf(in,"%d",&T);
    while(caseNo<T)
    {
        fscanf(in,"%s",N);
        strcpy(A,N);


            for(j=strlen(A)-2;j>=0;j--)
            {                         
                  min='a';                               
                  for(i=j+1;i<strlen(A);i++)
                  if((A[i]>A[j])&&(A[i]<min))
                  {
                               min=A[i];     
                               loc=i;
                  }
                  
                  if(min!='a')
                  {
                  c=A[j];
                  A[j]=min;
                  A[loc]=c;                                             
                  goto out;
                  }
            }
            
            out:

                
            if(!strcmp(A,N))
            {
                            for(i=0;i<strlen(A);i++)
                            {
                                                    min=A[i];
                                                    loc=i;
                            for(j=i;j<strlen(A);j++)
                            {
                                                    if(A[j]<min)
                                                    {
                                                                min=A[j];
                                                                loc=j;
                                                    }
                            }
                            c=A[loc];
                            A[loc]=A[i];
                            A[i]=c;
                            }
                            
                            if(A[0]=='0')
                            {
                                         j=1;
                                         while(A[j]=='0')
                                         j++;
                                         A[0]=A[j];
                                         A[j]='0';
                            }
                            for(j=strlen(A);j>0;j--)
                            A[j+1]=A[j];
                            A[1]='0';
            }


        fprintf(out,"Case #%d: %s\n",caseNo+1,A);
                    
        caseNo++;   
    }


    fclose(in);
    fclose(out);
    return 0;
}
