#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int main()
{
    //freopen("C:\\Users\\Utkarsh\\Desktop\\input.in","r",stdin);
     //freopen("C:\\Users\\Utkarsh\\Desktop\\out.txt","w",stdout);
    int t,i,j,k,l;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        string s[5],s1;
        int flag=0;
        for(i=0;i<4;i++)
            cin>>s[i];
        for(i=0;i<4;i++)
        {
            if(s[i]=="XXXX"||s[i]=="XXXT"||s[i]=="XXTX"||s[i]=="XTXX"||s[i]=="TXXX")
            {
                printf("Case #%d: X won\n",k);
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
           for(i=0;i<4;i++)
           {
            if(s[i]=="OOOO"||s[i]=="OOOT"||s[i]=="OOTO"||s[i]=="OTOO"||s[i]=="TOOO")
            {
                printf("Case #%d: O won\n",k);
                flag=1;
                break;
            }
           }
        }
        if(flag==0)
        {
            s1=s[0][0];
            for(i=1;i<4;i++)
            {
                s1=s1+s[i][i];
            }
            if(s1=="XXXX"||s1=="XXXT"||s1=="XXTX"||s1=="XTXX"||s1=="TXXX")
            {
                printf("Case #%d: X won\n",k);
                flag=1;
            }
           else if(s1=="OOOO"||s1=="OOOT"||s1=="OOTO"||s1=="OTOO"||s1=="TOOO")
            {
                printf("Case #%d: O won\n",k);
                flag=1;
            }

        }
        if(flag==0)
        {
            s1=s[0][3];
            l=3;
            for(i=1;i<4;i++)
            {
              s1=s1+s[i][l-i];
            }
            if(s1=="XXXX"||s1=="XXXT"||s1=="XXTX"||s1=="XTXX"||s1=="TXXX")
            {
                printf("Case #%d: X won\n",k);
                flag=1;
            }
           else if(s1=="OOOO"||s1=="OOOT"||s1=="OOTO"||s1=="OTOO"||s1=="TOOO")
            {
                printf("Case #%d: O won\n",k);
                flag=1;
            }
        }
        if(flag==0)
        {
            for(i=0;i<4;i++)
            {
              string s2;
              s2=s2+s[0][i];
              for(j=1;j<4;j++)
              {
                  s2=s2+s[j][i];
              }
            if(s2=="XXXX"||s2=="XXXT"||s2=="XXTX"||s2=="XTXX"||s2=="TXXX")
            {
                printf("Case #%d: X won\n",k);
                flag=1;
            }
           else if(s2=="OOOO"||s2=="OOOT"||s2=="OOTO"||s2=="OTOO"||s2=="TOOO")
            {
                printf("Case #%d: O won\n",k);
                flag=1;
            }
            }
        }
        if(flag==0)
        {
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(s[i][j]=='.')
                    {
                        printf("Case #%d: Game has not completed\n",k);
                        flag=1;
                        break;
                    }
                }
                if(flag==1)
                    break;
            }
        }
        if(flag==0)
            printf("Case #%d: Draw\n",k);
    }
    return 0;
}
