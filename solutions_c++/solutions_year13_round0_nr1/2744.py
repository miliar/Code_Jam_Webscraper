#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
string ch[4];
int check(char x)
{
    int c1=0,c2=0;
    int i,j;
    int row=0;
    int col=0;
    int ans=0;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(i==j&&(ch[i][j]==x||ch[i][j]=='T'))
            c1++;
            if(i+j==3&&(ch[i][j]==x||ch[i][j]=='T'))
            c2++;
            if((ch[i][j]==x||ch[i][j]=='T'))
            row++;
        }
        if(row==4)
        ans=1;
        row=0;
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if((ch[j][i]==x||ch[j][i]=='T'))
            col++;
        }
        if(col==4)
        ans=1;
        col=0;
    }
    if(ans==1)
    return 1;
    if(c1==4||c2==4)
    return 1;
    return 0;
    
}
int main()
{
    int t;
    freopen("C:\\Users\\Gaurav\\Desktop\\A-large.in","r",stdin);
    freopen("C:\\Users\\Gaurav\\Desktop\\output.txt","w",stdout);
    cin>>t;
    //cout<<" X won"<<endl;
    int k=0;
    while(t--)
    {
        k++;
        //cout<<": X won"<<endl;
        int i,j;
        for(i=0;i<4;i++)
        cin>>ch[i];
        if(check('X'))
        cout<<"Case #"<<k<<": X won"<<endl;
        else if(check('O'))
        cout<<"Case #"<<k<<": O won"<<endl;
        else
        {
            int val=0;
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(ch[i][j]=='.')
                    val=1;
                }
            }
            if(val==1)
            cout<<"Case #"<<k<<": Game has not completed"<<endl;
            else
            cout<<"Case #"<<k<<": Draw"<<endl;
        }
    }
    return 0;
}
