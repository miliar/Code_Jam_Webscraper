#include<iostream>
#include<string.h>
using namespace std;
    int m,n;
char board[666][666];
char mode[16][6]={"0000","0001","0010","0011","0100",
               "0101","0110","0111","1000","1001",
               "1010","1011","1100","1101","1110",
               "1111"};
char from[20]="0123456789ABCDEF";
void make(int id, char *s)
{
     board[id][0]=0;
     for(; *s; s++)
     {
         for(int i=0; i<16; i++)
         if(from[i]==*s)
         {
             strcat(board[id], mode[i]);
             break;
         }
     }
}

bool check(int x,int y, int size)
{if(size==1) return board[x][y]!='9';
     if(x+size>m || y+size >n ) return false;
     for(int i=x; i<x+size; i++)
     {
          if(i!=x)
          {
              if(board[i][y]+board[i-1][y]-'0'*2 != 1)
              return false;
          }
          for(int j=y+1; j<y+size; j++)
          {
              if(board[i][j]+board[i][j-1]-'0'*2 != 1)
              return false;
          }
     }
     return true;
}

void mark(int x, int y, int size)
{
     for(int i=x; i<x+size; i++)
     for(int j=y; j<y+size; j++)
     board[i][j]='9';
}

int main()
{
    freopen("C:\\Users\\Administrator\\Desktop\\IN1.txt","r",stdin);
    freopen("C:\\Users\\Administrator\\Desktop\\OUT.txt","w",stdout);
    int test;

    scanf("%d",&test);
    char tmp[20];
    int t=1;
    while(test--)
    {
        scanf("%d%d",&m,&n);
        for(int i=0; i<m; i++)
        {
            scanf("%s",tmp);
            make(i,tmp);
            //puts(board[i]);
        }//puts("");
        int ans[40]={0};
        for(int i=max(n,m); i>0; i--)
        {
            for(int j=0; j<m; j++)
            {
                for(int k=0; k<n; k++)
                {
                     if(check(j,k,i))
                     {
                         ans[i]++;
                         mark(j,k,i);
                         ///for(int x=0; x<m; x++)
                         //puts(board[x]);puts("");
                     }
                }
            }
        }
        int c=0;
        for(int i=1; i<40; i++)
        c+=ans[i]>0;
        printf("Case #%d: %d\n",t++, c);
        for(int i=39; i>0;i--)
        {
            if(ans[i])
            printf("%d %d\n",i,ans[i]);
        }
    }
}
