#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
    freopen("1.txt","r",stdin);
    freopen("a1.txt","w",stdout);
    int tc,x,o,t,d,flag=0,com=0;
    string str[4];
    cin>>tc;
    for(int xx=1;xx<=tc;xx++)
    {
        cin>>str[0];
        cin>>str[1];
        cin>>str[2];
        cin>>str[3];
        x=0;o=0;t=0;flag=0;com=0;d=0;

        for(int i=0;i<4;i++)
        {
            x=0;t=0;o=0;
            for(int j=0;j<4;j++)
            {
                if(str[i][j]=='X')
                    {x++;d++;}
                else if(str[i][j]=='T')
                    {t++;d++;}
                else if(str[i][j]=='O')
                    {o++;d++;}
            }
            if((d)==16)
            {
                com=1;
            }
            if((x+t)==4||(o+t)==4)
            {
                    flag=1;
                    break;
            }
        }

        if(flag==0)
        {
            d=0;
            for(int j=0;j<4;j++)
            {
                x=0;t=0;o=0;
                for(int i=0;i<4;i++)
                {

                    if(str[i][j]=='X')
                        {x++;d++;}
                    else if(str[i][j]=='T')
                        {t++;d++;}
                    else if(str[i][j]=='O')
                        {o++;d++;}
                }
                if((d)==16)
                {
                    com=1;
                }
                if((x+t)==4||(o+t)==4)
                {

                        flag=1;
                        break;
                }

            }
        }


        if(flag==0)
        {
            x=0;t=0;o=0;
                for(int i=0;i<4;i++)
                {
                    if(str[i][i]=='X')
                        x++;
                    else if(str[i][i]=='T')
                        t++;
                    else if(str[i][i]=='O')
                        o++;
                }
                if((x+t)==4||(o+t)==4)
                {

                        flag=1;
                }
        }
        if(flag==0)
        {
                x=0;t=0;o=0;
                for(int i=1;i<=4;i++)
                {
                    if(str[4-i][i-1]=='X')
                        x++;
                    else if(str[4-i][i-1]=='T')
                        t++;
                    else if(str[4-i][i-1]=='O')
                        o++;
                }

                if((x+t)==4||(o+t)==4)
                {

                        flag=1;
                }
            }

        if(flag==0&&com==0)
        {
            cout<<"Case #"<<xx<<": Game has not completed"<<endl;
        }
        else if(flag==0&&com==1)
        {
            cout<<"Case #"<<xx<<": Draw"<<endl;
        }
        else if(flag==1)
        {
            if((x+t)==4)
                cout<<"Case #"<<xx<<": X won"<<endl;
            else if((o+t)==4)
                cout<<"Case #"<<xx<<": O won"<<endl;
        }
    }
    return 0;
}
