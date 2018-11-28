#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

#define PROBLEM_1

const string DEFAULT_PATH = "C:\\Documents and Settings\\Administrator\\desktop\\";
const string DEFAULT_INPUT_PATH = "C:\\Documents and Settings\\Administrator\\desktop\\input.txt";
const string DEFAULT_OUTPUT_PATH = "C:\\Documents and Settings\\Administrator\\desktop\\output.txt";

void speaking_in_tongues();

int main()
{
#ifdef PROBLEM_1
  speaking_in_tongues();
#endif

  return 0;
}

void speaking_in_tongues()
{
  int T;
  string input;
  string S, G;

  //Create mapping of language
  string mapping = "yhesocvxduiglbkrztnwjpfmaq";

  //Open the file
  ifstream ifile;
  ifile.open((DEFAULT_PATH + "A-small-attempt1.in").c_str());

  //Read how many test cases (T)
  getline(ifile,input);
  T = atoi(input.c_str());

  ofstream ofile;
  ofile.open(DEFAULT_OUTPUT_PATH.c_str());

  //Go through test cases
  for (int i = 0; i < T; i++)
  {
    //Reset the translated language
    G = "";

    //Read input
     getline(ifile,S);

    //Translate characters
    for (unsigned j = 0; j < S.size(); j++)
    {
      char temp = S[j];
      //If space, put into G
      if (S[j] == ' ')
        G += S[j];
      //Else translate letters
      else
      {
        G += mapping[(int)S[j] - 97];
      }
    }

    ofile << "Case #" << i+1 << ": " << G << endl;
  }

  ifile.close();
  ofile.close();
}