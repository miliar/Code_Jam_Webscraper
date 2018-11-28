#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

long findSequence(string &text, int tseq, string &str, int sseq)
{
     long count = 0;
     int index;  
     
     while(true) {
          index = text.find(str[sseq], tseq);
          
          if(index == string::npos) 
                   return count;
          else     {
              if (sseq == str.length() - 1)
                   count = count + 1; 
              else 
                   count = count + findSequence(text, index + 1, str, sseq + 1);
          }    
          
          tseq = index + 1;
     }                  
}

int main(int argc, char *argv[])
{
    
  ifstream myfile("c:\\temp\\input.txt");
  ofstream outfile("c:\\temp\\output.txt");
     
  string text, str = "welcome to code jam";
  char resstr[50], outstr[50], *res;
  long s;
  int num;
  
  if (myfile.is_open())
  {
    if (outfile.is_open()) {                       
       while (! myfile.eof() ) {
    
          getline (myfile,text);
          num = atoi(text.c_str());
          
          for(int i=0; i<num; i++) {
                  
                  getline (myfile,text);
                  s = findSequence(text, 0, str, 0);
                  
                  res = ltoa(s, resstr, 10);
                  
                  strcpy(outstr, "0000");
                  strcat(outstr, resstr);
                  
                  outfile<<"Case #" << i+1 << ": " << (outstr + strlen(outstr) - 4) <<endl;
          }
        }
     }   
     else cout << "Unable to open out file"; 
     
     myfile.close();
    }                
    
  else cout << "Unable to open in file"; 
  system("PAUSE");
  return EXIT_SUCCESS;
}
