#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <stack>
#include <vector>
using namespace std;

int main()
{
    ifstream inputFile;
    ofstream outputFile;

    inputFile.open("A-small-practice.in");
    outputFile.open("A-small-practice.out");

    int N;
    int i,j;
    string inStr;
    int sz=1;
    int ascii;
    char table[26]=
    {
        'y','h','e','s','o',
        'c','v','x','d','u',
        'i','g','l','b','k',
        'r','z','t','n','w',
        'j','p','f','m','a',
        'q'
    };

    string outStr;
    while(inputFile>>N)
    {
        inputFile.ignore();
        for (i=0;i<N;i++)
        {
            getline(inputFile,inStr);
            outStr=inStr;
            sz=inStr.length();
            for (j=0;j<sz;j++)
            {
                if(inStr[j]==' ')
                    continue;
                ascii=inStr[j]-'a';
                outStr[j]=table[ascii];
            }

            outputFile<<"Case #"<<i+1<<": ";
            outputFile<<outStr<<endl;
        }

    }

    system("pause");
    return 0;
}