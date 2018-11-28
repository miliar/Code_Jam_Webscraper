#include<stdlib.h>

#include<stdio.h>
FILE *in,*out;
int t,m,n,i,j,t_store;
char matrix[100][100];
float win,total,wp[100],owp[100],oowp[100],total_m[100];
main()
{in=fopen("in.txt","r");
out=fopen("out.txt","w");

fscanf(in,"%d",&t);
t_store=t;while(t--)
{fscanf(in,"%d",&m);
for(i=0;i<m;i++)
{fscanf(in,"%s",matrix[i]);
  
                }
for(i=0;i<m;i++)
{win=0;
total=0;
for(j=0;j<m;j++)
{
              if(matrix[i][j]=='0')
              {total=total+1;
                                   }
else if(matrix[i][j]=='1')
{win=win+1;
total=total+1;
     }

                 }
wp[i]=win/total;
total_m[i]=total;
}
for(i=0;i<m;i++)
{win=0;
total=0;
for(j=0;j<m;j++)
if(matrix[i][j]=='0'||matrix[i][j]=='1')
{if(matrix[i][j]=='0')
win+=(wp[j]*total_m[j]-1)/(total_m[j]-1);
else 
win+=(wp[j]*total_m[j])/(total_m[j]-1);
                                         }
owp[i]=win/total_m[i];     
}

for(i=0;i<m;i++)
{win=0;
total=0;
for(j=0;j<m;j++)
if(matrix[i][j]=='0'||matrix[i][j]=='1')
{win+=owp[j];
                                            }
oowp[i]=win/total_m[i];
                }
fprintf(out,"Case #%d:\n",t_store-t);
for(i=0;i<m;i++)
{fprintf(out,"%f\n",((0.25*wp[i])+(0.5*owp[i])+(0.25*oowp[i])));
                }
}
}
