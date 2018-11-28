#include<stdio.h>
int z;
int horizon(char a[][4][4],int t,char y)
{int k,j,x,v;
     for(j=0;j<4;j++)
{x=0;
         for(k=0;k<4;k++)
            {if(a[t][j][k]==y || a[t][j][k]=='T')x++;}
      if(x==4)
      {printf("Case #%d: %c won\n",t+1,y); z++;return 1; }
      else {if(j==3)return 0;}
      }
      }
int vertical(char a[][4][4],int t,char y)
{int k,j,x,v;
 
     for(j=0;j<4;j++)
{v=0;
         for(k=0;k<4;k++)
         {if(a[t][k][j]==y || a[t][k][j]=='T') v++;}
      if(v==4)
      {printf("Case #%d: %c won\n",t+1,y); z++;return 1; }
      else {if(j==3)return 0;}
      }
      }

int diagonal(char a[][4][4],int t,char y)
{int i,j,x=0,v;
for(j=0;j<4;j++)
{if(a[t][j][j]==y || a[t][j][j]=='T')x++;}
j=4;v=0;
for(i=0;i<4;i++)
{j--;
if(a[t][i][j]==y || a[t][i][j]=='T') v++;}
      if(x==4 || v==4)
      {printf("Case #%d: %c won\n",t+1,y); z++; return 1;}
      else return 0;
}

int main()
{
int t,i,j,k;
freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
scanf("%d\n",&t);
char a[t][4][4];
for(i=0;i<t;i++)
{for(j=0;j<4;j++)
{for(k=0;k<4;k++)
scanf("%c",&a[i][j][k]);
scanf("\n");
}
scanf("\n");
}
int mc;
//end of input
for(i=0;i<t;i++)
{mc=0;
z=0;
                for(j=0;j<4;j++)
 for(k=0;k<4;k++)
if(a[i][j][k]!='.') mc++;
 if(horizon(a,i,'X'))continue;
 if(vertical(a,i,'X'))continue;
 if(horizon(a,i,'O'))continue; 
 if(vertical(a,i,'O'))continue;
if(diagonal(a,i,'X'))continue;
if(diagonal(a,i,'O'))continue;

if(mc==16 && z==0)
printf("Case #%d: Draw\n",i+1); 
else
{if(z==0)
    printf("Case #%d: Game has not completed\n",i+1);} 


}//end of i fo
         
return 0;
}
