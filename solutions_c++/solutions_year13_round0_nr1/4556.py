#include<stdio.h>
char a[1000][4][5];

int horizontal(int n)
{
    int i,j,k,d[2];
    
             for(j=0;j<4;j++)
             {
                             d[0]=d[1]=0;
                             for(k=0;k<4;k++)
                             {
                                        if(a[n][j][k]=='O')
                                                           d[0]++;
                                        if(a[n][j][k]=='X')
                                                           d[1]++;
                                        if(a[n][j][k]=='T')
                                        {
                                        d[0]++;
                                        d[1]++;
                                        }
                             }
                             if(d[0]==4)
                             {
                             printf("Case #%d: O won\n",(n+1));
                             return 1;
                             }
                             if(d[1]==4)
                             {
                                         printf("Case #%d: X won\n",(n+1));
                                         return 1;
                             }
             }                                    
return 0;
}

int vertical(int n)
{
int i,j,k,d[2];

for(i=0;i<4;i++)
{
 d[0]=d[1]=0;
 for(j=0;j<4;j++)
 {
 if(a[n][j][i]=='O')d[0]++;
 if(a[n][j][i]=='X')d[1]++;
if(a[n][j][i]=='T')
{
                   d[0]++;
                   d[1]++;
}
}

if(d[0]==4)
{
printf("Case #%d: O won\n",(n+1));
return 1;
}

if(d[1]==4)
{
printf("Case #%d: X won\n",(n+1));
return 1;
}

}
return 0;   
}

int diagonal(int n)
{
    int i,j,d[2]={0,0},e[2]={0,0};
  for(i=0;i<4;i++)
  {                      
    if(a[n][i][i]=='O') d[0]++;
    if(a[n][i][i]=='X') d[1]++;
    if(a[n][i][i]=='T')
    {
                       d[0]++;
                       d[1]++;
    }
    if(a[n][i][3-i]=='O')e[0]++;
    if(a[n][i][3-i]=='X')e[1]++;
    if(a[n][i][3-i]=='T')
    {
                       e[0]++;
                       e[1]++;
    }
  }

if(d[0]==4 || e[0]==4)
{
printf("Case #%d: O won\n",(n+1));
return 1;
}

if(d[1]==4 || e[1]==4)
{
printf("Case #%d: X won\n",(n+1));
return 1;
}

return 0;

}

int gamecomplete(int n)
{
    int i,j,k=0;
    for(i=0;i<4;i++)
    {
                    for(j=0;j<4;j++)
                    {
                                    if(a[n][i][j]=='.')
                                    {
                                      printf("Case #%d: Game has not completed\n",(n+1));
                                      return 1;
                                    }                 
                    }
    }
    
return 0;
}



int main()
{

int n;
scanf("%d",&n);
int i,j,k;

for(i=0;i<n;i++)
{
                    for(j=0;j<4;j++)
                    {
                                    scanf("%s",a[i][j]);
                    }
}


for(i=0;i<n;i++)
{
if(horizontal(i))continue;
if(vertical(i))continue;
if(diagonal(i))continue;
if(gamecomplete(i))continue;
printf("Case #%d: Draw\n",(i+1));
}

return 0;
}
