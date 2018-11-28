#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define PROBLEM_2

const string DEFAULT_PATH = "C:\\Documents and Settings\\Administrator\\desktop\\";
const string DEFAULT_INPUT_PATH = "C:\\Documents and Settings\\Administrator\\desktop\\input.txt";
const string DEFAULT_OUTPUT_PATH = "C:\\Documents and Settings\\Administrator\\desktop\\output.txt";

void speaking_in_tongues();
void dancing_with_the_googlers();

int main()
{
#ifdef PROBLEM_1
  speaking_in_tongues();
#endif
#ifdef PROBLEM_2
  dancing_with_the_googlers();
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

void dancing_with_the_googlers()
{
  string input;
  int T, N, S, p;
  vector <int> t;

  //Open file
  ifstream ifile;
  ifile.open((DEFAULT_PATH + "B-large.in").c_str());

  //Read T
  ifile >> T;

  //Open output file for write
  ofstream ofile;
  ofile.open("output.txt");

  //Go through each case
  for (int test_case = 0; test_case < T; test_case++)
  {
    //Get N, S, p, and t
    ifile >> N >> S >> p;
  
    //Read t (scores)
    for (int scores = 0; scores < N; scores++)
    {
      ifile >> input;
      t.push_back(atoi(input.c_str()));
    }

    //Note: Normal score to pass is at or above (p*3)-2
    int pass_score = (p*3) - 2;
    int pass = 0;

    for (unsigned person = 0; person < N; person++)
    {
      //If score is at or above passing, add to counter
      if (t[person] >= p && t[person] >= pass_score)
        pass++;
      //If score is surprising, then it may have a shot
      else if (S > 0)
      {
        //...but only if the number is at p or higher and greater than or equal to pass score - 2
        if (t[person] >= p && t[person] >= (pass_score - 2))
        {
          pass++;
          S--;
        }
      }
    }

    ofile << "Case #" << test_case + 1 << ": " << pass << endl;

    //Erase vector
    t.clear();
  }
}