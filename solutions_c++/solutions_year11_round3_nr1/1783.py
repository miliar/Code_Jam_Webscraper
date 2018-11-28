#include<cstdio>
#include<cstring>
#include<iostream.h>
#include<conio.h>

using namespace std;
int i,j;
int r,c;
char row[55][55];
int f=1;

void replace()
{
   
  
   if(j==c-1)f=0;
   else if((row[i][j+1]=='#')&&(row[i+1][j]=='#')&&(row[i+1][j+1]=='#'))
   {
   
   row[i][j]='/';
   row[i][j+1]='\\';
   row[i+1][j]='\\';
   row[i+1][j+1]='/';
   f=1;
   }
   else f=0;
}  


int main()
{
    
    int t,test;
    
    
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&t);
    test=t;
    
    
    
    while(t--)
    {
            f=1;
            scanf("%d",&r);
            scanf("%d\n",&c);
            
            printf("Case #%d:\n",test-t);
                        
            for(i=0;i<r;i++)
            gets(row[i]);
            
            
            
            for(i=0;i<r;i++)
            {
                            for(j=0;j<c;j++)
                            {
                                            if(row[i][j]=='#')
                                            {
                                                              replace();
                                                              //for(i=0;i<r;i++)
                                                              //puts(row[i]);
                                                              if(f==0)break;
                                            }
                                            if(f==0)break;
                            }
                            if(f==0)break;
            } 
            if(f==0)printf("Impossible\n");
            else if(f==1)
            {
                 for(i=0;i<r;i++)
                 puts(row[i]);
            }
    }
            
            //getch();
}
                        
