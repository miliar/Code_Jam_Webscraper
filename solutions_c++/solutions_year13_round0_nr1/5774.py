#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#define loop(v) for(int i=0;i<v.size();i++)
#define loopb(v) for(int i=v.size()-1;i>=0;i--)

using namespace std;

bool ifXwin(char board[4][4])
{
    int compteur1=0,compteur2=0,compteur3=0,compteur4=0,compteur5=0,compteur6=0,compteur7=0,compteur8=0,compteur9=0,compteur10=0;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(i==j && (board[i][j]=='X' || board[i][j]=='T'))
               compteur1++;
            if(i==0 && (board[i][j]=='X' || board[i][j]=='T'))
               compteur2++;
            if(i==1 && (board[i][j]=='X' || board[i][j]=='T'))
               compteur3++;
            if(i==2 && (board[i][j]=='X' || board[i][j]=='T'))
               compteur4++;
            if(i==3 && (board[i][j]=='X' || board[i][j]=='T'))
               compteur5++;
            if(j==0 && (board[i][j]=='X' || board[i][j]=='T'))
               compteur6++;
            if(j==1 && (board[i][j]=='X' || board[i][j]=='T'))
               compteur7++;
            if(j==2 && (board[i][j]=='X' || board[i][j]=='T'))
               compteur8++;
            if(j==3 && (board[i][j]=='X' || board[i][j]=='T'))
               compteur9++;
            if(i==3-j && (board[i][j]=='X' || board[i][j]=='T'))
               compteur10++;
        }
    }
    if(compteur10==4||compteur9==4||compteur8==4||compteur7==4||compteur6==4||compteur5==4||compteur4==4||compteur3==4||compteur2==4||compteur1==4)
        return true;
    else
        return false;
}

bool ifOwin(char board[4][4])
{
    int compteur1=0,compteur2=0,compteur3=0,compteur4=0,compteur5=0,compteur6=0,compteur7=0,compteur8=0,compteur9=0,compteur10=0;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(i==j && (board[i][j]=='O' || board[i][j]=='T'))
               compteur1++;
            if(i==0 && (board[i][j]=='O' || board[i][j]=='T'))
               compteur2++;
            if(i==1 && (board[i][j]=='O' || board[i][j]=='T'))
               compteur3++;
            if(i==2 && (board[i][j]=='O' || board[i][j]=='T'))
               compteur4++;
            if(i==3 && (board[i][j]=='O' || board[i][j]=='T'))
               compteur5++;
            if(j==0 && (board[i][j]=='O' || board[i][j]=='T'))
               compteur6++;
            if(j==1 && (board[i][j]=='O' || board[i][j]=='T'))
               compteur7++;
            if(j==2 && (board[i][j]=='O' || board[i][j]=='T'))
               compteur8++;
            if(j==3 && (board[i][j]=='O' || board[i][j]=='T'))
               compteur9++;
            if(i==3-j && (board[i][j]=='O' || board[i][j]=='T'))
               compteur10++;
        }
    }
    if(compteur10==4||compteur9==4||compteur8==4||compteur7==4||compteur6==4||compteur5==4||compteur4==4||compteur3==4||compteur2==4||compteur1==4)
        return true;
    else
        return false;
}

bool ifNotyet(char board[4][4])
{
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(board[i][j]=='.')
                return true;
        }
    }
    return false;
}



int main() {

    int N;
    char board[4][4];
    string line;
    ofstream OUT ("small.out");
    ifstream IN ("small.in");
    IN >> N;
    //OUT << N;
    IN.ignore();
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                board[j][k] = IN.get();
            }
            IN.ignore();
        }
        IN.ignore();
        OUT <<"Case #"<<i+1<<": ";
        if(ifXwin(board))
            OUT <<"X won"<<endl;
        else if(ifOwin(board))
            OUT <<"O won"<<endl;
        else if(ifNotyet(board))
            OUT <<"Game has not completed"<<endl;
        else
            OUT <<"Draw"<<endl;
        /*cout<<endl;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cout <<  board[j][k];
            }
            cout<<endl;
        }*/
    }
    OUT<<endl;
    return 0;
}
