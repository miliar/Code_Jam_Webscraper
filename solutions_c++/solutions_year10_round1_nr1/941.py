#include <iostream>
using namespace std;
char c[100][100];
int  t,n,k;

bool panduan(int x,int y,char ch)
{int i,j;
for(i=x;i<=x+k-1;i++)
  {if(c[i][y]!=ch)break;
   if(i==x+k-1)return true;
  }
for(j=y;j<=y+k-1;j++)
    {if(c[x][j]!=ch)break;
     if(j==y+k-1)return true;
    }  
for(i=x,j=y;i<=x+k-1,j<=y+k-1;i++,j++)
  {if(c[i][j]!=ch)break;
   if(i==x+k-1)return true;
  }
for(i=x,j=y;i>=x-k+1,j<=y+k-1;i--,j++)
  {if(c[i][j]!=ch)break;
   if(i==x-k+1)return true;
  }
return false;   
}

bool blue()
{
for(int i=1;i<=n;i++)
  for(int j=0;j<n;j++)
    {
     if(panduan(i,j,'B'))return true;   
    }  
return false;  
}
bool red()
{
    for(int i=1;i<=n;i++)
  for(int j=0;j<n;j++)
    {
     if(panduan(i,j,'R'))return true;   
    }
return false;  
}

int main()
{
scanf("%d",&t);
for(int p=1;p<=t;p++)
 {   memset(c,0,sizeof(c));
     scanf("%d%d",&n,&k);
     for(int i=1;i<=n;i++)
       {scanf("%s",c[i]);
        for(int j=n-1;j>=0;j--)
          if(c[i][j]!='R'&&c[i][j]!='B')
          for(int j2=j-1;j2>=0;j2--)
             if(c[i][j2]=='R'||c[i][j2]=='B')
                {c[i][j]=c[i][j2];               
                 c[i][j2]='.';
                 break;
                }
        //printf("%s\n",c[i]);     
       }   
     if(blue()&&!red())printf("Case #%d: Blue\n",p);  
     else if(blue()&&red())printf("Case #%d: Both\n",p);
     else if(!blue()&&red())printf("Case #%d: Red\n",p);
     else if(!blue()&&!red())printf("Case #%d: Neither\n",p);
 }
return 0;    
}

