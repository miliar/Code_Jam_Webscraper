#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <set>

#define REP(i, n) for (int i = 0; i < (n); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define SWAP(a, b,tmp) {tmp = a; a= b; b=tmp;}
#define SQR(a) ((a)*(a))
#define PI (acos(0.0)*2)
#define MIN(a, b) ((a) < (b) ? (a):(b))
#define MAX(a, b) ((a) > (b) ? (a):(b))

#ifdef _WIN32
typedef __int64 int64;
#else
typedef long long int64;
#endif

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VS> VVS;



VS tokenize(string s, string token)
{
   VS res;
   string st = "";
   REP(i, s.length())
  {
     if (token.find(s[i])==string::npos)
    {
        st+=s[i];
    }
    else
    {
       if (st!="")
      {
         res.push_back(st); st = "";
       }
     }
   }
   if (st!="") res.push_back(st);
   return res;
}

VI toInt(VS s) {
  VI res;
  REP(i, s.size())
  {
     int d;
     sscanf(s[i].c_str(), "%d", &d);
     res.push_back(d);
  }
  return res;
}

int a[510][510];

int main(void)
{
	int n = 0;
	char line[1000];

	FILE* f = fopen("in.txt", "r");
	fscanf(f, "%d", &n);
	fgets(line, 1000, f);

	string word = "welcome to code jam";
	
	
	
	for (int i = 0; i < n; i++)
	{		
		fgets(line, 1000, f);
		memset(a, 0, 510*510 * 4);

		int m = strlen(line);
		REP(j, m)
		{
			if (line[j]==word[0]) a[0][j] = 1;
		}

		for (int i= 1; i < word.length(); i++)
		{
			REP(j, m)
			{
				if (line[j]==word[i])
				{
					REP(k, j)
					{
						a[i][j] = (a[i][j] + a[i-1][k]) % 10000;
					}
				}
			}			
		}
		int sum = 0;
		REP(j, m)
			sum = (sum + a[word.length() - 1][j]) %10000;

		char result[5];
		sprintf(result, "%4d", sum);
		REP(j, 4) if (result[j]==' ') result[j] = '0';
		printf("Case #%d: %s\n", i+1, result);
	}
}