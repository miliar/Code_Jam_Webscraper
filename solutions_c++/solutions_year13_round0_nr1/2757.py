#include <iostream>
#include<fstream>
#include<vector>
using namespace std;

bool FullSet(vector<vector<char> > Board)
{
    for (int i =0; i < 4;i++)
    {
        for (int j =0; j < 4;j++)
        {
            if (Board[i][j] == '.') return false;
        }
    }
    return true;
}
bool AllRowsOrT(vector<vector<char> > Board,char x)
{
    for (int row =0; row < 4; row++)
    {
        int xcount =0;
        int tcount = 0;
        for (int coloumn =0;coloumn < 4; coloumn++)
        {
            if ((Board[row][coloumn]) == x) xcount++;
            if ((Board[row][coloumn]) == 'T') tcount++;
        }

        if (xcount == 4) return true;
        if (xcount ==3 && tcount == 1) return true;

    }
    return false;
}

bool AllColoumnsOrT(vector<vector<char> > Board,char x)
{
    for (int coloumn =0; coloumn < 4; coloumn++)
    {
        int xcount =0;
        int tcount = 0;
        for (int row =0;row < 4; row++)
        {
            if ((Board[row][coloumn]) == x) xcount++;
            if ((Board[row][coloumn]) == 'T') tcount++;
        }

        if (xcount == 4) return true;
        if (xcount ==3 && tcount == 1) return true;

    }
    return false;
}

bool AllDiagonalsOrT(vector<vector<char> > Board, char x )
{

    int xcount =0;
    int tcount =0;
    for(int i = 0 ; i < 4; i++)
    {
        if (Board[i][i] == x) xcount++;
        if (Board[i][i] == 'T') tcount++;
    }
    if (xcount == 4) return true;
    if (xcount ==3 && tcount == 1) return true;



    int xcount2 =0;
    int tcount2 =0;
    for(int i = 0 ; i < 4; i++)
    {
        if (Board[i][3-i] == x) xcount2++;
        if (Board[i][3-i] == 'T') tcount2++;
    }
    if (xcount2 == 4) return true;
    if (xcount2 ==3 && tcount2 == 1) return true;
    return false;
}

bool XWon(vector<vector<char> > &Board)
{
    if (AllRowsOrT(Board,'X') || AllColoumnsOrT(Board,'X') ||  AllDiagonalsOrT(Board,'X') ) return true;
    else return false;
}

bool YWon(vector<vector<char> > &Board)
{
    if (AllRowsOrT(Board,'O') || AllColoumnsOrT(Board,'O') ||  AllDiagonalsOrT(Board,'O') ) return true;
    else return false;
}
int main()
{
    ifstream in("A-large.in");
    ofstream out("output.out");

    int NumberOfTestCases;
    in >> NumberOfTestCases;

    string empty;
    getline(in,empty);

for (int n = 1; n <= NumberOfTestCases;n++)
{
    out << "Case #" << n <<  ": ";

    vector<vector<char> > Board;
    for (int i = 0 ; i < 4; i++)
    {
        vector<char> line;
        for (int j = 0; j < 4;j++)
        {
            char item;
            in >> item;
            line.push_back(item);
        }
        Board.push_back(line);
    }

//    for (int i =0; i < 4; i++)
//    {
//        for (int j =0; j < 4; j++)
//
//        {
//            cout << Board[i][j] << " ";
//        }
//
//        cout << endl;
//    }

        if (XWon(Board))
        {
            out << "X won" ;
            if (n != NumberOfTestCases) out << endl;

        }
        else if (YWon(Board))
        {
            out << "O won" ;
            if (n != NumberOfTestCases) out << endl;


        }
        else if (FullSet(Board))
        {
            out << "Draw" ;
            if (n != NumberOfTestCases) out << endl;

        }
        else
        {
            out << "Game has not completed";
            if (n != NumberOfTestCases) out << endl;
        }

    }




     return 0;
}


