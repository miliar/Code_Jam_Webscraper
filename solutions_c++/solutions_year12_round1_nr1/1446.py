#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define PROBLEM_4

const string DEFAULT_PATH = "C:\\Documents and Settings\\Administrator\\desktop\\";
const string DEFAULT_INPUT_PATH = "C:\\Documents and Settings\\Administrator\\desktop\\input.txt";
const string DEFAULT_OUTPUT_PATH = "C:\\Documents and Settings\\Administrator\\desktop\\output.txt";

void speaking_in_tongues();
void dancing_with_the_googlers();
void recycled_numbers();
void password_problem();

int main()
{
#ifdef PROBLEM_1
  speaking_in_tongues();
#endif
#ifdef PROBLEM_2
  dancing_with_the_googlers();
#endif
#ifdef PROBLEM_3
  recycled_numbers();
#endif
#ifdef PROBLEM_4
  password_problem();
#endif
#ifdef PROBLEM_5
#endif
#ifdef PROBLEM_6
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

    for (unsigned person = 0; (int)person < N; person++)
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

void recycled_numbers()
{
  int T;
  string A, B;

  //Open file
  ifstream ifile;
  ifile.open((DEFAULT_PATH + "C-large.in").c_str());

  //Get T
  ifile >> T;

  //Open output file for write
  ofstream ofile;
  ofile.open("output.txt");

  //Go through the tests
  for (int test = 0; test < T; test++)
  {

    //Read input
    ifile >> A >> B;

    int A_num = atoi(A.c_str()), B_num = atoi(B.c_str());
    int recycled = 0;
    map <string, string> n;
    map <string, string> m;

    //Go through the numbers
    for (int i = A_num; i <= B_num; i++)
    {
      stringstream ss;
      ss << i;
      string compare = ss.str();
      string current = compare;
      for (unsigned j = 1; j < A.size(); j++)
      {
        string temp = current.substr(1,current.size() - 1) + current[0];
        current = temp;
        if (current[0] != '0' && atoi(current.c_str()) > atoi(compare.c_str()) && n[current] != "Y" && atoi(current.c_str()) <= B_num)
        {
          recycled++;
          n[compare] = "Y";
          //ofile << compare << "\t" << current << endl;
        }
      }
    }

    //Output results
    ofile << "Case #" << test + 1 << ": " << recycled << endl;
  }

}

void password_problem()
{
  int T;
  int A, B;

  //Open file
  ifstream ifile;
  ifile.open((DEFAULT_PATH + "A-large.in").c_str());

  //Get T
  ifile >> T;

  //Open output file for write
  ofstream ofile;
  ofile.open("output.txt");

  for (int test = 0; test < T; test++)
  {
    //Get A and B
    ifile >> A >> B;

    vector <double> p_i;
    double input;

    //Get the probabilities for p_i
    for (int i = 0; i < A; i++)
    {
      ifile >> input;
      p_i.push_back(input);
    }

    double best_prob = 0;
    vector<double> bs_i;

    double prod_prob = 1;
    //Populate backspace vector
    for (int i = 0; i < A; i++)
    {
      prod_prob *= p_i[i];
      bs_i.push_back(prod_prob * (-B-1) + 2*B - A + 2 + 2*(A-i-1));
    }
    
    //try to get the best possibilities starting from type-all, backspaces, and then end
    best_prob = bs_i[bs_i.size() - 1];
    if (best_prob == B-A+1)
    {
    }
    //check best in backspaces
    else
    {
      for (int i = 0; i < A - 1; i++)
      {
        if (best_prob > bs_i[i])
        {
          best_prob = bs_i[i];
        }
      }

      if (best_prob > B+2)
        best_prob = B+2;
    }

    //Print results
    ofile << setprecision(6) << fixed << "Case #" << test+1 << ": " << best_prob << endl;
  }

  //Close the files
  ofile.close();
  ifile.close();
}