#include <iostream>
#include <fstream>
#include <string>


using namespace std ;

int main()
{

    //Area for holding global variables
    int testCases ;
    int runs = 0 ;
    string trash ;

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
    getline(inputFile , trash) ;


    while (runs < testCases)
    {
        string currentCase ;
        string translated ;
        int i = 0 ;

        getline(inputFile , currentCase) ;

        while(currentCase[i])
        {
            if (currentCase[i] == 'A' || currentCase[i] == 'a')
            {
                translated += "y" ;
            }

            else if (currentCase[i] == 'B' || currentCase[i] == 'b')
            {
                translated += "h" ;
            }

            else if (currentCase[i] == 'C' || currentCase[i] == 'c')
            {
                translated += "e" ;
            }

            else if (currentCase[i] == 'D' || currentCase[i] == 'd')
            {
                translated += "s" ;
            }

            else if (currentCase[i] == 'E' || currentCase[i] == 'e')
            {
                translated += "o" ;
            }

            else if (currentCase[i] == 'F' || currentCase[i] == 'f')
            {
                translated += "c" ;
            }

            else if (currentCase[i] == 'G' || currentCase[i] == 'g')
            {
                translated += "v" ;
            }

            else if (currentCase[i] == 'H' || currentCase[i] == 'h')
            {
                translated += "x" ;
            }

            else if (currentCase[i] == 'I' || currentCase[i] == 'i')
            {
                translated += "d" ;
            }

            else if (currentCase[i] == 'J' || currentCase[i] == 'j')
            {
                translated += "u" ;
            }

            else if (currentCase[i] == 'K' || currentCase[i] == 'k')
            {
                translated += "i" ;
            }

            else if (currentCase[i] == 'L' || currentCase[i] == 'l')
            {
                translated += "g" ;
            }

            else if (currentCase[i] == 'M' || currentCase[i] == 'm')
            {
                translated += "l" ;
            }

            else if (currentCase[i] == 'N' || currentCase[i] == 'n')
            {
                translated += "b" ;
            }

            else if (currentCase[i] == 'O' || currentCase[i] == 'o')
            {
                translated += "k" ;
            }

            else if (currentCase[i] == 'P' || currentCase[i] == 'p')
            {
                translated += "r" ;
            }

            else if (currentCase[i] == 'Q' || currentCase[i] == 'q')
            {
                translated += "z" ;
            }

            else if (currentCase[i] == 'R' || currentCase[i] == 'r')
            {
                translated += "t" ;
            }

            else if (currentCase[i] == 'S' || currentCase[i] == 's')
            {
                translated += "n" ;
            }

            else if (currentCase[i] == 'T' || currentCase[i] == 't')
            {
                translated += "w" ;
            }

            else if (currentCase[i] == 'U' || currentCase[i] == 'u')
            {
                translated += "j" ;
            }

            else if (currentCase[i] == 'V' || currentCase[i] == 'v')
            {
                translated += "p" ;
            }

            else if (currentCase[i] == 'W' || currentCase[i] == 'w')
            {
                translated += "f" ;
            }

            else if (currentCase[i] == 'X' || currentCase[i] == 'x')
            {
                translated += "m" ;
            }

            else if (currentCase[i] == 'Y' || currentCase[i] == 'y')
            {
                translated += "a" ;
            }

            else if (currentCase[i] == 'Z' || currentCase[i] == 'z')
            {
                translated += "q" ;
            }

            else
            {
                translated += " " ;
            }

            i++ ;
        }

        outputFile << "Case #" << (runs + 1) << ": " << translated << endl ;

        runs ++ ;


    }

    inputFile.close() ;
    outputFile.close() ;
    return 0 ;
}
