#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;

char a[4][5];

bool func(char ch)
{
    int i;
    for(i=0;i<4;i++)
        if(a[i][0]==ch&&a[i][1]==ch&&a[i][2]==ch&&a[i][3]==ch) return 1;
    for(i=0;i<4;i++)
        if(a[0][i]==ch&&a[1][i]==ch&&a[2][i]==ch&&a[3][i]==ch) return 1;
    if(a[0][0]==ch&&a[1][1]==ch&&a[2][2]==ch&&a[3][3]==ch) return 1;
    if(a[0][3]==ch&&a[1][2]==ch&&a[2][1]==ch&&a[3][0]==ch) return 1;
    return 0;

}

int main()
{
    int t,i,w,j,posi,posj;
    char s[10];
    //bool flag;
    scanf("%d\n",&t);
    for(w=1;w<=t;w++)
    {
        for(j=0;j<4;j++)
            gets(a[j]);
            gets(s);

        for(i=0;i<4;i++)
       {
           for(j=0;j<4;j++)
        if(a[i][j]=='T') break;
        if(a[i][j]=='T')break;

       }

         if(i!=4)   a[i][j]='X';
            if(func('X'))
            {
                printf("Case #%d: X won\n",w);continue;
            }
          if(i!=4)    a[i][j]='O';
            if(func('O'))
            {
                printf("Case #%d: O won\n",w);continue;
            }
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                if(a[i][j]=='.')  break;
                if(a[i][j]=='.') break;

            }

            if(i==4)
                printf("Case #%d: Draw\n",w);
            else
                printf("Case #%d: Game has not completed\n",w);
    }


}
