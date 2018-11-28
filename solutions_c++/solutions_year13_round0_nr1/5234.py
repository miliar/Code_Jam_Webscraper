#include<conio.h>
#include<iostream>
using namespace std;


int main()
{
    int t,x=0;
    cin>>t;
    while(t>0)
    {
        x++;
        int i,j,c=0,flag=0;
        char inp[4][4],a,b;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>inp[i][j];
                if(inp[i][j]=='.')
                {
                    c=1;
                }

            }

        }
        for(i=0;i<4;i++)
        {
            a=inp[i][0];
            if(a=='T')
            {
                a=inp[i][1];

            }
            if(a=='.')
            {
                continue;
            }
            for(j=1;j<4;j++)
            {
                if(a!=inp[i][j] && inp[i][j]!='T')
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                cout<<"\nCase #"<<x<<": "<<a<<" won";
                flag=2;
                break;
            }
            else
            {
                flag=0;
            }
        }
        if(flag==2)
        {
            t--;
            flag=0;
            continue;
        }
        for(j=0;j<4;j++)
        {
            a=inp[0][j];
            if(a=='T')
            {
                a=inp[1][j];
            }
            if(a=='.')
            {
                continue;
            }
            for(i=1;i<4;i++)
            {
                if(inp[i][j]!=a && inp[i][j]!='T')
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                cout<<"\nCase #"<<x<<": "<<a<<" won";
                flag=2;
                break;
            }
            else
            {
                flag=0;
            }
        }
        if(flag==2)
        {
            t--;
            continue;
        }
        a=inp[0][0];
        if(a=='T')
        {
            a=inp[1][1];
        }
        if(a!='.')
        {
            if ((inp[1][1]== a || inp[1][1]=='T') && (inp[2][2]== a || inp[2][2]=='T') && (inp[3][3]== a || inp[3][3]=='T'))
            {
                cout<<"\nCase #"<<x<<": "<<a<<" won";
                t--;
                continue;
            }
        }
        a=inp[0][3];
        if(a=='T')
        {
            a=inp[1][2];
        }
        if(a!='.')
        {

            if ((inp[1][2]== a || inp[1][2]=='T') && (inp[2][1]== a || inp[2][1]=='T') && (inp[3][0]== a || inp[3][0]=='T'))
            {
                cout<<"\nCase #"<<x<<": "<<a<<" won";
                t--;
                continue;
            }
        }
        if(c==1)
        {
            cout<<"\nCase #"<<x<<": Game has not completed";
        }
        else
        {
            cout<<"\nCase #"<<x<<": Draw";
        }
        t--;
    }
}
