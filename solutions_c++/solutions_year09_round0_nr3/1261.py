#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <memory.h>
#include <set>
#include <map>
#include <vector>
#include <list>


using namespace std;

typedef int byte;

string INPUT_NAME = "input.txt";
string OUTPUT_NAME = "output.txt";

int n;

string phrase = "welcome to code jam";

int LEN = 19;

int dp[501][20];

int solve(string st)
{
    for (int i = 0; i < st.length() + 1; i++)
	memset(dp[i], 0, 20 * 4);
    dp[0][0] = 1;
    for (int i = 1; i <= st.length(); i++)
	for (int j = 0; j < LEN + 1; j++)
	{
	    dp[i][j] = dp[i - 1][j];
	    if (j >= 1 && st[i-1] == phrase[j-1])
	    {
		dp[i][j] += dp[i-1][j-1];
		//cout << i << ' ' << j << ' ' << dp[i][j] << '\n';
	    }
	    dp[i][j] %= 10000;
	}
    return dp[st.length()][LEN];
}
    
int dig(int value)
{
    int res = 0;
    do
    {
	res++;
	value /= 10;
    } while (value != 0);
    return res;
}

    
int main(int argn, char** args)
{
  string ainput;
  string aoutput;
  if (argn > 1 && strcmp(args[1],"HOME") == 0)
    {
      ainput = "input.txt";
      aoutput = "output.txt";
    }
  else
    {
      ainput = INPUT_NAME;
      aoutput = OUTPUT_NAME;
    }
  ifstream fin(ainput.c_str());
  ofstream fout(aoutput.c_str());

  fin >> n;
  string st;
  getline(fin,st);
  
  for (int i = 0; i < n; i++)
  {
      getline(fin,st);
      int result = solve(st);
      fout << "Case #" << i + 1 << ": ";
      for (int i = 0; i < 4 - dig(result); i++)
	  fout << '0';
      fout << result << '\n';

  }
  
  return 0;
}
