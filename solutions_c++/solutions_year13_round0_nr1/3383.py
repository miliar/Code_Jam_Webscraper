#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
char s[4][4];

bool checkRow(int i,int j,char rch)
{
    char ch=s[i][j];

    if(j>=3)
    {
        if(ch==rch || ch=='T')
            return true;
        else
            return false;
    }

    if(ch==rch || ch=='T')
        return checkRow(i,j+1,rch);
    else
        return false;
}

bool checkCol(int i,int j,char rch)
{
    char ch=s[i][j];

    if(i>=3)
    {
        if(ch==rch || ch=='T')
            return true;
        else
            return false;
    }

    if(ch==rch || ch=='T')
        return checkCol(i+1,j,rch);
    else
        return false;
}

bool checkDiag1(int i,int j,char rch)
{
    char ch=s[i][j];

    if(j==3 && i==3)
    {
        if(ch==rch || ch=='T')
            return true;
        else
            return false;
    }

    if(ch==rch || ch=='T')
        return checkDiag1(i+1,j+1,rch);
    else
        return false;
}

bool checkDiag2(int i,int j,char rch)
{
    char ch=s[i][j];

    if(i==3 && j==0)
    {
        if(ch==rch || ch=='T')
            return true;
        else
            return false;
    }

    if(ch==rch || ch=='T')
        return checkDiag2(i+1,j-1,rch);
    else
        return false;
}

int main()
{
    ifstream r;
    ofstream w;
    r.open("A-large.in");
    w.open("output-large.txt");

    int t,i,j,cno=0;
    bool incomp,flag;
    char rch,wonch;

    r>>t;
    while(t--)
    {
        memset(s,'.',sizeof(s));
        incomp=false;
        flag=false;
        ++cno;

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                r>>s[i][j];
                if(s[i][j]=='.')
                    incomp=true;
            }
        }

        for(i=0;i<4;i++)
        {
            rch=s[i][0];
            if(rch=='T')
                rch=s[i][1];
            if(rch=='.')
                continue;

            if(checkRow(i,0,rch))
            {
                wonch=rch;
                flag=true;
                break;
            }
        }

        if(!flag)
        {
        for(j=0;j<4;j++)
        {
            rch=s[0][j];
            if(rch=='T')
                rch=s[1][j];
            if(rch=='.')
                continue;

            if(checkCol(0,j,rch))
            {
                wonch=rch;
                flag=true;
                break;
            }
        }
        }

        if(!flag)
        {
                rch=s[0][0];
                if(rch=='T')
                    rch=s[1][1];
                if(rch=='.')
                    goto move1;

                if(checkDiag1(0,0,rch))
                {
                    wonch=rch;
                    flag=true;
                }
        }

        move1:
        if(!flag)
        {
                rch=s[0][3];
                if(rch=='T')
                    rch=s[1][2];
                if(rch=='.')
                    goto move2;

                if(checkDiag2(0,3,rch))
                {
                    wonch=rch;
                    flag=true;
                }
        }

        move2:
        if(flag)
            w<<"Case #"<<cno<<": "<<wonch<<" won"<<endl;
        else if(incomp)
            w<<"Case #"<<cno<<": "<<"Game has not completed"<<endl;
        else
            w<<"Case #"<<cno<<": "<<"Draw"<<endl;
    }
    return 0;
}
