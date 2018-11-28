#include<iostream>
#include<cstdio>
using namespace std;
int input[4][4];
int fun()
{
    int X,T,O;
    for(int i=0;i<4;i++)
    {
        X=O=T=0;
        for(int j=0;j<4;j++)
        {
            if(input[i][j]==0)
            X++;
            if(input[i][j]==2)
            T++;
            if(input[i][j]==1)
            O++;
        }
        if(X==4 || (X==3&&T==1))
        return 1;
        if(O==4 || (O==3&&T==1))
        return 2;
    }

    for(int i=0;i<4;i++)
    {
        X=O=T=0;
        for(int j=0;j<4;j++)
        {
            if(input[j][i]==0)
            X++;
            if(input[j][i]==2)
            T++;
            if(input[j][i]==1)
            O++;
        }
        if(X==4 || (X==3&&T==1))
        return 1;
        if(O==4 || (O==3&&T==1))
        return 2;
    }

    X=O=T=0;
    for(int j=0;j<4;j++)
    {
        if(input[j][j]==0)
        X++;
        if(input[j][j]==2)
        T++;
        if(input[j][j]==1)
        O++;
    }
    if(X==4 || (X==3&&T==1))
    return 1;
    if(O==4 || (O==3&&T==1))
    return 2;

    X=O=T=0;
    for(int j=0;j<4;j++)
    {
        if(input[j][3-j]==0)
        X++;
        if(input[j][3-j]==2)
        T++;
        if(input[j][3-j]==1)
        O++;
    }
    if(X==4 || (X==3&&T==1))
    return 1;
    if(O==4 || (O==3&&T==1))
    return 2;
    return 0;
}
int main()
{
    char c;
    int t,x=1,flag,k,i,j;
    cin>>t;
    while(t--)
    {
        flag=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>c;
                if(c=='X')
                input[i][j]=0;
                else if(c=='O')
                input[i][j]=1;
                else if(c=='T')
                input[i][j]=2;
                else
                input[i][j]=3;
            }
        }
//        for(i=0;i<4;i++)
//        {
//            for(j=0;j<4;j++)
//            {
//                cout<<input[i][j]<<" ";
//            }
//            cout<<"\n";
//        }
        k=fun();
        if(k==1)
        {
            printf("Case #%d: X won\n",x);
        }
        else if(k==2)
        {
            printf("Case #%d: O won\n",x);
        }
        else
        {
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(input[i][j]==3)
                    {
                        flag=1;
                       break;
                    }
                }
                if(flag==1)
                break;
            }
            if(i==4 &&j==4)
            printf("Case #%d: Draw\n",x);//draw
            else
            printf("Case #%d: Game has not completed\n",x);
        }
        x++;
    }
    return 0;
}
