#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;

int index(char c)
{
  return c-97;
}

int setUp(char* translate)
{
  string i[3];
  i[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  i[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  i[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

  string o[3];
  o[0] = "our language is impossible to understand";
  o[1] = "there are twenty six factorial possibilities";
  o[2] = "so it is okay if you want to just give up";

  int count = 0;
  for(int n = 0; n < 26; n++)
    translate[n] = ' ';
  for(int n = 0; n < 3; n++)
    for(int j = 0; j < i[n].length(); j++)
    {
      if (i[n][j] != ' ')
      {
        translate[index(i[n][j])] = o[n][j];
        //cout << "translate " << index(i[n][j]) << " to " << o[n][j] << endl;
        count ++;
      }
    }
    cout << "translated: " << count << endl;
    for(int n = 0; n < 26; n++)
    {
      cout << char(n+97) << ": " << translate[n] << endl;
    }
    return count;
}

int main (int argc, char **argv) {
  ifstream inputFile(argv[1]);
  cout << "process file: " << argv[1] << endl;
  string lines;
  getline(inputFile, lines);
  int numOfLines = atoi(lines.c_str());
  cout << "number of lines: " << numOfLines << endl;
  string inputData[numOfLines];
  for(int i = 0; i < numOfLines; i++)
  {
    getline(inputFile, inputData[i]);
  }
  char translate[26];
  int numberKnown = setUp(translate);
  inputFile.close();
  
  ofstream output1("output1");
  ofstream output2("output2");

  for(int i = 0; i < numOfLines; i++)
  {
    output1 << "Case #";
    output1 << i+1;
    output1 << ": ";
    output2 << "Case #";
    output2 << i+1;
    output2 << ": ";
    for(int j = 0; j < inputData[i].length(); j++)
    {
      if(inputData[i][j] == ' ')
      {
        output1 << ' ';
        output2 << ' ';
      }
      else if(inputData[i][j] == 'q')
      {
        output1 << 'q';
        output2 << 'z'; 
      }
      else if(inputData[i][j] == 'z')
      {
        output1 << 'z';
        output2 << 'q'; 
      }
      else
      {
        output1 << translate[index(inputData[i][j])];
        output2 << translate[index(inputData[i][j])]; 
      }
    }
    output1 << '\n';
    output2 << '\n';
  }
  return 0;
}









