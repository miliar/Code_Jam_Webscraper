#include<iostream>
#include<string>
#include<fstream>

using namespace std;

string dict[5000];
bool fl[5000][15]={false};
int l,d;

void setflag(char ch,int c)
{
    int j=0;
    for(j=0;j<d;j++)
    {
        if(dict[j][c]==ch)
        {
            fl[j][c]=true;
        }
    }
}

int count(string str)
{
    int ctr=0;
    int i,j;
    bool flag=false;
    for(i=0;i<d;i++)
    {
        for(j=0;j<l;j++)
        {
            fl[i][j]=false;
        }
    }
    for(i=0,j=0;i<l;i++,j++)
    {
        if(str[j]=='(')
        {
            j++;
            while(str[j]!=')')
            {
                setflag(str[j],i);
                j++;
            }
        }
        else
        {
            setflag(str[j],i);
        }
    }

    for(i=0;i<d;i++)
    {
        flag=false;
        for(j=0;j<l;j++)
        {
            if(fl[i][j]==false)
            {
                flag=true;
            }
        }
        if(!flag)
        {
            ctr++;
        }
    }
    return ctr;
}

int main()
{
    unsigned long int res;
    string str;
    str.reserve(450);
    int n,i;
    char ch;
    ifstream in ("A-small-attempt1.in",ios::in|ios::binary);
    ofstream out ("output",ios::out);
    in>>l;
    in>>d;
    in>>n;
    in.get(ch);
    for(i=0;i<d;i++)
    {
        getline(in,dict[i]);
    }
    for(i=0;i<n;i++)
    {
        getline(in,str,'\n');
        res = count(str);
        out<<"Case #"<<i+1<<": "<<res<<endl;
    }
}
