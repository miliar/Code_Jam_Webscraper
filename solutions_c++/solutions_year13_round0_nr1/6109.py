#include<iostream>
#include<cstdio>
using namespace std;

char a[4][4];

int main()
{
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    int t;                                          //number of testcase
    char x='X',o='O',T='T',dot='.';
    int flagX,flagO,flagDot;
    cin>>t;
    string str;
    for(int i=1;i<=t;i++)                           //for each test case
    {
        flagDot=0;
        for(int j=0;j<4;j++)
        {
            cin>>str;
            for(int k=0;k<4;k++)
            {
                a[j][k]=str[k];
                if(a[j][k]==dot)
                    flagDot=1;
            }
        }

        /*for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cout<<a[j][k];
            }
            cout<<endl;
        }*/

        //test up-down left-right diagonally
        flagO=0;
        flagX=0;
        for(int j=0;j<4;j++)
        {
            if(a[j][j]!=x && a[j][j]!=T)
                flagX=1;
            if(a[j][j]!=o && a[j][j]!=T)
                flagO=1;
        }
        if(flagO==0){
            cout<<"Case #"<<i<<": O won"<<endl;
            continue;
        }
        else if(flagX==0){
            cout<<"Case #"<<i<<": X won"<<endl;
            continue;
        }

        //test up-down right-left diagonally
        flagO=0;
        flagX=0;
        for(int j=0;j<4;j++)
        {
            if(a[j][3-j]!=x && a[j][3-j]!=T)
                flagX=1;
            if(a[j][3-j]!=o && a[j][3-j]!=T)
                flagO=1;
        }
        if(flagO==0){
            cout<<"Case #"<<i<<": O won"<<endl;
            continue;
        }
        else if(flagX==0){
            cout<<"Case #"<<i<<": X won"<<endl;
            continue;
        }

        //test horizontally
        for(int j=0;j<4;j++)
        {
            flagO=0;
            flagX=0;
            for(int k=0;k<4;k++)
            {
                if(a[j][k]!=x && a[j][k]!=T)
                    flagX=1;
                if(a[j][k]!=o && a[j][k]!=T)
                    flagO=1;
            }
            if(flagO==0){
                cout<<"Case #"<<i<<": O won"<<endl;
                break;
            }
            else if(flagX==0){
                cout<<"Case #"<<i<<": X won"<<endl;
                break;
            }
        }
        if(flagX==0 || flagO==0)
            continue;


        //test vertically
        for(int j=0;j<4;j++)
        {
            flagO=0;
            flagX=0;
            for(int k=0;k<4;k++)
            {
                if(a[k][j]!=x && a[k][j]!=T)
                    flagX=1;
                if(a[k][j]!=o && a[k][j]!=T)
                    flagO=1;
            }
            if(flagO==0){
                cout<<"Case #"<<i<<": O won"<<endl;
                break;
            }
            else if(flagX==0){
                cout<<"Case #"<<i<<": X won"<<endl;
                break;
            }
        }
        if(flagX==0 || flagO==0)
            continue;
        if(flagDot==1)
            cout<<"Case #"<<i<<": Game has not completed"<<endl;
        else
            cout<<"Case #"<<i<<": Draw"<<endl;
    }
}
