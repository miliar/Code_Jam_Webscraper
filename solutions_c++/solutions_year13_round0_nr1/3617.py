#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin;
    string line;
    char testSize[2000];
    fin.open("A-large.in");
    int T;
    fin>>T;
    //getchar();
    //getline(fin,line);
    string result[T];
    char board[4][4];
    int i;
    for(i=0; !fin.eof(), i<T; i++)
    {
        bool anwered = false;
        for(int j=0; j<4; j++)
        {
            fin>>line;
            for( int k=0; k<4; k++)
            {
                board[j][k] = line[k];
            }
        }
        //getchar();
        //getline(fin,line);
        char first = board[0][0];
        if(board[0][0]=='T')
            first = board[1][1];
        if( (board[0][0]=='T' || board[0][0]==first)
            && (board[1][1]=='T' || board[1][1]==first)
           && (board[2][2]=='T' || board[2][2]==first)
           && (board[3][3]=='T' || board[3][3]==first) )
        {
            if(first!='.')
            {
                char tmp[2];
                tmp[0] = first;
                tmp[1] = '\0';
                string str(tmp);
                result[i] = str + " won";
                anwered = true;
                continue;
            }
        }
        first = board[0][3];
        if(board[0][3]=='T')
            first = board[1][2];
        if( (board[0][3]=='T' || board[0][3]==first)
            && (board[1][2]=='T' || board[1][2]==first)
           && (board[2][1]=='T' || board[2][1]==first)
           && (board[3][0]=='T' || board[3][0]==first) )
        {
            if(first!='.')
            {
                char tmp[2];
                tmp[0] = first;
                tmp[1] = '\0';
                string str(tmp);
                result[i] = str + " won";
                anwered = true;
                continue;
            }
        }
        for(int j=0; j<4; j++)
        {
            char first = board[j][0];
            int k=0;
            for( k=1; k<4; k++)
            {
                if(first == 'T')
                    first = board[j][k];
                else if(board[j][k]!='T' && board[j][k]!=first)
                    break;
            }
            if(k==4 && first!='.')
            {
                char tmp[2];
                tmp[0] = first;
                tmp[1] = '\0';
                string str = tmp;
                result[i] = str + " won";
                anwered = true;
                break;
            }
        }
        if(anwered)
            continue;
        for(int j=0; j<4; j++)
        {
            char first = board[0][j];
            int k=0;
            for( k=1; k<4; k++)
            {
                if(first == 'T')
                    first = board[k][j];
                else if(board[k][j]!='T' && board[k][j]!=first)
                    break;
            }
            if(k==4 && first!='.')
            {
                char tmp[2];
                tmp[0] = first;
                tmp[1] = '\0';
                string str = tmp;
                result[i] = str + " won";
                anwered = true;
                break;
            }
        }
        if(anwered)
            continue;
        for(int j=0; !anwered,j<4; j++)
            for( int k=0; !anwered, k<4; k++)
                {
                    if(board[j][k]=='.')
                    {
                        result[i] = "Game has not completed";
                        anwered = true;
                    }
                }
        if(!anwered)
            result[i] = "Draw";
    }
    ofstream out("A-large.out");
    for(int i=0; i<T; i++)
    {
        out<<"Case #"<<i+1<<": "<<result[i]<<endl;
    }
        //cout<<"Case #"<<i+1<<": "<<result[i]<<endl;

    fin.close();
    out.close();
    return 0;
}
