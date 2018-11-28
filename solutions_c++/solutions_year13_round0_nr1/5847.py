#include <iostream>
#include <fstream>

using namespace std;

unsigned char ch, line1[5][5];
int judge();
int main()
{
    ifstream in("A-large.in");


    if(!in)
    {
        cout<<"can't open in file."<<endl;
    }
    ofstream out("A-large.out");
    if(!out)
    {
        cout<<"can't open out file."<<endl;
    }

    int T;
    string result[5]={"", "X won", "O won", "Draw", "Game has not completed"};
    int i, j, count=1;

    in>>T;
    for(count=1; count<=T; count++)
    {
        for(j=1; j<=4; j++)
        {
            for(i=1; i<=4; i++)
            {
                in>>ch;
                switch(ch)
                {
                    case 'X':
                        line1[j][i]=1;
                        break;
                    case 'O':
                        line1[j][i]=2;
                        break;
                    case '.':
                        line1[j][i]=4;
                        break;
                    case 'T':
                        line1[j][i]=255;   //注意此处不是256，而是255！！！
                        break;
                    default:
                        break;
                }
            }
        }

        out<<"Case #"<<count<<": "<<result[judge()]<<endl;
    }

    return 0;
}

int judge()
{
    int i, j;
    unsigned char a;
/*
    for(int c=1; c<=4; c++)
    {
        for(int b=1; b<=4; b++)
        {
            switch(line1[c][b])
            {
                case 1:
                    cout<<'X';
                    break;
                case 2:
                    cout<<'O';
                    break;
                case 4:
                    cout<<'.';
                    break;
                default:
                    cout<<'T';
                    break;
            }

        }
        cout<<endl;
    }
    */

    for(i=1; i<=4; i++)
    {
        a=line1[i][1]&line1[i][2]&line1[i][3]&line1[i][4];
        //cout<<(int)(line1[i][4])<<endl;
        if(a!=0)
        {
            switch(a)
            {
                case 1:
                    return 1;
                case 2:
                    return 2;
                default:
                    break;
            }
        }
        a=line1[1][i]&line1[2][i]&line1[3][i]&line1[4][i];
        if(a!=0)
        {
            switch(a)
            {
                case 1:
                    return 1;
                case 2:
                    return 2;
                default:
                    break;
            }
        }
    }
    a=line1[1][1]&line1[2][2]&line1[3][3]&line1[4][4];
    if(a!=0)
    {
        switch(a)
        {
            case 1:
                return 1;
            case 2:
                return 2;
            default:
                    break;
        }
    }
    a=line1[1][4]&line1[2][3]&line1[3][2]&line1[4][1];
    if(a!=0)
    {
        switch(a)
        {
            case 1:
                return 1;
            case 2:
                return 2;
            default:
                    break;
        }
    }
    for(i=1; i<=4; i++)
    {
        for(j=1; j<=4; j++)
        {
            if(line1[i][j]==4)
            {
                return 4;
            }
        }
    }
    return 3;
}
