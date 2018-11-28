#include<iostream>
using namespace std;
char str[100][100];
int main()
{
    int cases;
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++)
    {
        int r,c;
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++)
        {
            scanf("%s",str[i]);
        }
        bool judge =true;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(str[i][j]=='#')
                {
                    if(str[i+1][j]!='#'||str[i][j+1]!='#'||str[i+1][j+1]!='#')
                    {
                        judge =false;
                        break;
                    }
                    else
                    {
                        str[i][j]='/';
                        str[i][j+1]='\\';
                        str[i+1][j]='\\';
                        str[i+1][j+1]='/';
                    }
                }
            }
            if(!judge) break;
        }
        printf("Case #%d:\n",ca);
        if(!judge)
        puts("Impossible");
        else
        {
            for(int i=0;i<r;i++)
            puts(str[i]);
        }

    }
}
