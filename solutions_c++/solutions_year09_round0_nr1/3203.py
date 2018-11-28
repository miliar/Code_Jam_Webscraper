#include<iostream>
#include<string>
#include <fstream>
#include <vector>

#define INPUT     "A-large.in"
#define OUTPUT    "output.txt"

using namespace std;

int main()
{
    int numOfCharacter,numOfWords,noOfTestCases;
    vector<char> t;
    char ch;
    string str1;
    
    int flag =0,noOfMatch=0;
    register int i,j,k,l,m;
    vector<string> s;
    ifstream inFile(INPUT); 
    if(!inFile) 
    {
        cout << " Input file can not be opened\n";
        exit(0);
    }

    inFile>>numOfCharacter;
    inFile>>numOfWords;
    inFile>>noOfTestCases; 
 
    ofstream outFile(OUTPUT);
 
    for(i=0;i<numOfWords;i++)
    {
    	inFile>>str1;
	s.push_back(str1);
    }
    for(i=0;i<noOfTestCases;i++)
    {
        inFile>>str1;
        noOfMatch=0;
 
      
	for(j=0;j<numOfWords;j++)
        {
            l=-1;
      
	    for(k=0;k<numOfCharacter;k++)
            {
                l++;
                ch = s[j][k];
      
                flag =0;
                if(str1[l]=='(')
                {
             	   for(l=l;str1[l]!=')';l++)
                       if(str1[l]==ch)
                          flag=1;
                }   
                else if(str1[l]==ch)
             
                    flag=1;
                     
                if(!flag) break;
                
             }
             if(flag)
               noOfMatch++;
        }
        outFile<<"Case #"<<i+1<<": "<<noOfMatch<<endl; 
   
    }
 
    inFile.close();
    outFile.close();
    return 0;
}
