#include<stdio.h>
FILE *in,*out;
int t,t_store,r,c,i,j,n,flag,pd,pg,temp;
char matrix[60][60];
main()
{in=fopen("in.txt","r");
out=fopen("out.txt","w");
fscanf(in,"%d",&t);
t_store=t;
  while(t--)
{
fscanf(in,"%d%d",&r,&c);
for(i=0;i<r;i++)           
            {fscanf(in,"%s",matrix[i]);
            }
            flag=1;
for(i=0;i<r;i++)
for(j=0;j<c;j++)
{if(flag==1){if(matrix[i][j]=='#')
{{
if((i+2<=r)&&(j+2<=c)){if((matrix[i][j+1]=='#')&&(matrix[i+1][j]=='#')&&(matrix[i+1][j+1]=='#')){matrix[i][j]='/';
matrix[i][j+1]='\\';
matrix[i+1][j]='\\';
matrix[i+1][j+1]='/';
                        }else flag=0;}
                        else flag=0;}
                       }
  }  
             }
fprintf(out,"Case #%d:\n",t_store-t);
if(flag==1)
{for(i=0;i<r;i++)
fprintf(out,"%s\n",matrix[i]);
}
else {fprintf(out,"Impossible\n");
     }
            
            
            }
      }
