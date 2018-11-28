#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

char swapLetter(char);

int cases = 0;
char code[] = {25,8,5,19,15,3,22,24,4,21,9,7,12,2,11,18,26,20,14,23,10,16,6,13,1,17};
const int start = int('a');
 
int main(int argc, char *argv[])
{
    cin >> cases;
    string words[cases];
    
    for(int i = 0; i < cases; i++)
    {
         while(words[i] == "")
         {
            getline(cin, words[i]);
         }        
    }
    for(int i = 0; i < cases; i++)
    {
          for(int j = 0; j < words[i].length(); j++)
          {
                words[i][j] =  swapLetter(words[i][j]); 
          }      
    }
    system("CLS");
    for(int i = 0; i < cases; i++)
    {
        cout << "Case #" << i+1 << ": " << words[i] << endl;       
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}

char swapLetter(char in)
{
     if(in != ' ')
     {
           return char(code[int(in)-start]+start-1);
     }else{
           return in;
     }
}
