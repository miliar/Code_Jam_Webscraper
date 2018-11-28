#include <fstream>
using namespace std;
int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t, i, j, k;
    char mat[4][4], pat;
    cin>>t;
    for(k=0; k<t; ++k)
    {
        pat='Q';
        for(j=0; j<4; ++j)
        {
            for(i=0; i<4; ++i)
            {
                cin>>mat[j][i];
                if(mat[j][i]=='.')
                {
                    pat='D';
                }
            }
        }
        for(i=0; i<4; ++i)
        {
            for(j=0; j<4; ++j)
            {
                if(mat[i][j]!='X' && mat[i][j]!='T')
                {
                    break;
                }
            }
            if(j==4)
            {
                pat='X';
            }
        }
        for(i=0; i<4; ++i)
        {
            for(j=0; j<4; ++j)
            {
                if(mat[j][i]!='X' && mat[j][i]!='T')
                {
                    break;
                }
            }
            if(j==4)
            {
                pat='X';
            }
        }
        for(i=0; i<4; ++i)
        {
            if(mat[i][i]!='X' && mat[i][i]!='T')
            {
                break;
            }
        }
        if(i==4) pat='X';
        for(i=0; i<4; ++i)
        {
            if(mat[i][3-i]!='X' && mat[i][3-i]!='T')
            {
                break;
            }
        }
        if(i==4) pat='X';
        for(i=0; i<4; ++i)
        {
            for(j=0; j<4; ++j)
            {
                if(mat[i][j]!='O' && mat[i][j]!='T')
                {
                    break;
                }
            }
            if(j==4)
            {
                pat='O';
            }
        }
        for(i=0; i<4; ++i)
        {
            for(j=0; j<4; ++j)
            {
                if(mat[j][i]!='O' && mat[j][i]!='T')
                {
                    break;
                }
            }
            if(j==4)
            {
                pat='O';
            }
        }
        for(i=0; i<4; ++i)
        {
            if(mat[i][i]!='O' && mat[i][i]!='T')
            {
                break;
            }
        }
        if(i==4) pat='O';
        for(i=0; i<4; ++i)
        {
            if(mat[i][3-i]!='O' && mat[i][3-i]!='T')
            {
                break;
            }
        }
        if(i==4) pat='O';
        if(pat=='X' || pat=='O') cout<<"Case #"<<k+1<<": "<<pat<<" won\n";
        else
        {
            if(pat=='D')
            {
                cout<<"Case #"<<k+1<<": Game has not completed\n";
            }
            else
                cout<<"Case #"<<k+1<<": Draw\n";
        }
    }
    return 0;
}
