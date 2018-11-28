#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
using namespace std;
const char *const pMessage = "welcome to code jam";

int FindChar(const string &str, unsigned strOffset, unsigned msgOffset, unsigned &totalResult)
{
  if (msgOffset >= strlen(pMessage))
  {
    totalResult++;
    return 0;
  }


  const string::size_type not_found = string::npos;
  string::size_type pos = strOffset;

  while (true)
  {
    pos = str.find(pMessage[msgOffset], pos);
    if (pos == not_found)
      return 1;

    FindChar(str, (unsigned)pos + 1, msgOffset + 1, totalResult);

    pos++;
  }
}


int Test(const string &str)
{
  unsigned result = 0;

  FindChar(str, 0, 0, result);

  return result;
}




int main(int argc, char *argv[])
{
  if (argc != 3) return 1;

  ifstream inFile(argv[1]);
  ofstream outFile(argv[2]);
  if (inFile.fail() || outFile.fail()) return 1;

  int N;
  inFile >> N;
  inFile.get(); // Eat a line break.

  vector<int> result;
  string buf;
  for (int i = 0; i < N; i++)
  {
    getline(inFile, buf);
    result.push_back(Test(buf));
  }

  // Output
  {
    for (int i = 0; i < N; i++)
    {
      if (i != 0) outFile << "\n";
      outFile << "Case #" << (i+1) << ": " << setw(4) << setfill('0') << result[i];
    }
    outFile << std::flush;
  }


  return 0;
}