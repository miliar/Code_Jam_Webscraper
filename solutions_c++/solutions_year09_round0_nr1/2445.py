#include <cctype>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int L; // Word length
int D; // Word count
int N; // Test count


vector< vector<string> > testSet;
vector<string> wordList;
vector<string> testList;
vector<int> testResult;


void Output(ostream &target, const vector<int> result)
{
  for (unsigned i = 0; i < result.size(); i++)
  {
    if (i > 0) target << "\n";
    target << "Case #" << (i + 1) << ": " << result[i];
  }
  target << std::flush;
}



int Test(int n)
{
  int result = 0;

  const string::size_type not_found = string::npos;
  const vector<string> &test = testSet[n];

  for (int d = 0; d < D; d++)
  {
    const string &word = wordList[d];
    for (int i = 0; i < L; i++)
    {
      if (not_found == test[i].find(word[i]))
      {
        goto NEXT_WORD;
      }
    }
    result++;

NEXT_WORD:;
  }

  return result;
}



int main(int argc, char *argv[])
{
  if (argc != 3) return 1;

  ifstream inFile(argv[1]);
  ofstream outFile(argv[2]);
  if (inFile.fail() || outFile.fail())
  {
    return 1;
  }

  // temp char buffer.
  string buf;

  // Read file.
  {
    inFile >> L >> D >> N;
    inFile.get(); // Eat line break.

    // Get word list.
    for (int i = 0; i < D; i++)
    {
      getline(inFile, buf);
      wordList.push_back(buf);
    }

    // Get test code.
    for (int i = 0; i < N; i++)
    {
      getline(inFile, buf);
      testList.push_back(buf);
    }
  }

  // Build TEST_SET
  {
    for (int i = 0; i < N; i++)
    {
      const string &test = testList[i];

      vector<string> testChar;
      testChar.resize(L);
      for (int l = 0, p = 0; l < L; l++)
      {
        if (isalpha(test[p]))
        {
          testChar[l] = test[p];
          p++;
          continue;
        }
        else if (test[p] == '(')
        {
          p++;
          while (isalpha(test[p]))
          {
            testChar[l].push_back(test[p]);
            p++;
          }
          p++; // Skip ')'
        }
      }

      testSet.push_back(testChar);
    }

  }

  // Test the words.
  {
    for (int n = 0; n < N; n++)
    {
      testResult.push_back(Test(n));
    }
  }

  // Output
  {
    Output(outFile, testResult);
  }

  return 0;
}

