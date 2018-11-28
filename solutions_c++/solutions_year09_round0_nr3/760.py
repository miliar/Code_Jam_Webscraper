#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>

using namespace std;


// constants
const char INPUT_FILE[] = "input.txt";
const char OUTPUT_FILE[] = "output.txt";
const int MAX_LINE_LENGTH = 30000;


// class Case solves a separate problem with the given arguments
class Case
{
private:
  static const long long M = 10000;

public:
  Case()
  {
  }

  virtual ~Case()
  {
  }

  // returns the given test case solution
  int GetSolution(const string &s, const string t = "welcome to code jam")
  {
    long long d[1000][1000];
    long long r = 0;

    memset(d, 0, sizeof(d));

    for(int i = 1; i <= t.length(); i++)
    {
      for(int j = 0; j < s.length(); j++)
      {
        if(s[j] == t[i - 1])
        {
          if(i == 1)
          {
            d[i][j] = 1;
          }
          else
          for(int k = 0; k < j; k++)
          {
            d[i][j] += d[i - 1][k];
            d[i][j] %= M;
          }
        }
      }
    }

    for(int i = 0; i < s.length(); i++)
    {
      r += d[t.length()][i];
      r %= M;
    }

    return int(r);
  }
};


// class Problem is used to read the input and write the output
class Problem
{
private:
  fstream InputStream;
  fstream OutputStream;

  // casts v from SrcClass to SrcClass value
  template< class SrcClass, class DestClass >
  DestClass Cast(SrcClass v)
  {
    stringstream ss;
    DestClass r;

    ss << v;
    ss >> r;

    return r;
  }

  // get the following line from input file
  string GetLine()
  {
    char sz[MAX_LINE_LENGTH];

    InputStream.getline(sz, sizeof(sz));

    return sz;
  }

  // split the given string by words, sDlm - array of delimiters
  vector< string > Split(string &sSrc, string sDlm = " ")
  {
    string w;
    vector<string> vResult;

    sSrc += sDlm[0];
    for(int i = 0; i < int(sSrc.length()); i++)
    {
      if(sDlm.find_first_of(sSrc[i]) == string::npos)
      {
        w += sSrc[i];
      }
      else
      {
        if(w.length() > 0)
        {
          vResult.push_back(w);
        }
        w.clear();
      }
    }

    return vResult;
  }

public:
  Problem()
  {
  }

  virtual ~Problem()
  {
  }

  // reads the given input and then write solution of all test cases to output file
  void Solve(const char szInputFile[], const char szOutputFile[])
  {
    int N; // test cases count

    InputStream.open(szInputFile, ios::in);
    OutputStream.open(szOutputFile, ios::out | ios_base::trunc);

    N = atoi(GetLine().c_str());

    for(int i = 1; i <= N; i++)
    {
      Case *pCase = new Case();

      // read test case input
      string s;
      s = GetLine();

      // write solutions of all cases to the file
      int r = pCase->GetSolution(s);
      string sr;
      stringstream ss;
      ss << r;
      sr = ss.str();
      while(sr.length() < 4) sr = '0' + sr;
      OutputStream << "Case #" << i << ": " << sr << endl;

      delete pCase;
    }

    InputStream.close();
    OutputStream.close();
  }
};


// applicaton entry point
int main(int argc, char *argv[])
{
  Problem *pProblem = new Problem();
  pProblem->Solve(INPUT_FILE, OUTPUT_FILE);
  delete pProblem;
  return 0;
}