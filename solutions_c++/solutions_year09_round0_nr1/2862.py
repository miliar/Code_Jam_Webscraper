#include <iostream>
#include <conio.h>
#include <fstream>

using namespace std;

int matchPatternWithWords(string pattern,string* wordArr, int numwords, int wordlen)
{
    /* First lets tokenize the pattern to extract individual segements */
    int patternLen = pattern.length();
    string* patternTokens = new string[wordlen];
    int wordMatch =0;
    size_t pos = 0;
    for(int i=0; i< wordlen; i++)
    {
            if(pattern.at(pos)!='(')
            {
                                    patternTokens[i] = pattern.at(pos);
                                    pos++;
            }
            else
            {
                int rightpos = pattern.find(')', pos);
                patternTokens[i] = pattern.substr(pos+1, rightpos-pos-1);
                pos = rightpos+1;
            }
    }
    
    /* Now that the pattern is tokenize, find if the tokens contain the letter required */
    for(int i=0;i < numwords; i++)
    {
            int j;
            for(j=0; j<wordlen;j++)
            {
                    char chartofind = wordArr[i].at(j);
                    if(string::npos == patternTokens[j].find(chartofind))
                                    break;
            }
            if(j==wordlen)
            {
                          wordMatch++;
            }
    }
    return wordMatch;
}
int main(int argc, char** argv)
{
/* Code to parse input file */
   if(argc!=2)
   {
              cout <<"\n Please enter input file name ";
              getch();
              return 0;
   }
   fstream infile(argv[1]);
   int L, D, N;
   infile>> L;
   infile>> D;
   infile>> N;
   string* wordArr = new string[D];
   string* patternArr = new string[N];
   for(int i=0;i <D;i++)
   {
           infile>> wordArr[i];
   }
   for(int i=0; i<N; i++)
   {
           infile >> patternArr[i];
   }
   for(int i =0;i<N; i++)
   {
           int result = matchPatternWithWords(patternArr[i],wordArr, D, L);
           cout<< "Case #"<<i+1<<": "<<result<<endl;
   }
   
   return 0;
}
