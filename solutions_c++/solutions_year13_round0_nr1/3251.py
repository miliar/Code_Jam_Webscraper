#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int i,j,t,p;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>t;
    for(p=1;p<=t;p++)
    {
        int x=0,o=0,d=0;
        char a[4][4];

        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        {fin>>a[i][j];
        if(a[i][j]=='.')
        d++;}

        for(i=0;i<4;i++)//all rows
        {
            int j=0;
            while(j<4 && (a[i][j]=='X' || a[i][j]=='T'))
            j++;
            if(j==4)
            {
                x=1;break;
            }
            j=0;
            while(j<4 && (a[i][j]=='O' || a[i][j]=='T'))
            j++;
            if(j==4)
            {
                o=1;break;
            }

        }
        if(x==1)
        {
            fout<<"Case #"<<p<<": X won\n";
            continue;
        }
        if(o==1)
        {
            fout<<"Case #"<<p<<": O won\n";
            continue;
        }


        for(j=0;j<4;j++)//all cols
        {
            int i=0;
            while(i<4 && (a[i][j]=='X' || a[i][j]=='T'))
            i++;
            if(i==4)
            {
                x=1;break;
            }
            i=0;
            while(i<4 && (a[i][j]=='O' || a[i][j]=='T'))
            i++;
            if(i==4)
            {
                o=1;break;
            }

        }
        if(x==1)
        {
            fout<<"Case #"<<p<<": X won\n";
            continue;
        }
        if(o==1)
        {
            fout<<"Case #"<<p<<": O won\n";
            continue;
        }

        ////////////diagonals 1
        i=j=0;
        while(i<4 && (a[i][j]=='X' || a[i][j]=='T'))
        {
            i++;j++;
        }
        if(i==4)
        {x=1;
            fout<<"Case #"<<p<<": X won\n";
            continue;
        }

        i=j=0;
        while(i<4 && (a[i][j]=='O' || a[i][j]=='T'))
        {
            i++;j++;
        }
        if(i==4)
        {o=1;
            fout<<"Case #"<<p<<": O won\n";
            continue;
        }


        ////////////diagonals 2
        i=3;j=0;
        while(i>=0 && (a[i][j]=='X' || a[i][j]=='T'))
        {
            i--;j++;
        }
        if(i==-1)
        {x=1;
            fout<<"Case #"<<p<<": X won\n";
            continue;
        }

        i=3;j=0;
        while(i>=0 && (a[i][j]=='O' || a[i][j]=='T'))
        {
            i--;j++;
        }
        if(i==-1)
        {o=1;
            fout<<"Case #"<<p<<": O won\n";
            continue;
        }
        if(x==0 && o==0)
        {
            if(d==0)
            fout<<"Case #"<<p<<": Draw\n";
            else
            fout<<"Case #"<<p<<": Game has not completed\n";
        }


    }
    return 0;
}
