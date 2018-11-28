#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
string s[5];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cases=1;cases<=T;cases++)
    {
        for(int i=1;i<=4;i++)
            cin>>s[i];
        int n_x=0,n_o=0,n_dot=0,n_t=0;
        for(int i=1;i<=4;i++)
            for(int j=0;j<=3;j++)
            {
                if(s[i][j]=='X')
                    n_x++;
                if(s[i][j]=='O')
                    n_o++;
                if(s[i][j]=='.')
                    n_dot++;
                if(s[i][j]=='T')
                    n_t++;
            }
            //printf("%d...%d..%d..%d\n",n_x,n_o,n_dot,n_t);
            int tag=0;
            for(int i=1;i<=4;i++)
            {
                int ans_o=0,ans_x=0;
                for(int j=0;j<=3;j++)
                {
                    if(s[i][j]=='X'||s[i][j]=='T')
                        ans_x++;
                    if(s[i][j]=='O'||s[i][j]=='T')
                        ans_o++;
                }
                if(ans_o==4)
                    tag=-1;
                if(ans_x==4)
                    tag=1;
                if(tag!=0)
                    break;
            }
            for(int i=0;i<=3;i++)
            {
                int ans_o=0,ans_x=0;
                for(int j=1;j<=4;j++)
                {
                    if(s[j][i]=='X'||s[j][i]=='T')
                        ans_x++;
                    if(s[j][i]=='O'||s[j][i]=='T')
                        ans_o++;
                }
                if(ans_o==4)
                    tag=-1;
                if(ans_x==4)
                    tag=1;
                if(tag!=0)
                    break;
            }
            int ans_o=0,ans_x=0;
            if(s[1][0]=='X'||s[1][0]=='T')
                ans_x++;
            if(s[2][1]=='X'||s[2][1]=='T')
                ans_x++;
            if(s[3][2]=='X'||s[3][2]=='T')
                ans_x++;
            if(s[4][3]=='X'||s[4][3]=='T')
                ans_x++;
            if(s[1][0]=='O'||s[1][0]=='T')
                ans_o++;
            if(s[2][1]=='O'||s[2][1]=='T')
                ans_o++;
            if(s[3][2]=='O'||s[3][2]=='T')
                ans_o++;
            if(s[4][3]=='O'||s[4][3]=='T')
                ans_o++;
            if(ans_x==4)
                tag=1;
            if(ans_o==4)
                tag=-1;

            ans_o=0,ans_x=0;
            if(s[4][0]=='X'||s[4][0]=='T')
                ans_x++;
            if(s[3][1]=='X'||s[3][1]=='T')
                ans_x++;
            if(s[2][2]=='X'||s[2][2]=='T')
                ans_x++;
            if(s[1][3]=='X'||s[1][3]=='T')
                ans_x++;
            if(s[4][0]=='O'||s[4][0]=='T')
                ans_o++;
            if(s[3][1]=='O'||s[3][1]=='T')
                ans_o++;
            if(s[2][2]=='O'||s[2][2]=='T')
                ans_o++;
            if(s[1][3]=='O'||s[1][3]=='T')
                ans_o++;
            if(ans_x==4)
                tag=1;
            if(ans_o==4)
                tag=-1;
            printf("Case #%d: ",cases);
            if(tag==1)
                printf("X won\n");
            else if(tag==-1)
                printf("O won\n");
            else
            {
                if(n_dot==0)
                    printf("Draw\n");
                else
                {
                    printf("Game has not completed\n");
                }
            }
    }
    return 0;
}
