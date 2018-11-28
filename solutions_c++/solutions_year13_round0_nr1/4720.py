#include<cstdio>
char s[5][5];
int main()
{
    int T;
    scanf("%d",&T);
    int time=0;
    while(T--)
    {
        time++;
        int status=0;
        for(int i=0;i<4;i++)scanf("%s",s[i]);
        //for(int i=0;i<4;i++)printf("%s\n",s[i]);
        for(int i=0;i<4;i++)
        {
            int sum=0,sum2=0;
            for(int j=0;j<4;j++)
            {
                if(s[i][j]=='.'){status=3;sum+=0;}
                else if(s[i][j]=='T')sum+=100;
                else if(s[i][j]=='O')sum+=1;
                else if(s[i][j]=='X')sum+=10;
                if(s[j][i]=='.'){status=3;sum2+=0;}
                else if(s[j][i]=='T')sum2+=100;
                else if(s[j][i]=='O')sum2+=1;
                else if(s[j][i]=='X')sum2+=10;
            }
            //printf("%d\n",sum2);
            if(sum==103||sum==4||sum2==103||sum2==4){status=1;break;}
            else if(sum==130||sum==40||sum2==130||sum2==40){status=2;break;}
        }
        if(status!=1&&status!=2)
        {
            int sum=0,sum2=0;
            for(int i=0;i<4;i++)
            {
                if(s[i][i]=='.'){status=3;sum+=0;}
                else if(s[i][i]=='T')sum+=100;
                else if(s[i][i]=='O')sum+=1;
                else if(s[i][i]=='X')sum+=10;
                if(s[3-i][i]=='.'){status=3;sum2+=0;}
                else if(s[3-i][i]=='T')sum2+=100;
                else if(s[3-i][i]=='O')sum2+=1;
                else if(s[3-i][i]=='X')sum2+=10;
            }
            if(sum==103||sum==4||sum2==103||sum2==4){status=1;}
            else if(sum==130||sum==40||sum2==130||sum2==40){status=2;}
        }
        printf("Case #%d: ",time);
        if(status==0)puts("Draw");
        else if(status==1)puts("O won");
        else if(status==2)puts("X won");
        else puts("Game has not completed");
    }
}
