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


int main()
{
	VS words;
	string word;
	int l, d, n;	
	freopen("in.txt", "r", stdin);
	cin >> l >> d >> n;	
	REP(i, d) 
	{
		cin>> word;
		words.push_back(word);
	}
	REP(i, n)
	{
		string pattern;
		cin >> pattern;
		//VS groups = tokenize(pattern, "()");
		VS groups;
		int j = 0;
		while (j < pattern.length())
		{
			if (pattern[j]!='(') 
			{
				string s;
				s += pattern[j];
				groups.push_back(s);
			}
			else
			{
				j++;
				string s= "";
				while (pattern[j]!=')') 
				{
					s+=pattern[j];
					j++;
				}
				groups.push_back(s);				
			}
			j++;
		}

		int count = 0;
		if (groups.size()==l)
		{
			REP(j, words.size())
			{
				bool contain = true;
				REP(k, words[j].length())
				{
					if (groups[k].find(words[j][k])==string::npos)
					{
						contain = false; break;
					}
				}
				if (contain)
					count++;
			}
		}
		printf("Case #%d: %d\n", i+1, count);
	}
}
