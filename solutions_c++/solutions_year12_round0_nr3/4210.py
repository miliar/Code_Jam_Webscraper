#include <iostream>
#include <fstream>
#include <string>
#include <sstream>



using namespace std ;

int recycledCheck(string, int, int) ;
bool uniqueCheck (string) ;

int main()
{

    //Area for holding global variables
    int testCases ;
    int runs = 0 ;
    int recycled = 0 ;

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
        int low ;
        int high ;

        inputFile >> low ;
        inputFile >> high ;

        recycled = 0 ;

        for (int i = low ; i <= high ; i++)
        {
            string currNumber ;
            stringstream out ;

            out << i ;
            currNumber = out.str() ;

            bool unique ;

            unique = uniqueCheck(currNumber) ;

            if (unique)
            {
                int result ;


                result = recycledCheck(currNumber, low, high) ;

                if (result != 0)
                {
                    recycled += result ;
                }

            }
        }

        outputFile << "Case #" << (runs + 1) << ": " << (recycled / 2) << endl ;

        runs ++ ;

    }



    inputFile.close() ;
    outputFile.close() ;
    return 0 ;
}

int recycledCheck(string num, int low, int high)
{
    int length = num.size() ;
    int recycled = 0 ;

    for (int i = 0 ; i < (length - 1) ; i++)
    {
        int j = 0 ;
        int newInt ;
        string leadString ;
        string tailString ;
        string newString ;

        while (j >= 0 && j <= i)
        {
            leadString += num[j] ;
            j++ ;
        }

        while (j > i && j < length)
        {
            tailString += num[j] ;
            j++ ;
        }

        newString = tailString + leadString ;

        int rightCheck = (newString.size() - 1) ;

        istringstream (newString) >> newInt ;

        if ((newString[0] != '0') && (newInt >= low) && (newInt <= high))
        {
            recycled ++ ;
            cout << newInt << endl ;
        }
    }

    return recycled ;
}

bool uniqueCheck(string num)
{
    int length = num.size() ;
    int iter = 1 ;
    int runs = 0 ;

    bool result = false ;

    for (int i = 0 ; i < 1 ; i++)
    {
        for (int j = 0 ; j < length ; j++)
        {
            if (num[i] != num[j])
            {
                result = true ;
            }
        }
    }

    return result ;
}
