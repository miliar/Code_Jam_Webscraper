#include<stdio.h>
#include<conio.h>
int main()        
{
    int T,r,k,n,r1;
    //int g[4];
    FILE *fp,*ft;
    fp=fopen("C-small-attempt1.in","rb");
    ft=fopen("output1.out","wb");
    fscanf(fp,"%d",&T);
    for(int x=1;x<T+1;x++)
    {
            fscanf(fp,"%d%d%d",&r,&k,&n);
            //printf("r=%d,k=%d,n=%d\n",r,k,n);
            int *g = new int[n];     
            for(int i=0;i<n;i++)
              fscanf(fp,"%d",&g[i]);
            
           /* for(int i=0;i<n;i++)
              printf("%d ",g[i]);
            printf("\n\n");  */              
            int s=0,e=0,j=0,c=0;
            for(int i=0;i<r;i++)
            {
                     s=0;c=0;
                     while(1)
                    {
                               s=s+g[j];
                    //           printf("\t s=%d",s);
                               j++;
                               c++;
                               int t=j;
                               j=j%n;
                               if(c==n || s+g[j]>k)
                               {
                                         j=t%n;
                                         break;
                               }  
                    }
                   // printf("\ns=%d,e=%d,j=%d\n",s,e,j);
                    e=e+s;
            }
            printf("\nCase #%d: %d",x,e);
            fprintf(ft,"Case #%d: %d\n",x,e);
            
    }
    /*for(int i=0;i<4;i++)
    {
            fscanf(fp,"%d%",&g[i]);

    }
    fscanf(fp,"%d",&r1);
     if(fp==NULL)
     {
                 puts("Cannot open file");
//                 break;
     }
     printf("\n%d,%d,%d,%d,%d\n",T,r,k,n,r1);
     for(int i=0;i<4;i++)
    {
            printf("%d%\t",g[i]);
    } */
    
     fclose(fp);
    fclose(ft);
   	getchar();
}
