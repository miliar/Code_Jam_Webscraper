#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <set>

using namespace std;

#define D(x) cout << (x) << endl;
#define D2(x,y) cout << (x) << " " << (y) << endl;
#define D3(x,y,z) cout << (x) << " " << (y) << " " << (z) << endl;

int T;
unsigned long long int r;

int main()
{
  int n,m,len, num,i,j,k;
  stringstream ss,ss1;
  ifstream input("input.txt");
  input >> T;
  string s,s1;
  set<int> used;
  for (i = 1; i <= T; i++)
  {
    ss.str("");
    r = 0;
    input >> n >> m;
    ss << n;
    len = ss.str().length();

    for (k = n; k < m-1; k++)
    {
      ss.str("");
      used.clear();
      ss << k;
      s = ss.str();

      for (j = 1; j < len; j++)
      {
        if (s[len-j] != '0')
        {
//          ss1.flush();
          s1 = s.substr(len-j,j) + s.substr(0, len-j);
          // ss1 << s1;
          // ss1 >> num;
          num = atoi(s1.c_str());
          if (num >= n && k < num && num <= m && used.find(num) == used.end())
          {
           // D2(k, num)
            used.insert(num);
            r++;
          }
        }
      }
    }
    cout << "Case #" << i << ": "  << r << endl;
  }
  return 0;
}
