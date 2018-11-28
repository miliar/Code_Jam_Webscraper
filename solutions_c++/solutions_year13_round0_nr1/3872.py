#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<map>
#include<vector>
#include<queue>
#include<stack>

using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t;
    cin>>t;

    for(int T=1; T<=t; T++)
    {
        char a[4][4];
        int k=0;
        char d1[4],d2[4];
        int l1=0,l2=0,dot=0;

        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                cin>>a[i][j];
                if(i==j)
                    d1[l1++]=a[i][j];
                if(i==4-j-1)
                    d2[l2++]=a[i][j];
                if(a[i][j]=='.')
                    dot=1;
            }

        }

        if((d1[0]=='X'||d1[0]=='T')&&(d1[1]=='X'||d1[1]=='T')&&(d1[2]=='X'||d1[2]=='T')&&(d1[3]=='X'||d1[3]=='T'))
        {
            cout<<"Case #"<<T<<": "<<"X won\n";
            continue;
        }
        if((d2[0]=='X'||d2[0]=='T')&&(d2[1]=='X'||d2[1]=='T')&&(d2[2]=='X'||d2[2]=='T')&&(d2[3]=='X'||d2[3]=='T'))
        {
            cout<<"Case #"<<T<<": "<<"X won\n";
            continue;
        }

        if((d1[0]=='O'||d1[0]=='T')&&(d1[1]=='O'||d1[1]=='T')&&(d1[2]=='O'||d1[2]=='T')&&(d1[3]=='O'||d1[3]=='T'))
        {
            cout<<"Case #"<<T<<": "<<"O won\n";
            continue;
        }


        if((d2[0]=='O'||d2[0]=='T')&&(d2[1]=='O'||d2[1]=='T')&&(d2[2]=='O'||d2[2]=='T')&&(d2[3]=='O'||d2[3]=='T'))
        {
            cout<<"Case #"<<T<<": "<<"O won\n";
            continue;
        }


        for (int j=0; j<4; j++)
        {
            l1=0;
            for(int i=0; i<4; i++)
            {
                d1[l1++]=a[i][j];
            }

            if((d1[0]=='O'||d1[0]=='T')&&(d1[1]=='O'||d1[1]=='T')&&(d1[2]=='O'||d1[2]=='T')&&(d1[3]=='O'||d1[3]=='T'))
            {
                cout<<"Case #"<<T<<": "<<"O won\n";
                k=1;
                continue;
            }


            if((d1[0]=='X'||d1[0]=='T')&&(d1[1]=='X'||d1[1]=='T')&&(d1[2]=='X'||d1[2]=='T')&&(d1[3]=='X'||d1[3]=='T'))
            {
                cout<<"Case #"<<T<<": "<<"X won\n";
                k=1;
                continue;
            }
            if(k==1)
                continue;

        }

        if(k==0)
        {


         for (int i=0; i<4; i++)
        {
            l1=0;
            for(int j=0; j<4; j++)
            {
                d1[l1++]=a[i][j];
            }

            if((d1[0]=='O'||d1[0]=='T')&&(d1[1]=='O'||d1[1]=='T')&&(d1[2]=='O'||d1[2]=='T')&&(d1[3]=='O'||d1[3]=='T'))
            {
                cout<<"Case #"<<T<<": "<<"O won\n";
                k=1;
                continue;
            }


            if((d1[0]=='X'||d1[0]=='T')&&(d1[1]=='X'||d1[1]=='T')&&(d1[2]=='X'||d1[2]=='T')&&(d1[3]=='X'||d1[3]=='T'))
            {
                cout<<"Case #"<<T<<": "<<"X won\n";
                k=1;
                continue;
            }
            if(k==1)
                continue;


        }
        }

        if(k==0)
        {


        if(dot==1)
                 cout<<"Case #"<<T<<": "<<"Game has not completed\n";

        else
            cout<<"Case #"<<T<<": "<<"Draw\n";
        }
    }
}
