#include <iostream>
#include <fstream>
#include <string>


using namespace std ;

//function prototype

int withinTwo(int, int, int, int) ;

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
         int googlers ;
         int specialCases ;
         int goal ;
         int scores[googlers] ;
         int bestResult = 0 ;

         inputFile >> googlers ;
         inputFile >> specialCases ;
         inputFile >> goal ;

         for (int i = 0 ; i < googlers ; i++)
         {
             inputFile >> scores[i] ;
         }

         for (int i = 0 ; i < googlers ; i++)
         {
            int average = scores[i] / 3 ;

            if (scores[i] < goal)
            {

            }
             else if (average >= goal)
             {
                 bestResult ++ ;
             }

             else if (average >= (goal - 2))
             {

                 int result = withinTwo(scores[i], average, goal, specialCases) ;

                 if (result == 1)
                 {
                     bestResult ++ ;
                 }

                 else if (result == 2)
                 {
                     bestResult ++ ;
                     specialCases -- ;
                 }

             }
         }

         outputFile << "Case #" << (runs + 1) << ": " << bestResult << endl ;
         runs ++ ;

    }


    inputFile.close() ;
    outputFile.close() ;
    return 0 ;
}

int withinTwo(int num, int average, int goal, int surprises)
{
    if ((goal - average) == 1)
    {
        if (((goal + goal + average) == num) || ((average + average + goal) == num))
        {
            return 1 ;
        }

        else if (((average - 1) + average + goal) == num && (surprises != 0))
        {
            return 2 ;
        }
    }

    else if (((goal - average) == 2))
    {
        if ((average + average + goal == num) && (surprises != 0))
        {
            return 2 ;
        }

        else
        {
            return 3 ;
        }
    }
}
