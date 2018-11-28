#include<fstream>
#include<iostream>
#include<string>
#include<vector>

using namespace std;

class AlienLanguage
{
    int length;
    int noWords;
    int noTestCases;
    int matchedWords;
    string words[5000];
    string tokenString;


    public:

    void countMatchedWords()
    {
        int i, j;
        int position, indexOpen, indexClose;
        string tempString, token = tokenString;
        matchedWords = 0;
        for( i = 0; i < noWords; ++i )
        {
            tokenString = token;
            for( j=0; j < length; ++j )
            {
                if( tokenString[0] == '(' )
                {
                    indexOpen = tokenString.find_first_of("(");
                    indexClose = tokenString.find_first_of(")");
                    tempString = tokenString.substr( indexOpen + 1, indexClose - indexOpen - 1 );
                    tokenString = tokenString.substr( indexClose + 1, tokenString.length() - indexClose );
                }
                else
                {
                    tempString = tokenString.substr( 0, 1 );
                    tokenString = tokenString.substr( 1, tokenString.length() - 1 );
                }
                position = tempString.find_first_of( words[i].at(j) );
                if( position ==  -1 )
                    break;
            }
            if( j == length )
                matchedWords += 1;
        }
    }
    AlienLanguage()
    {
        int i, j;
        ifstream inputFile;
        ofstream outputFile;
        string tempString = "";
        inputFile.open ( "A-large.in" );
        outputFile.open ( "A-large.out" );
        inputFile>>length>>noWords>>noTestCases;
        //cout<<length<<" "<<noWords<<" "<<noTestCases<<endl;
        for( j = 0; j < noWords; ++j )
        {
            inputFile>>words[j];
        //    cout<<words[j]<<endl;
        }
        for( i = 0; i < noTestCases; ++i )
        {
            inputFile>>tokenString;
            //cout<<tokenString<<endl;
            countMatchedWords();
            cout<<"Case #"<<i+1<<": "<<matchedWords<<endl;
            outputFile<<"Case #"<<i+1<<": "<<matchedWords<<endl;
         }
         inputFile.close();
         outputFile.close();
    }
};

int main()
{
    AlienLanguage alienLanguage;
}
