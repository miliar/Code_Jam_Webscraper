#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
    int t,i,j,k=1;
    scanf("%d",&t);
    string tmp[]={"XXXT","XXXX","XXTX","XTXX","TXXX","OOOO","OOOT","OOTO","OTOO","TOOO"};
    while(t--)
    {
        string s[4],a[10];
        for(i=0;i<4;i++)
        {
            cin>>s[i];
        }
        int c=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                a[i]+=s[j][i];
                if(s[i][j]=='.')c++;
            }
        }
        for(i=0;i<4;i++)
        {
            a[4]+=s[i][i];
            a[5]+=s[i][3-i];
            a[6+i]=s[i];
        }
        //for(i=0;i<10;i++) cout<<a[i]<<endl;
        int flag=0,pos=0;
        for(i=0;i<10;i++)
        {
            for(j=0;j<10;j++)
            {
                if(a[i]==tmp[j])
                    {flag=1;pos=j;
                break;}
            }
        }
        if(flag==1)
        {
            if(pos<=4) cout<<"Case #"<<k<<": X won\n";
            else cout<<"Case #"<<k<<": O won\n";
        }
        else
        {
            if(c>0) cout<<"Case #"<<k<<": Game has not completed\n";
            else cout<<"Case #"<<k<<": Draw\n";
        }
        k++;
    }
    return 0;
}
