#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    int n, i, j;
    string str[30];
    char conv[26] = 
        {'y','h','e','s','o','c','v','x','d','u','i','g','l'
        ,'b','k','r','z','t','n','w','j','p','f','m','a','q'};
    ifstream infile("input.txt");
    ofstream outfile("output.txt");
    
    infile >> n;
    getline(infile,str[0]);
    for (i=0;i<n;i++)
    {
        getline(infile,str[i]);
    }
    
    for (i=0;i<n;i++)
    {
        for (j=0;j<str[i].length();j++)
        {
            if (str[i][j] != ' ')
            {
                str[i][j] = conv[str[i][j]-97];
            }
        };
        outfile << "Case #" << i+1 << ": " << str[i] << endl;
    }
    
    infile.close();
    outfile.close();
    return 0;   
}

