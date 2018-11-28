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
  vector < vector <int> > m;
  vector< vector< pair<int, int> > > s;

  pair<int, int> GetSink(int r, int c)
  {
    if(s[r][c].first != -1)
    {
      return s[r][c];
    }

    int dr[] = {-1, 0, 0, 1};
    int dc[] = {0, -1, 1, 0};
    int x = -1;
    int q = -1;

    for(int d = 0; d < 4; d++)
    {
      if(0 <= r + dr[d] && r + dr[d] < m.size() &&
         0 <= c + dc[d] && c + dc[d] < m[0].size() &&
         ((q == -1 && m[r + dr[d]][c + dc[d]] < m[r][c]) || m[r + dr[d]][c + dc[d]] < q))
      {
        x = d;
        q = m[r + dr[d]][c + dc[d]];
      }
    }

    if(x == -1)
    {
      return make_pair(r, c);
    }
    else
    {
      return GetSink(r + dr[x], c + dc[x]);
    }
  }

public:
  Case()
  {
  }

  virtual ~Case()
  {
  }

  // returns the given test case solution
  vector<string> GetSolution(const vector < vector <int> > m)
  {
    int dr[] = {-1, 0, 0, 1};
    int dc[] = {0, -1, 1, 0};
    vector<string> res(m.size(), string(m[0].size(), '#'));
    map< pair<int, int>, char > ch;

    this->m = m;
    s.assign(m.size(), vector< pair<int, int> >(m[0].size(), make_pair(-1, -1)));

    for(int r = 0; r < m.size(); r++)
    {
      for(int c = 0; c < m[0].size(); c++)
      {
        s[r][c] = GetSink(r, c);
      }
    }

    char cc = 'a';
    for(int r = 0; r < m.size(); r++)
    {
      for(int c = 0; c < m[0].size(); c++)
      {
        if(ch.count(s[r][c]) == 0)
        {
          ch[s[r][c]] = cc++;
        }
        res[r][c] = ch[s[r][c]];
      }
    }

    return res;
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
      stringstream ss(GetLine());
      int H, W;
      ss >> H >> W;
      vector < vector<int> > m(H, vector<int>(W, -1));
      for(int r = 0; r < H; r++)
      {
        stringstream ss(GetLine());
        for(int c = 0; c < W; c++)
        {
          ss >> m[r][c];
        }
      }

      // write solutions of all cases to the file
      vector <string> r = pCase->GetSolution(m);
      OutputStream << "Case #" << i << ':' << endl;
      for(int i = 0; i < r.size(); i++)
      {
        for(int j = 0; j < r[i].length(); j++)
        {
          OutputStream << r[i][j] << ' ';
        }
        OutputStream << endl;
      }

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