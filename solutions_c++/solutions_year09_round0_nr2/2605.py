#include<stdio.h>
    int var,alt,T,H,W,in[100][100],i,j,temp,X,Y,m,n;
    char out[100][100],count='a',assign='a';

void process(int i, int j)
{
 
                X=-1;
                Y=-1;
                temp=12000;
                out[i][j]=assign;
                if((in[i+1][j]<in[i][j])&&(i<(H-1))&&(in[i+1][j]<=temp))//south
                {
                     X=i+1;
                     Y=j;
                     temp=in[X][Y];
                }
                if((in[i][j+1]<in[i][j])&&(j<(W-1))&&(in[i][j+1]<=temp))//east
                {
                     X=i;
                     Y=j+1;
                     temp=in[X][Y];
                }
                if((in[i][j-1]<in[i][j])&&(j>0)&&(in[i][j-1]<=temp))//west
                {
                     X=i;
                     Y=j-1;
                     temp=in[X][Y];
                }
                if((in[i-1][j]<in[i][j])&&(i>0)&&(in[i-1][j]<=temp))//north
                {
                     X=i-1;
                     Y=j;
                     temp=in[X][Y];
                }
                if(X!=-1)//reaching the sink..
                {
                         if(out[X][Y]!=0)
                         {
                             for(m=0;m<H;m++)
                             for(n=0;n<W;n++)
                             {
                                if(out[m][n]==assign)
                                out[m][n]=out[X][Y];                                
                             }
                             assign=out[X][Y];
                             count--;
                             return;
                         }
                         else out[X][Y]=assign;
                         process(X,Y);
                }
}




    
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);

    for(var=0;var<T;var++) 
    {
       count='a';
       
       scanf("%d%d",&H,&W);
       for(i=0;i<H;i++)
       for(j=0;j<W;j++)
       {
           scanf("%d",&in[i][j]);
           out[i][j]=0;
       }                                      
       for(i=0;i<H;i++)
       for(j=0;j<W;j++)
       { 
           assign=count;
           if(out[i][j]==0)
           {
              process(i,j);  
              count++;                                                     
           }
        }  
  printf("Case #%d:\n",var+1);
       for(i=0;i<H;i++)
       {
         for(j=0;j<W;j++)
         { 
           if(j<(W-1))
           printf("%c ",out[i][j]);       
           else
           printf("%c",out[i][j]);
         }
         printf("\n");
       }    
          
    }     
return 0;
}
