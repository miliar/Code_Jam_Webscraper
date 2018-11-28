#include <iostream>

using namespace std; 


// //////////////////////////////////////////////////
int main(int argc, char** argv)
{
    int caseNo;
    size_t mat[510][20];
    for(size_t i = 1; i < 510; i++)
        mat[i][0] = 1;
    for(size_t i = 1; i < 20; i++)
        mat[0][i] = 0;

    std::string pattern("welcome to code jam"), currentStr;
    //std::string pattern("TEST"), currentStr;
    cin >> caseNo;
    getline(cin,currentStr); // for blank
    size_t patternLength = pattern.length();
    for(int i = 1; i <= caseNo; i++)
    {
        getline(cin,currentStr);
        size_t currentStrLength = currentStr.length();
        for(size_t j = 1; j <= patternLength; j++)
        {
            for(size_t k = 1; k <= currentStrLength; k++)
            {
                if ( currentStr[k-1] == pattern[j-1] )
                {
                    mat[k][j] = mat[k-1][j] + mat[k][j-1];
                    mat[k][j] = mat[k][j] % 10000;
                }
                else
                    mat[k][j] = mat[k-1][j];
                //printf("%5d ", mat[k][j]);
                
            }
            //cout << endl;
        } // end - for

        printf("Case #%d: %04u\n" , i, mat[currentStrLength][patternLength]);

    }


    return 0;

} // end - main
