#include<iostream>
#include<fstream>
using namespace std;

int match(char mat[4][4])
{
    int flag=5;
    string chkstrng;
    chkstrng=mat[0][0];
    chkstrng+=mat[1][1];
    chkstrng+=mat[2][2];
    chkstrng+=mat[3][3];
    if (chkstrng=="XXXX" || chkstrng=="TXXX" || chkstrng=="XTXX" || chkstrng=="XXTX" || chkstrng=="XXXT")
        flag=1;               //X wins
    else if (chkstrng=="OOOO" || chkstrng=="TOOO" || chkstrng=="OTOO" || chkstrng=="OOTO" || chkstrng=="OOOT")
        flag=2;               //O wins

    if (flag==5)
    {
        chkstrng=mat[3][0];
        chkstrng+=mat[2][1];
        chkstrng+=mat[1][2];
        chkstrng+=mat[0][3];
        if (chkstrng=="XXXX" || chkstrng=="TXXX" || chkstrng=="XTXX" || chkstrng=="XXTX" || chkstrng=="XXXT")
            flag=1;
        else if (chkstrng=="OOOO" || chkstrng=="TOOO" || chkstrng=="OTOO" || chkstrng=="OOTO" || chkstrng=="OOOT")
            flag=2;
    }

    if (flag==5)
    {
        for (int i=0; i<4; i++)
        {
            chkstrng=mat[i][0];
            chkstrng+=mat[i][1];
            chkstrng+=mat[i][2];
            chkstrng+=mat[i][3];
            if (chkstrng=="XXXX" || chkstrng=="TXXX" || chkstrng=="XTXX" || chkstrng=="XXTX" || chkstrng=="XXXT")
                flag=1;
            else if (chkstrng=="OOOO" || chkstrng=="TOOO" || chkstrng=="OTOO" || chkstrng=="OOTO" || chkstrng=="OOOT")
                flag=2;

            chkstrng=mat[0][i];
            chkstrng+=mat[1][i];
            chkstrng+=mat[2][i];
            chkstrng+=mat[3][i];
            if (chkstrng=="XXXX" || chkstrng=="TXXX" || chkstrng=="XTXX" || chkstrng=="XXTX" || chkstrng=="XXXT")
                flag=1;
            else if (chkstrng=="OOOO" || chkstrng=="TOOO" || chkstrng=="OTOO" || chkstrng=="OOTO" || chkstrng=="OOOT")
                flag=2;
        }
    }

    if (flag==5)
    {
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                if (mat[i][j]=='.')
                    flag=0;           //incomplete
            }
        }
    }

    if (flag==5)
        flag=3;                   //draw
    return flag;
}

int main()
{
    fstream f1, f2;
    f1.open("A-large.in", ios::in);
    f2.open("output.txt", ios::out | ios::binary);
    int num;
    f1>>num;
    f1.get();
    char mat[4][4];
    for (int x=0; x<num; x++)
    {
        string prntstrng = "Case #";
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                mat[i][j] = f1.get();
            }
            f1.get();
        }
        f1.get();
        int result = 0, w, y, z;
        result = match(mat);
        if (x<9)
            prntstrng+=(x+49);
        else if (x<99)
        {
            z = x+1;
            y = z%10;
            z = z/10;
            prntstrng+=(z+48);
            prntstrng+=(y+48);
        }
        else if(x<999)
        {
            z = x+1;
            w = z%10;
            z = z/10;
            y = z%10;
            z = z/10;
            prntstrng+=(z+48);
            prntstrng+=(y+48);
            prntstrng+=(w+48);
        }
        else
        {
            prntstrng+="1000";
        }
        if (result==0)
            prntstrng += ": Game has not completed";
        else if (result==1)
            prntstrng += ": X won";
        else if (result==2)
            prntstrng += ": O won";
        else
            prntstrng += ": Draw";
        f2<<prntstrng;
        f2<<endl;
    }
    f1.close();
    f2.close();
    return 0;
}
