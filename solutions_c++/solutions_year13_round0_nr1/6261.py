#include <iostream>
#include <fstream>
#include <string>


using namespace std ;

int resultCheck (string in[4][4]) ;
bool xWin (string in[4][4], int iT, int jT, bool x) ;
bool oWin (string in[4][4], int iT, int jT, bool x) ;
bool draw (string in[4][4]) ;

int main()
{

    //Area for holding global variables
    int testCases ;
    int runs = 0 ;

    //Code used to input the file for testing
    ifstream inputFile ;
    string filename ;

    cout << "What is the name of the inputfile?: " ;
    getline(cin,filename) ;
    cout << endl ;
    inputFile.open(filename.c_str()) ;

    //Code used to write out the correpsonding file
    ofstream outputFile ;

    cout << "What would you like to name the output file?: " ;
    getline(cin,filename) ;
    cout << endl ;
    outputFile.open(filename.c_str()) ;

    inputFile >> testCases ;

    while (runs < testCases)
    {
        string b [4][4] ;

        for (int i = 0 ; i < 4 ; i++)
        {
            string line ;
            inputFile >> line ;
            cout << line << endl ;
            for (int j = 0 ; j < 4 ; j++)
            {
                b [i][j] = line[j] ;
            }
        }
        int result = resultCheck(b) ;
        string r ;

        if (result == 0)
        {
            r = "X won" ;
        }

        else if (result == 1)
        {
            r = "O won" ;
        }

        else if (result == 2)
        {
            r = "Draw" ;
        }

        else
        {
            r = "Game has not completed" ;
        }


        outputFile << "Case #" << (runs + 1) << ": " << r <<endl ;
        cout << endl ;


        runs ++ ;
    }

    inputFile.close() ;
    outputFile.close() ;
    return 0 ;
}

int resultCheck (string in [4][4])
{
    int iT ;
    int jT ;
    bool x = false ;

    for (int i = 0 ; i < 4 ; i++)
    {
        for (int j = 0 ; j < 4 ; j++)
        {
            if (in[i][j] == "T")
            {

                 iT = i ;
                 jT = j ;
                 x = true ;
            }
        }
    }

    if (xWin(in, iT, jT, x))
    {
        return 0 ;
    }
    else if (oWin(in, iT, jT, x))
    {
        return 1 ;
    }
    else if (draw(in))
    {
        return 2 ;
    }
    else
    {
        return 3 ;
    }
}

bool xWin (string in [4][4], int iT, int jT, bool x)
{

    if (x)
    {
        in [iT] [jT] = "X" ;
    }

    if (in[0][0] == "X" && in[0][1] == "X" && in[0][2] == "X" && in[0][3] == "X" )
    {
        return true ;
    }
    else if (in[1][0] == "X" && in[1][1] == "X" && in[1][2] == "X" && in[1][3] == "X" )
    {
        return true ;
    }
    else if (in[2][0] == "X" && in[2][1] == "X" && in[2][2] == "X" && in[2][3] == "X" )
    {
        return true ;
    }
    else if (in[3][0] == "X" && in[3][1] == "X" && in[3][2] == "X" && in[3][3] == "X" )
    {
        return true ;
    }
    else if (in[0][0] == "X" && in[1][0] == "X" && in[2][0] == "X" && in[3][0] == "X" )
    {
        return true ;
    }
    else if (in[0][1] == "X" && in[1][1] == "X" && in[2][1] == "X" && in[3][1] == "X" )
    {
        return true ;
    }
    else if (in[0][2] == "X" && in[1][2] == "X" && in[2][2] == "X" && in[3][2] == "X" )
    {
        return true ;
    }
    else if (in[0][3] == "X" && in[1][3] == "X" && in[2][3] == "X" && in[3][3] == "X" )
    {
        return true ;
    }
    else if (in[0][0] == "X" && in[1][1] == "X" && in[2][2] == "X" && in[3][3] == "X" )
    {
        return true ;
    }
    else if (in[3][0] == "X" && in[2][1] == "X" && in[1][2] == "X" && in[0][3] == "X" )
    {
        return true ;
    }
    else
    {
        return false ;
    }

}

bool oWin (string in [4][4], int iT, int jT, bool x)
{
    if (x)
    {
        in [iT] [jT] = "O" ;
    }

    if (in[0][0] == "O" && in[0][1] == "O" && in[0][2] == "O" && in[0][3] == "O" )
    {
        return true ;
    }
    else if (in[1][0] == "O" && in[1][1] == "O" && in[1][2] == "O" && in[1][3] == "O" )
    {
        return true ;
    }
    else if (in[2][0] == "O" && in[2][1] == "O" && in[2][2] == "O" && in[2][3] == "O" )
    {
        return true ;
    }
    else if (in[3][0] == "O" && in[3][1] == "O" && in[3][2] == "O" && in[3][3] == "O" )
    {
        return true ;
    }
    else if (in[0][0] == "O" && in[1][0] == "O" && in[2][0] == "O" && in[3][0] == "O" )
    {
        return true ;
    }
    else if (in[0][1] == "O" && in[1][1] == "O" && in[2][1] == "O" && in[3][1] == "O" )
    {
        return true ;
    }
    else if (in[0][2] == "O" && in[1][2] == "O" && in[2][2] == "O" && in[3][2] == "O" )
    {
        return true ;
    }
    else if (in[0][3] == "O" && in[1][3] == "O" && in[2][3] == "O" && in[3][3] == "O" )
    {
        return true ;
    }
    else if (in[0][0] == "O" && in[1][1] == "O" && in[2][2] == "O" && in[3][3] == "O" )
    {
        return true ;
    }
    else if (in[3][0] == "O" && in[2][1] == "O" && in[1][2] == "O" && in[0][3] == "O" )
    {
        return true ;
    }
    else
    {
        return false ;
    }

}

bool draw (string in[4][4])
{
    for (int i = 0 ; i < 4 ; i++)
    {
        for (int j = 0 ; j < 4 ; j++)
        {
            if (in[i][j] == ".")
            {
                return false ;
            }
        }
    }

    return true ;
}
