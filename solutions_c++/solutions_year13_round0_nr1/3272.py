#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int test,i,j,t,k,X,O,freqdot,result,dot;
    string arr[4];
    int ct=0;
    char c,d;
    cin>>test;
    while(test--)
    {
        for(i=0;i<4;i++)
        {
            cin>>arr[i];
            //cout<<arr[i]<<"\n";;
        }
        result=0;
        dot=X=O=t=0;
        //horizontal
        for(i=0;i<4;i++)
        {
            X=O=t=0;
            for(j=0;j<4;j++)
            {
                if(arr[i][j]=='.')
                    dot++;
                else if(arr[i][j]=='T')
                    t++;
                else if(arr[i][j]=='X')
                    X++;
                else if(arr[i][j]=='O')
                    O++;
            }
            if(X==4 || (X==3 && t==1))
            {
                    result=1;
                    break;
            }
            if(O==4 || (O==3 && t==1))
            {
                    result=2;
                    break;
            }
        }
        X=O=t=0;
        if(result==0)
        {
            //vertical
            for(j=0;j<4;j++)
            {
                X=O=t=0;
                for(i=0;i<4;i++)
                {
                    if(arr[i][j]=='.')
                        dot++;
                    else if(arr[i][j]=='T')
                        t++;
                    else if(arr[i][j]=='X')
                        X++;
                    else if(arr[i][j]=='O')
                        O++;
                }
                if(X==4 || (X==3 && t==1))
                {
                        result=1;
                        break;
                }
                if(O==4 || (O==3 && t==1))
                {
                        result=2;
                        break;
                }
            }
        }
        X=O=t=0;
        if(result==0)
        {
            //diagonal 1
            for(j=0;j<4;j++)
            {
                for(i=j;i<j+1;i++)
                {
                    if(arr[i][j]=='.')
                        dot++;
                    else if(arr[i][j]=='T')
                        t++;
                    else if(arr[i][j]=='X')
                        X++;
                    else if(arr[i][j]=='O')
                        O++;
                }
                if(X==4 || (X==3 && t==1))
                {
                        result=1;
                        break;
                }
                if(O==4 || (O==3 && t==1))
                {
                        result=2;
                        break;
                }
            }
        }
         X=O=t=0;
        if(result==0)
        {
            //diagonal 2
            for(j=0;j<4;j++)
            {
                for(i=3-j;i<3-j+1;i++)
                {
                    if(arr[i][j]=='.')
                        dot++;
                    else if(arr[i][j]=='T')
                        t++;
                    else if(arr[i][j]=='X')
                        X++;
                    else if(arr[i][j]=='O')
                        O++;
                }
                if(X==4 || (X==3 && t==1))
                {
                        result=1;
                        break;
                }
                if(O==4 || (O==3 && t==1))
                {
                        result=2;
                        break;
                }
            }
        }
        ct++;
        if(result==1)
            cout<<"Case #"<<ct<<": X won";
        else if(result==2)
            cout<<"Case #"<<ct<<": O won";
        else if(dot>0)
            cout<<"Case #"<<ct<<": Game has not completed";
        else cout<<"Case #"<<ct<<": Draw";
        cout<<"\n";
    }

}













