#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
string ttt[4];
int verify(char check)
{
    int i,j,r=0,c=0,flag=0,p=0,q=0,ret;
    
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
        	if((ttt[i][j]==check || ttt[i][j]=='T')) r++;
        	if(i+j==3 && (ttt[i][j]==check || ttt[i][j]=='T')) q++;
            if(i==j && (ttt[i][j]==check || ttt[i][j]=='T')) p++;
        }
        if(r==4) flag=1;
        r=0;
    }
    
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
            if(ttt[j][i]==check || ttt[j][i]=='T') c++;
        if(c==4) flag=1;
        c=0;
    }
    
    ret=0;
    if(p==4 || q==4 || flag==1) ret=1;
    return ret;
}
int main()
{
    int t;
    freopen("F:\\inputA.in","r",stdin);
    freopen("F:\\outputA.txt","w",stdout);
    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
        int i,j,flag;
        for(i=0;i<4;i++)
        	cin>>ttt[i];
        if(verify('X')) cout<<"Case #"<<cas<<": X won"<<endl;
        else if(verify('O')) cout<<"Case #"<<cas<<": O won"<<endl;
        else
        {
            flag=0;
            for(i=0;i<4;i++)
                for(j=0;j<4;j++)
                    if(ttt[i][j]=='.') flag=1;
            if(flag==1) cout<<"Case #"<<cas<<": Game has not completed"<<endl;
            else cout<<"Case #"<<cas<<": Draw"<<endl;
        }
    }
    return 0;
}
