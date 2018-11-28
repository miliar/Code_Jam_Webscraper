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

public:
  Case()
  {
  }

  virtual ~Case()
  {
  }

  // returns the given test case solution
  int GetSolution(const vector<string> &d, const string &p)
  {
    vector<string> v;
    string s;
    bool bGroup = false;
    int r = 0;

    for(int i = 0; i < p.length(); i++)
    {
      if(p[i] == '(')
      {
        bGroup = true;
      }
      else
      if(p[i] == ')')
      {
        bGroup = false;
        v.push_back(s);
        s.clear();
      }
      else
      if(bGroup)
      {
        s += p[i];
      }
      else
      {
        s = p[i];
        v.push_back(s);
      }
    }

    for(int i = 0; i < d.size(); i++)
    {
      bool b  = true;

      for(int j = 0; j < d[i].length(); j++)
      {
        if(v[j].find_first_of(d[i][j]) == string::npos)
        {
          b = false;
          break;
        }
      }

      if(b)
      {
        r++;
      }
    }

    return r;
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
    int L, D, N; // test cases count
    vector<string> d; // dictionary

    InputStream.open(szInputFile, ios::in);
    OutputStream.open(szOutputFile, ios::out | ios_base::trunc);

    vector<string> s = Split(GetLine());

    L = atoi(s[0].c_str());
    D = atoi(s[1].c_str());
    N = atoi(s[2].c_str());

    d.assign(D, "");
    for(int i = 0; i < D; i++)
    {
      d[i] = GetLine();
    }

    for(int i = 1; i <= N; i++)
    {
      Case *pCase = new Case();

      // read test case input
      string p; // pattern
      p = GetLine();

      // write solutions of all cases to the file
      int r = pCase->GetSolution(d, p);
      OutputStream << "Case #" << i << ": " << r << endl;

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