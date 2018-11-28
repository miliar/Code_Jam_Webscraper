#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
char a[5][5];
int dot=0;
char solve()
{
    int i,j,k,l,m,n,count;
    char c,d;
    dot=0;
    for(k=0;k<4;k++)
    {
        for(m=0;m<4;m++)
        {
            if(a[k][m]=='.')
            {
                dot=1;
                break;
            }
        }
        c=a[k][0];
        if(c=='.')
            continue;
        j=1;
        count=1;
        if(c=='T')
        {
            c=a[k][j];
            if(c=='.')
                continue;
            j=2;
            count=2;
        }
        for(i=j;i<4;i++)
        {
            d=a[k][i];
            if((c==d)||(d=='T'))
                count++;
            else
                break;
        }
        if(count==4)
        {
            return c;
        }
    }
    for(k=0;k<4;k++)
    {
        for(m=0;m<4;m++)
        {
            if(a[m][k]=='.')
            {
                dot=1;
                break;
            }
        }
        c=a[0][k];
        if(c=='.')
            continue;
        j=1;
        count=1;
        if(c=='T')
        {
            c=a[j][k];
            if(c=='.')
                continue;
            j=2;
            count=2;
        }
        for(i=j;i<4;i++)
        {
            d=a[i][k];
            if((c==d)||(d=='T'))
                count++;
            else
                break;
        }
        if(count==4)
        {
            return c;
        }
    }
    c=a[0][0];
    j=1;
    count=1;
    if(c=='.')
        count=-1;
    if(c=='T')
    {
        c=a[j][j];
        j=2;
        count=2;
        if(c=='.')
            count=-1;
    }
    for(k=j;k<4;k++)
    {
        d=a[k][k];
        if((c==d)||(d=='T'))
            count++;
        else
            break;
    }
    if(count==4)
    {
        return c;
    }
    c=a[0][3];
    if(c=='.')
        count=-1;
    j=1;
    count=1;
    if(c=='T')
    {
        c=a[1][2];
        if(c=='.')
            count=-1;
        j=2;
        count=2;
    }
    else
    {
        if((c==a[1][2])||(a[1][2]=='T'))
            count++;
    }
    if((c==a[2][1])||(a[2][1]=='T'))
        count++;
    if((c==a[3][0])||(a[3][0]=='T'))
        count++;
    if(count==4)
    {
        return c;
    }
    if(dot==1)
    {
        return '.';
    }
    else
    {
        return '-';
    }
}
int main()
{
    int i,j,k,l,m,n,t;
    char val;
    string y;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        for(i=0;i<4;++i)
        {
            cin>>a[i];
        }
        getline(cin,y);
        val=solve();
        if((val=='X')||(val=='O'))
        {
            cout<<"Case #"<<k<<": "<<val<<" won"<<endl;
        }
        else if(val=='.')
        {
            cout<<"Case #"<<k<<": Game has not completed"<<endl;
        }
        else
        {
            cout<<"Case #"<<k<<": Draw"<<endl;
        }
    }
    return 0;
}
