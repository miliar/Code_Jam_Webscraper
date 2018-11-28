#include<iostream>
#include<cstdio>

using namespace std;
#define WHITE 0
#define BLUE 1
#define RED1 2
#define RED2 3
#define RED3 4
#define RED4 5
int main()
{
    int T;
    scanf("%d",&T);
    for(int kase=1;kase <= T ; kase++)
    {
      int R,C;
      scanf("%d%d",&R,&C);
      getchar();
      string A[R];
      for(int i=0;i<R;i++)
        cin>>A[i];
      int B[R][C];
      for(int i = 0; i < R ; i ++ ) 
        for(int j = 0 ;j<C;  j++)
        {
          if(A[i][j]=='#')
            B[i][j]=BLUE;
          else B[i][j]=WHITE;
        }
      for(int i=0;i<R-1;i++)
        for(int j=0;j<C-1;j++)
        {
          if(B[i][j]==BLUE)
          {
            if(B[i][j]==BLUE && B[i+1][j]==BLUE && B[i][j+1]==BLUE && B[i+1][j+1]==BLUE)
            {
              B[i][j]=RED1;
              B[i][j+1]=RED2;
              B[i+1][j]=RED3;
              B[i+1][j+1]=RED4;
            }
          }
        }
      bool is=true;
      for(int i=0;i<R;i++)
        for(int j=0;j<C;j++)
          if(B[i][j]==BLUE)
            is=false;
      if(is)
      {
        for(int i=0;i<R;i++)
          for(int j=0;j<C;j++)
          {
            if(B[i][j]==RED1)
              A[i][j]='/';
            else if(B[i][j]==RED2)
            {
              A[i][j]='\\';
            }
            else if(B[i][j]==RED3)
            {
              A[i][j]='\\';
            }
            else
              if(B[i][j]==RED4)
              {
                A[i][j]='/';
              }
          }
      }
      printf("Case #%d:\n", kase);
      if(is)
      {
        for(int i=0;i<R;i++)
          cout<<A[i]<<"\n";

      }
      else cout<<"Impossible\n";
    }

}
