#include <cstdlib>
#include <fstream>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
    ofstream fout("trail1.out");
    ifstream fin("A-small-attempt0.in");
    int i,j,T,t;
    vector <string> results;
    char game[4][4],gameX[4][4],gameO[4][4];
    string s;
    fin>>T;
    for(t=0;t<T;t++)
    {
        if(t!=0){getline(fin,s);}
        fin>>s;
        game[0][0]=s[0];
        game[0][1]=s[1];
        game[0][2]=s[2];
        game[0][3]=s[3];
        fin>>s;
        game[1][0]=s[0];
        game[1][1]=s[1];
        game[1][2]=s[2];
        game[1][3]=s[3];
        fin>>s;
        game[2][0]=s[0];
        game[2][1]=s[1];
        game[2][2]=s[2];
        game[2][3]=s[3];
        fin>>s;
        game[3][0]=s[0];
        game[3][1]=s[1];
        game[3][2]=s[2];
        game[3][3]=s[3];
        
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                gameX[i][j]=game[i][j];
                if(gameX[i][j]=='T'){gameX[i][j]='X';}
                gameO[i][j]=game[i][j];
                if(gameO[i][j]=='T'){gameO[i][j]='O';}
            }
        }
        //check for win X
        for(i=0;i<4;i++)
        {
            if(gameX[i][0]=='X' && gameX[i][0]==game[i][1] && gameX[i][0]==gameX[i][2] && gameX[i][0]==gameX[i][3])
            {
               results.push_back("X won");
               break;
            }
        }
        if(i<4){continue;}
        
        for(i=0;i<4;i++)
        {
            if(gameX[0][i]=='X' && gameX[0][i]==game[1][i] && gameX[0][i]==gameX[2][i] && gameX[0][i]==gameX[3][i])
            {
               results.push_back("X won");
               break;
            }
        }
        if(i<4){continue;}
        
        if(gameX[0][0]=='X' && gameX[1][1]=='X' && gameX[2][2]=='X' && gameX[3][3]=='X')
        {
           results.push_back("X won");
           continue;
        }
        
        if(gameX[0][3]=='X' && gameX[1][2]=='X' && gameX[2][1]=='X' && gameX[3][0]=='X')
        {
           results.push_back("X won");
           continue;
        }
        
        //check for win O
        for(i=0;i<4;i++)
        {
            if(gameO[i][0]=='O' && gameO[i][0]==game[i][1] && gameO[i][0]==gameO[i][2] && gameO[i][0]==gameO[i][3])
            {
               results.push_back("O won");
               break;
            }
        }
        if(i<4){continue;}
        
        for(i=0;i<4;i++)
        {
            if(gameO[0][i]=='O' && gameO[0][i]==game[1][i] && gameO[0][i]==gameO[2][i] && gameO[0][i]==gameO[3][i])
            {
               results.push_back("O won");
               break;
            }
        }
        if(i<4){continue;}
        
        if(gameO[0][0]=='O' && gameO[1][1]=='O' && gameO[2][2]=='O' && gameO[3][3]=='O')
        {
           results.push_back("O won");
           continue;
        }
        
        if(gameO[0][3]=='O' && gameO[1][2]=='O' && gameO[2][1]=='O' && gameO[3][0]=='O')
        {
           results.push_back("O won");
           continue;
        }
        
        //check for finish or not
        
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(game[i][j]=='.')
                {
                   results.push_back("Game has not completed");
                   break;
                }
            }
            if(j<4){break;}
        }
        if(i<4){continue;}
        results.push_back("Draw");
    }
    
    for(t=0;t<T;t++)
    {
        fout<<"Case #"<<t+1<<": "<<results[t]<<endl;
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
