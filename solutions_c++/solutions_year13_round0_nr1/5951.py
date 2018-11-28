#include<iostream>
#include<fstream>
using namespace std;

int check(char m[4][4])
{
    int p=5;
    string a;
    a=m[0][0];
    a+=m[1][1];
    a+=m[2][2];
    a+=m[3][3];
    if (a=="XXXX" || a=="TXXX" || a=="XTXX" || a=="XXTX" || a=="XXXT")
        p=1;               //X wins
    else if (a=="OOOO" || a=="TOOO" || a=="OTOO" || a=="OOTO" || a=="OOOT")
        p=2;               //O wins

    if (p==5)
    {
        a=m[3][0];
        a+=m[2][1];
        a+=m[1][2];
        a+=m[0][3];
        if (a=="XXXX" || a=="TXXX" || a=="XTXX" || a=="XXTX" || a=="XXXT")
            p=1;
        else if (a=="OOOO" || a=="TOOO" || a=="OTOO" || a=="OOTO" || a=="OOOT")
            p=2;
    }

    if (p==5)
    {
        for (int i=0; i<4; i++)
        {
            a=m[i][0];
            a+=m[i][1];
            a+=m[i][2];
            a+=m[i][3];
            if (a=="XXXX" || a=="TXXX" || a=="XTXX" || a=="XXTX" || a=="XXXT")
                p=1;
            else if (a=="OOOO" || a=="TOOO" || a=="OTOO" || a=="OOTO" || a=="OOOT")
                p=2;

            a=m[0][i];
            a+=m[1][i];
            a+=m[2][i];
            a+=m[3][i];
            if (a=="XXXX" || a=="TXXX" || a=="XTXX" || a=="XXTX" || a=="XXXT")
                p=1;
            else if (a=="OOOO" || a=="TOOO" || a=="OTOO" || a=="OOTO" || a=="OOOT")
                p=2;
        }
    }

    if (p==5)
    {
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                if (m[i][j]=='.')
                    p=0;           //incomplete
            }
        }
    }

    if (p==5)
        p=3;                   //draw
    return p;
}

int main()
{
    fstream f1, f2;
    f1.open("A-large.in", ios::in);
    f2.open("output.txt", ios::out | ios::binary);
    int iter;
    f1>>iter;
    f1.get();
    char m[4][4];
    for (int x=0; x<iter; x++)
    {
        string s = "Case #";
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                m[i][j] = f1.get();
            }
            f1.get();
        }
        f1.get();
        int res = 0;
        res = check(m);
//        cout<<res<<endl;
        int z=x, c,d;
        if(z+1<=9)
        s+=(x+49);
        else if(z+1<=99)
        {
            z++;
            c=z%10;
            z=z/10;
            s+=(z+48);
            s+=(c+48);
            //cout<<s;
        }
        else if(z+1<=999)
        {
            z++;
            c=z%10;
            z=z/10;
            d=z%10;
            z=z/10;
            s+=(z+48);
            s+=(d+48);
            s+=(c+48);
        }
        else
        {
            s+="1000";
        }
        if (res==0)
        s += ": Game has not completed";
        else if (res==1)
            s += ": X won";
        else if (res==2)
            s += ": O won";
        else
            s += ": Draw";
        f2<<s;
        f2<<endl;
    }
    f1.close();
    f2.close();
    return 0;
}
