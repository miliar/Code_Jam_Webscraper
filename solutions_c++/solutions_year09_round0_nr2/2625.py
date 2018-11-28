#include<stdio.h>
using namespace std;
int a[100][100];
char b[100][100];
int d[4];
char current;
int call;
void check(char s,char t,int u,int v)
{
     int i,j;
  //   printf("%c %c\n",s,t);
     
     for(i=0;i<u;i++)
     {
                     for(j=0;j<v;j++)
                     {
                                     if(b[i][j]==s)
                                     {
                                          //printf("Equals fr %d %d\n",i,j);         
                                     b[i][j]=t;
                                     }
                                     else if(b[i][j]>s)
                                     {
                                         // printf("true for %d,%d\n",i,j);
                                     b[i][j]=b[i][j]-1;
                                     }
                     }
     }
current--;
call=1;
//printf("current=%c\n",current);
return;
} 
int main()
{
    
    
    int cnt=1;
    int h,w; 
    int t,i=0;
    scanf("%d",&t);
    
    int p;
    int small,index,j,k;
    
    int stat=0;
   current='a';
    while(i<t)
    {
              current='a';
               cnt=0;
               
            scanf("%d %d",&h,&w);
    for(j=0;j<h;j++)
    {
    for(k=0;k<w;k++)
    {
    b[j][k]=' ';         
    }
       }
    b[0][0]='a';
            
            for(j=0;j<h;j++)
            {
            for(k=0;k<w;k++)
            {
            scanf("%d",&a[j][k]);
            }
            }
            for(j=0;j<h;j++)
            {
            for(k=0;k<w;k++)
            {
                            stat=0;
                            call=0;
                            if(b[j][k]==' ')
                            {
                                             current++;
                                             b[j][k]=current;
                                             stat=1;
                            }
                            
                            for(p=0;p<=3;p++)
                            d[p]=99999;
                            small=99999;
                            if(j-1>=0)
                            {
                                             d[0]=a[j-1][k];
                            }
                            else
                            {
                                
                                d[0]=99999;
                            }
                            if(j+1<h)
                            {
                                     d[3]=a[j+1][k];
                            }
                            else
                            {
                                d[3]=99999;
                            }
                             if(k-1>=0)
                            {
                                             d[1]=a[j][k-1];
                            }
                            
                            else
                            {
                                d[1]=99999;
                            }
                             if(k+1<w)
                            {
                                             d[2]=a[j][k+1];
                            }
                            else
                            {
                                d[2]=99999;     
                            }
                            
                            for(p=0;p<=3;p++)
                            {
                                             if(d[p]<small)
                                             {
                                             small=d[p];         
                                             index=p;     
                                             
                                             }
                                             
                            }
                            if(small<a[j][k])
                            {
                            if(index==0)
                            {
                                        if(b[j-1][k]==' ')
                                        {
                                        b[j-1][k]=b[j][k];
                                        }
                                        else if(b[j][k] > b[j-1][k])
                                        {
                                        check(b[j][k],b[j-1][k],h,w);
                                        b[j][k]=b[j-1][k];
                                        
                                        }
                                        else
                                        {
                                        check(b[j-1][k],b[j][k],h,w);
                                        b[j-1][k]=b[j][k];
                                        
                                        }
                            }
                            else if(index==1)
                            {
                                 if(b[j][k-1]==' ')
                                 {
                                        b[j][k-1]=b[j][k]; 
                                        }
                                        else if(b[j][k]>b[j][k-1])
                                        {
                                             check(b[j][k],b[j][k-1],h,w);
                                        b[j][k]=b[j][k-1];
                                        }
                                        else
                                        {
                                            check(b[j][k-1],b[j][k],h,w);
                                        b[j][k-1]=b[j][k];
                                        }
                            }
                            else if(index==3)
                            {
                                 if(b[j+1][k]==' ')
                                 {
                                 b[j+1][k]=b[j][k];
                                 }
                                 else if(b[j][k] > b[j+1][k])
                                 {
                                      check(b[j][k],b[j+1][k],h,w);
                                 b[j][k]=b[j+1][k];
                                 }
                                 else
                                 {
                                     check(b[j+1][k],b[j][k],h,w);
                                 b[j+1][k]=b[j][k];
                                 }
                            }
                            else if(index==2)
                            {
                                 if(b[j][k+1]==' ')
                                b[j][k+1]= b[j][k];
                                else if(b[j][k] >b[j][k+1])
                                {
                                     check(b[j][k],b[j][k+1],h,w);
                                b[j][k]=b[j][k+1];
                                }
                                else
                                {
                                    check(b[j][k+1],b[j][k],h,w);
                                b[j][k+1]=b[j][k];
                                }
                            }
                            }
                            if(stat==1 && b[j][k]!=current && call ==0)
                            current--;
                            
                                             
                            
            }
            }   
           
           printf("Case #%d:\n",i+1);
    
            for(j=0;j<h;j++)
            {
            for(k=0;k<w;k++)
            {
            
            printf("%c ",b[j][k]);
            
            
            }
            printf("\n");
            }
           i++;
    }
        return 0;
}



