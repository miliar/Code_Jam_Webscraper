#include<iostream>
using namespace std;

int main()
{
    string a;
    int mark[4][4],sum1=0,sum2=0,flag=0,win=-1,T;
    cin>>T;
    for(int t=1; t<=T; t++)
    {   flag=0;
        win=-1;
        for(int i=0; i<4; i++)
        {
            cin>>a;
            for(int j=0; j<4; j++)
            {
                if(a[j]=='O') mark[i][j]=-1;
                if(a[j]=='X') mark[i][j]=1;
                if(a[j]=='T') mark[i][j]=0;
                if(a[j]=='.')
                {
                    mark[i][j]=-9;
                    flag=1;
                }
            }
        }
        cout<<"Case #"<<t<<": ";
        for(int i=0; i<4; i++)
        {
            sum1=0;sum2=0;
            for(int j=0; j<4; j++)
            {
                sum1=sum1+mark[i][j];
                sum2=sum2+mark[j][i];
            }
            if(sum1==-3||sum1==-4||sum2==-3||sum2==-4)
                win=1;
            if(sum1==3||sum1==4||sum2==3||sum2==4)
                win=2;
        }
        sum1=0;sum2=0;
        for(int i=0; i<4; i++)
        {
            sum1+= mark[i][i];
            sum2+= mark[i][3-i];
        }

        if(sum1==-3||sum1==-4||sum2==-3||sum2==-4)
            win=1;
        if(sum1==3||sum1==4||sum2==3||sum2==4)
             win=2;
        if(win==1)
            cout<<"O won\n";
        else if(win==2)
            cout<<"X won\n";
        else if(flag==0)
            cout<<"Draw\n";
        else
            cout<<"Game has not completed\n";
    }

    return 0;
}
