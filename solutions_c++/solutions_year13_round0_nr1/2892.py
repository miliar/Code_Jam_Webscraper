#include <iostream>
#include <fstream>
using namespace std;
char Board[4][4];
ifstream input("input.txt");
    ofstream output("output.txt");
bool diagonal1()
{
    int Number_X=0;
    int Number_O=0;
    int Number_T=0;
    for(int i=0;i<4;i++)
    {
        if(Board[i][i]=='O')
            Number_O++;
        if(Board[i][i]=='X')
            Number_X++;
        if(Board[i][i]=='T')
            Number_T++;
    }
    if((Number_O==3 && Number_T==1 ||Number_O==4 && Number_T== 0))
    {
        output<<"O won"<<endl;
        return 1;
    }
    else if((Number_X==3 && Number_T==1) ||(Number_X==4 && Number_T== 0))
    {
        output<<"X won"<<endl;
        return 2;
    }
    else
        return 0;
}
bool diagonal2()
{
    int Number_X=0;
    int Number_O=0;
    int Number_T=0;
    for(int i=0;i<4;i++)
    {
        if(Board[i][4-i-1]=='O')
            Number_O++;
        if(Board[i][4-i-1]=='X')
            Number_X++;
        if(Board[i][4-i-1]=='T')
            Number_T++;
    }
    if((Number_O==3 && Number_T==1 ||Number_O==4 && Number_T== 0))
    {
        output<<"O won"<<endl;
        return 1;
    }
    else if((Number_X==3 && Number_T==1) ||(Number_X==4 && Number_T== 0))
    {
        output<<"X won"<<endl;
        return 2;
    }
    else
        return 0;
}
bool Longeur()
{
    for(int i=0;i<4;i++)
    {
        int Number_X=0;
        int Number_O=0;
        int Number_T=0;
        for(int j=0;j<4;j++)
        {
        if(Board[i][j]=='O')
            Number_O++;
        if(Board[i][j]=='X')
            Number_X++;
        if(Board[i][j]=='T')
            Number_T++;
        }
    if((Number_O==3 && Number_T==1 ||Number_O==4 && Number_T== 0))
    {
        output<<"O won"<<endl;
        return 1;
    }
    else if((Number_X==3 && Number_T==1) ||(Number_X==4 && Number_T== 0))
    {
        output<<"X won"<<endl;
        return 2;
    }
 }
}
bool Largeur()
{
    for(int i=0;i<4;i++)
    {
        int Number_X=0;
        int Number_O=0;
        int Number_T=0;
        for(int j=0;j<4;j++)
        {
        if(Board[j][i]=='O')
            Number_O++;
        if(Board[j][i]=='X')
            Number_X++;
        if(Board[j][i]=='T')
            Number_T++;
        }
    if((Number_O==3 && Number_T==1 ||Number_O==4 && Number_T== 0))
    {
        output<<"O won"<<endl;
        return 1;
    }
    else if((Number_X==3 && Number_T==1) ||(Number_X==4 && Number_T== 0))
    {
        output<<"X won"<<endl;
        return 2;
    }
}
return 0;
}
bool Draw()
{
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(Board[i][j]=='.')
                return 0;
        }
    }
    output<<"Draw"<<endl;
    return 1;
}
void solve()
{
    if(diagonal1() ||diagonal2())
        return;
    else if(Longeur()||Largeur())
        return;
    else if(Draw())
        return;
    else
        output<<"Game has not completed"<<endl;
}
int main()
{

    int Test_Case;
    input>>Test_Case;
    cout<<Test_Case<<endl;
    for(int i=1;i<=Test_Case;i++)
    {
        output<<"Case #"<<i<<": ";
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                input>>Board[j][k];
            }
        }
        solve();
    }
    return 0;
}
