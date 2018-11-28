#include <iostream>
#include <fstream>
#include <string.h>
#include <cstring>
#include <conio.h>
using namespace std;

int main()
{
    ifstream in;
    in.open("B-large.in");

    ofstream out;
    out.open("output.txt");
    
    int noc=0;
    in >> noc;
    
    
    for (int i=1; i<=noc; i++)
    {
        out << "Case #" << i << ": [" ;
        
        int c=0;
        in >> c;
        
        char com[c*2][3];
        
        for (int j=0; j<c*2; j+=2)
        {
            in >> com[j];
            //cout << "input com: " << com[j] << "\n" ;
            com[j+1][0] = com[j][1];
            com[j+1][1] = com[j][0];
            com[j+1][2] = com[j][2];
        }
/*        
        for (int j=0; j<c*2; j++)
        {
            com[j][3] = '\0';    
        }
*/        
        //cout << "\n\n\ncombine list\n\n" ;
        //for (int j=0; j<c*2; j++)
        //{
        //    cout << com[j] << "\n" ;    
        //}
        //cout << "\n\n\n" ;
        
        int d=0;
        in >> d;
        
        char opp[d*2][2];
        
        for (int j=0; j<(d*2); j++)
        {
            in >> opp[j];
            opp[j+1][0] = opp[j][1];
            opp[j+1][1] = opp[j][0];
            j++;
        }
        
        int len=0;
        in >> len;
        char* word = new char[len];
        in >> word;
        int length = len;
  
        for (int j=1; j<len; j++)
        {
            bool comb = false;
            
            for (int k=0; k<c*2; k++)
            {
                if (word[j] == com[k][0])
                {
                   //cout << "word: " << word << " at pos: " << j << "  combine 1st match found\n" ;
                   if (word[j-1] == com[k][1])
                   {
                      //cout << "2nd match found\n" ;
                      length--;
                      //cout << "new length: " << length << "\n\n" ;
                      char* temp = new char[length];
                      //cout << "temp initially: " << temp << "\n" ;
                      int m=0;
                      for (m=0; m<(j-1); m++)
                      {
                          //cout << "m = " << m << "\n" ;
                          temp[m] = word[m];
                          //cout << "after 1st for, temp: " << temp << "\n" ;
                      }
                      temp[m] = com[k][2];
                      //cout << "after copying T, temp: " << temp << "\n" ;
                      m++;
                      for ( ; m<length; m++)
                      {
                          temp[m] = word[m+1];
                          //cout << "last for entered\n" ;
                      }
                      //cout << "finally temp: " << temp << "\n" ;
                      strcpy(word,temp);
                      word[length] = '\0';
                      
                      j-=2;
                
                      //cout << "combine found... new word: " << word << "\n" ;
                
                      len = length;
                
                      comb = true;      
                      break;
                   }            
                }
            }
            
            if (comb)
               continue;
            
            for (int k=0; k<d*2; k++)
            {
                if (word[j] == opp[k][0])
                {
                   for (int m=0; m<j; m++)
                   {
                       if (word[m] == opp[k][1])
                       {
                          length -= (j+1);
                          char* temp = new char[length];
                          
                          for (int p=0, q=j+1; p<length; p++, q++)
                          {
                              temp[p] = word[q];
                          }
                          strcpy(word, temp);
                          word[length] = '\0';
                          
                          //cout << "oppose found... new word: " << word << "\n" ;
                          
                          len = length;
                          j = 0;
                       }
                   }
                }
            }
        }
        
        for (int x=0; x<length; x++)
        {
            if (x == 0)
               out << word[x] ;
            else
                out << ", " << word[x];
        }
        out << "]\n" ;
        //getch();
    }
    

    //system("pause");
    return 0;
}
