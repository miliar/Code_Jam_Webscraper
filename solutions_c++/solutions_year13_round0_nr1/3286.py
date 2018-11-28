#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
int n,j;
short e,f,i,nr;
char s[5][5],*p,ch;
ifstream ci("A-large.in");
ofstream g("i.out");
void back()
{
    ci>>s[0]>>s[1]>>s[2]>>s[3];
    nr=0;
    e=0;
    f=0;
    p=strchr(s[0],'.');
    if (p!=NULL)
    {
        e=1;
    }
    else
    {
        p=strchr(s[1],'.');
        if (p!=NULL)
        {
            e=1;
        }
        else
        {
            p=strchr(s[2],'.');
            if (p!=NULL)
            {
                e=1;
            }
            else
            {
                p=strchr(s[3],'.');
                if (p!=NULL)
                {
                    e=1;
                }
            }
        }
    }
    for(i=0;i<=3&&f!=1;i++)
    {
        if ((s[i][0]=='T')&&(s[i][1]!='.'))
        {
            if ((s[i][1]==s[i][2])&&(s[i][1]==s[i][3])) nr=4;
        }
        else
        if (s[i][0]!='.')
        {
         if (((s[i][1]==s[i][0])||(s[i][1]=='T'))&& ((s[i][2]==s[i][0])||(s[i][2]=='T'))&&((s[i][3]==s[i][0])||(s[i][3]=='T'))) nr=4;

        }
        if (nr==4)
        {
            f=1;
            if (s[i][0]!='T') g<<"Case #"<<j<<": "<<s[i][0]<<" won"<<'\n';
            else g<<"Case #"<<j<<": "<<s[i][1]<<" won"<<'\n';
        }
    }
    if (f==0)
    {
        for(i=0;i<=3&&f!=1;i++)
    {
        if ((s[0][i]=='T')&&(s[1][i]!='.'))
        {
            if ((s[1][i]==s[2][i])&&(s[1][i]==s[3][i])) nr=4;
        }
        else
        if (s[0][i]!='.')
        {
         if (((s[1][i]==s[0][i])||(s[1][i]=='T'))&& ((s[2][i]==s[0][i])||(s[2][i]=='T'))&&((s[3][i]==s[0][i])||(s[3][i]=='T'))) nr=4;

        }
        if (nr==4)
        {
            f=1;
            if (s[0][i]!='T') g<<"Case #"<<j<<": "<<s[0][i]<<" won"<<'\n';
            else g<<"Case #"<<j<<": "<<s[1][i]<<" won"<<'\n';
        }
    }
    }
    if (f==0)
    {
        if ((s[0][0]=='T')&&(s[1][1]!='.'))
        {
            if ((s[1][1]==s[2][2])&&(s[1][1]==s[3][3])) nr=4;
        }
        else
        if (s[0][0]!='.')
        {
         if (((s[1][1]==s[0][0])||(s[1][1]=='T'))&& ((s[2][2]==s[0][0])||(s[2][2]=='T'))&&((s[3][3]==s[0][0])||(s[3][3]=='T'))) nr=4;

        }
        if (nr==4)
        {
            f=1;
            if (s[0][0]!='T') g<<"Case #"<<j<<": "<<s[0][0]<<" won"<<'\n';
            else g<<"Case #"<<j<<": "<<s[1][1]<<" won"<<'\n';
        }
    }
    if(f==0)
    {
        if ((s[0][3]=='T')&&(s[1][2]!='.'))
        {
            if ((s[1][2]==s[2][1])&&(s[1][2]==s[3][0])) nr=4;
        }
        else
        if (s[0][3]!='.')
        {
         if (((s[1][2]==s[0][3])||(s[1][2]=='T'))&& ((s[2][1]==s[0][3])||(s[2][1]=='T'))&&((s[3][0]==s[0][3])||(s[3][0]=='T'))) nr=4;

        }
        if (nr==4)
        {
            f=1;
            if (s[0][3]!='T') g<<"Case #"<<j<<": "<<s[0][3]<<" won"<<'\n';
            else g<<"Case #"<<j<<": "<<s[1][2]<<" won"<<'\n';
    }

}
if (f==0)
{
    if (e==1) g<<"Case #"<<j<<": "<<"Game has not completed"<<'\n';
    else g<<"Case #"<<j<<": "<<"Draw"<<'\n';
}
}
int main()
{
    ci>>n;
    for(j=1;j<=n;j++)
    {
        back();

    }
    return 0;
}
