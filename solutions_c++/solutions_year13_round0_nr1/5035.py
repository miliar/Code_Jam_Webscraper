#include<iostream>
using namespace std;
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int C;
    char c,s[4][4];
    cin>>C;
    for (int T=1;T<=C;++T)
    {
        c=getchar();      
        for (int i=0;i<4;++i)
          {
            for (int j=0;j<4;++j)
              s[i][j]=getchar();
            c=getchar();
          }
     //   if (T<C) c=getchar();
        int x,o,t=0;
        x=o=0;
        for (int i=0;i<4;++i)
          switch (s[i][i])
              {
                case 'X': ++x;break;
                case 'O': ++o;break;
                case 'T': ++x;++o;break;
              }
        if (x<4&&o<4)
        {
         x=o=0;
        for (int i=0;i<4;++i)
          switch (s[i][3-i])
              {
                case 'X': ++x;break;
                case 'O': ++o;break;
                case 'T': ++x;++o;break;
              }
        }
        if (x<4&&o<4)
        for (int i=0;i<4;++i)
        {
            x=o=0;
            for (int j=0;j<4;++j)
              switch (s[i][j])
              {
                case 'X': ++x;++t;break;
                case 'O': ++o;++t;break;
                case 'T': ++x;++o;++t;break;
              }
            if (x==4||o==4) break;
            x=o=0;
            for (int j=0;j<4;++j)
              switch (s[j][i])
              {
                case 'X': ++x;break;
                case 'O': ++o;break;
                case 'T': ++x;++o;break;
              }
            if (x==4||o==4) break;
        }
        printf("Case #%d: ",T);
        if (x==4) printf("X won\n");
        else if (o==4) printf("O won\n");
        else if (t==16) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    //system("pause");
    return 0;
} 
