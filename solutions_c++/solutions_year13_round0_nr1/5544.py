#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

char calc_sit(string s)
{
    int i,j;
    char c;
    for (i=0;i<4;i++)
    {
        c=s[i*4];
        if (c!='.')
        {
        for (j=1;j<4;j++)
            if (!((s[i*4+j] == c) || (s[i*4+j] == 'T')))
            {
                c='N';
                break;
            }
        if (c!='N')
            return c;
        }
        c=s[i];
        if (c!='.')
        {
        for (j=1;j<4;j++)
            if (!((s[i+j*4] == c) || (s[i+j*4] == 'T')))
            {
                c='N';
                break;
            }
        if (c!='N')
            return c;
        }
    }
    c=s[0];
    if (c!='.')
    {
    for (i=5;i<16;i+=5)
        if (!((s[i] == c) || (s[i] == 'T')))
        {
            c='N';
            break;
        }
    if (c!='N')
        return c;
    }
    c=s[3];
    if (c!='.')
    {
    for (i=6;i<16;i+=3)
        if (!((s[i] == c) || (s[i] == 'T')))
        {
            c='N';
            break;
        }
    if (c!='N')
        return c;
    }
    for (i=0;i<16;i++)
        if (s[i]=='.')
            return 'E';
    return 'N';
}

int main()
{
    int n,i,j;
    string s,ts;
    char c;
    cin>>n;
    for (i=0;i<n;i++)
    {
        s="";
        for (j=0;j<4;j++)
        {
            cin>>ts;
            s+=ts;
        }
        c=calc_sit(s);
        if ((c=='X')||(c=='O'))
            cout<<"Case #"<<(i+1)<<": "<<c<<" won"<<endl;
        else if (c=='E')
            cout<<"Case #"<<(i+1)<<": "<<"Game has not completed"<<endl;
        else
            cout<<"Case #"<<(i+1)<<": "<<"Draw"<<endl;
    }
}
