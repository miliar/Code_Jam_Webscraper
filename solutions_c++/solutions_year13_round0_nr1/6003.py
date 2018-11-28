#include<string>
#include<iostream>
#include<cstdio>
using namespace std;
bool test(char c[5][5],char C)
{
    int i,j,k;
    int ch=0;
    for(int k=0;k<4;k++)
        if(c[k][k]==C)
        ch++;
    if(ch>3)
        return true ;
    ch=0;
        for(int k=3;k>=0;k--)
        if(c[k][3-k]==C)
            ch++;
         if(ch>3)
        return true ;
        for(int i=0;i<4;i++)
          {
                if(c[i][0]==C)
                {
                            ch=0;
                            for(int j=0;j<4;j++)
                            if(c[i][j]==C) ch++;
                              if(ch>3)
                                return true ;
                }
          }
          for(int i=0;i<4;i++)
          {
                if(c[0][i]==C)
                {
                            ch=0;
                            for(int j=0;j<4;j++)
                            if(c[j][i]==C) ch++;
                              if(ch>3)
                                return true ;
                }
          }


    return false ;
}

main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin>>t;
    bool X,O;
    char x[5][5],o[5][5];
    for(int v=1;v<t+1;v++)
    {
        for(int i=0;i<4;i++)
        {
            cin>>x[i];
            for(int j=0;j<4;j++)
            {
                o[i][j]=x[i][j];
                if(x[i][j]=='T')
                {
                    x[i][j]='X';
                     o[i][j]='O';
                }
            }
        }
        X=test(x,'X');
        O=test(o,'O');
        printf("Case #%d: ",v);
        if(!X&&!O)
        {
            bool test=true ;
            for(int i=0;i<4;i++)
                        for(int j=0;i<4;i++)
                        if(x[i][j]=='.')
                        {
                        test=false;break;
                        }
                        if(test )
                        printf("Draw\n");
                        else
                            printf("Game has not completed\n");
        }
        else if(X)
            printf("X won\n");
        else
            printf("O won\n");
    }

   return 0;
}
