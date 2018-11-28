#include <cstdlib>
#include <iostream>
#include <string>
#include <list>
using namespace std;

int main(int argc, char *argv[])
{
    int L,D,N = 0;
    string word = "";
    list<string> words;
    cin >> L;    // length of words
    cin >> D;    // number of words
    cin >> N;    // number of patterns

    for(int i = 0;i<D;i++)
            {
                cin >> word;
                words.push_back(word);
            }
    
    for(int i = 0;i<N;i++)
            {
             int currentchar = 0;    // index for parsing pattern
             string pattern = "";    // pattern variable
             cin >> pattern;
             
             list<string> tokens;    //Put tokens in a list
             while(currentchar < pattern.length())
              {
               if(pattern.substr(currentchar,1) == "(")
                {
                 string group = "";
                 currentchar++;
                 while(pattern.substr(currentchar,1) != ")")
                  {
                   group = group + pattern.substr(currentchar,1);
                   currentchar++;
                  }
                 tokens.push_back(group);
                }
               else
                {
                 tokens.push_back(pattern.substr(currentchar,1));
                }
               currentchar++;
              }
              
              // Count How Many Words Match The Pattern
              int count = 0;
              
              // Loop Through Words
              list<string>::iterator currentword;
              currentword = words.begin();
              while(currentword != words.end())
               {
                int wordchar;
                wordchar = 0;
                word = *currentword;
                
                // Loop Through Tokens
                list<string>::iterator currenttoken;
                currenttoken = tokens.begin();
                while(currenttoken != tokens.end())
                 {
                  string token = *currenttoken;
                  if (token.find(word.substr(wordchar,1)) != string::npos)
                   {
                    currenttoken++;
                    wordchar++;
                   }
                  else
                   {
                    break;
                   }                                      
                 }
                if (currenttoken == tokens.end())
                 {
                  count++;
                 }
                currentword++;
               }
             cout << "Case #" << i+1 << ": " << count << endl;                  
            }
    return EXIT_SUCCESS;
}
