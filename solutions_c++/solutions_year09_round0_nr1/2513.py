#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int matchPattern(string word, string *chars)
{
    for (int i=0; i<word.length(); i++)    {
         if (chars[i].find(word[i]) == string::npos) 
            return 0;
    }

    return 1;
}

void genChars(string str, string *chars)
{
     int i, j, index = 0;
  
     for(i=0; i<str.length(); i++) {
              if (str[i] == '(') {
                         
                 j = i;
                 i = str.find_first_of(")", i);
                 chars[index++] = str.substr(j+1, (i-j)-1);  
                 
              } else
                 chars[index++] = str.substr(i, 1); 
     }           
}

void readLines(ifstream &myfile, int count, string *lines)
{
     string line;
     
     for (int i=0; i<count; i++)     {

         getline (myfile,line);
         lines[i] = line;
     };
}

void handleCase(ifstream &myfile)
{
     ofstream outfile("c:\\temp\\output.txt");
     string line, *words, *chars;
     int l, d, n, i, j, count;
          
     getline (myfile,line);
    
     i = line.find_first_of(" ");
     j = line.find_last_of(" ");
 
     l = atoi(line.substr(0, i).c_str());
     d = atoi(line.substr(i, j - i).c_str());
     n = atoi(line.substr(j).c_str()); 

     words = new string[d];
     chars = new string[l];

     readLines(myfile, d, words);
     
     if (outfile.is_open()) {
        for(i=0; i<n; i++) {

                 getline (myfile,line);
                 genChars(line, chars);
         
                 count = 0;
                 for (j=0; j<d; j++) {
                     count = count + matchPattern(words[j], chars);
                 } 
         
                 outfile << "Case #" << i + 1 << ": " << count << endl;
         }
         outfile.close();
  }
  
  else cout << "Unable to open out file";
     
}

int main(int argc, char *argv[])
{
  ifstream myfile ("c:\\temp\\input.txt");
  
  if (myfile.is_open())
  {
    while (! myfile.eof() )
          handleCase(myfile);              

    myfile.close();
  }

  else cout << "Unable to open in file"; 

  system("PAUSE");
  return EXIT_SUCCESS;
}
