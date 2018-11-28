//
//  tictac.cpp
//  
//
//  Created by Abdallah on 4/12/13.
//
//
#include <fstream>
#include <iostream>

using namespace std;

main()
{
    ifstream fin;
    ofstream fout;
    
    fin.open("data.in.txt");
    fout.open("data.out.txt");

    int T, i,j,k;
    
    char board[4][4];
    fin>>T;
    
    for(i=0;i<T;i++)
    {
        
        //read the board
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                fin>>board[j][k];
            }
        
        bool fX=false, fO=false, fD=false, fincomp=false;
        int countX, countO;
        //test rows
        for(j=0;j<4;j++)
        {
            countX=0; countO=0;
            for(k=0;k<4;k++)
            {
                if(board[j][k]=='X') countX++;
                if(board[j][k]=='O') countO++;
                if(board[j][k]=='.') fincomp=true;
                if(board[j][k]=='T') {countX++;countO++;}
            }
            if(countX==4) fX=true;
            if(countO==4) fO=true;
        }
        
        //test cols
        for(j=0;j<4;j++)
        {
            countX=0; countO=0;
            for(k=0;k<4;k++)
            {
                if(board[k][j]=='X') countX++;
                if(board[k][j]=='O') countO++;
                if(board[k][j]=='.') fincomp=true;
                if(board[k][j]=='T') {countX++;countO++;}
            }
            if(countX==4) fX=true;
            if(countO==4) fO=true;
        }
        
        //test first diag
        countX=0; countO=0;
        for(j=0;j<4;j++)
        {
            if(board[j][j]=='X') countX++;
            if(board[j][j]=='O') countO++;
            if(board[j][j]=='.') fincomp=true;
            if(board[j][j]=='T') {countX++;countO++;}
        }
        if(countX==4) fX=true;
        if(countO==4) fO=true;

        //test second diag
        countX=0; countO=0;
        for(j=0;j<4;j++)
        {
            if(board[j][3-j]=='X') countX++;
            if(board[j][3-j]=='O') countO++;
            if(board[j][3-j]=='.') fincomp=true;
            if(board[j][3-j]=='T') {countX++;countO++;}
        }
        if(countX==4) fX=true;
        if(countO==4) fO=true;
        
        fout<<"Case #"<<i+1<<": ";
        if(fX) fout<<"X won"<<endl;
        else if(fO) fout<<"O won"<<endl;
        else if(fincomp) fout<<"Game has not completed"<<endl;
        else fout<<"Draw"<<endl;
        
    }
    
    fin.close();
    fout.close();

}