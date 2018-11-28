#include<iostream>
#include<string>
#include <fstream>
#include <vector>

#define INPUTFILE     "A-large.in"
#define OUTPUTFILE    "output.txt"

using namespace std;

int main()
{
    int numOfChar,numOfWords,noOfTestCases;
    vector<char> t;
    char ch;
    string str1;
    
    int flag =0,noOfMatch=0;
    register int i,j,k,l,m;
    vector<string> s;
    ifstream inFile(INPUTFILE); 
    if(!inFile) 
    {
        cout << "Cannot open Input file...Please check the input filename\n";
        exit(0);
    }

    inFile>>numOfChar;
    inFile>>numOfWords;
    inFile>>noOfTestCases; 
 
    ofstream outFile(OUTPUTFILE);
 
    for(i=0;i<numOfWords;i++)
    {
    	inFile>>str1;
	s.push_back(str1);
    }
    for(i=0;i<noOfTestCases;i++)
    {
        inFile>>str1;
        noOfMatch=0;
 
      //  cout<<numOfChar<<" "<<numOfWords <<" "<<noOfTestCases<<endl;
	for(j=0;j<numOfWords;j++)
        {
            l=-1;
            //flag =0;
	    for(k=0;k<numOfChar;k++)
            {
                l++;
                ch = s[j][k];
               // cout<<ch <<" "<<str1[l]<<endl;
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
