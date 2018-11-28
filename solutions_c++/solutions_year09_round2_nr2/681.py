#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <cfloat>
#include <string>
#include <cstring>

typedef unsigned long long ull;

#define FOR(i,n) for (int i=0; i<(n); i++)
#define ALL(v) (v).begin(),(v).end()
#define PV(v) for (int __i=0; __i<(v).size(); __i++) cout << (v)[__i] << " "; cout << endl;

using namespace std;

int main()
{
  int _N;
  cin >> _N;

  string s;
  int badi;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> s;
      badi=-1;
      for (int i=s.size()-1; i>=1; i--)
	if (s[i-1]<s[i])
	  {
	    badi=i-1;
	    break;
	  }

      //      cout << "bad i is " << badi << endl;

      if (badi==-1)
	{
	  int zeroes=0;
	  for (int i=s.size()-1; s[i]=='0'; i--)
	    zeroes++;
	  cout << s[s.size()-1-zeroes];

	  for (int i=0; i<zeroes+1; i++)
	    cout << "0";

	  for (int i=s.size()-2-zeroes; i>=0; i--)
	    cout << s[i];
	}
      else
	{
	  int nums[10];
	  memset(nums,0,10*sizeof(int));
	  nums[s[badi]-'0']++;
	  int mingreater=10;
	  for (int i=badi+1; i<s.size(); i++)
	    {
	      nums[s[i]-'0']++;
	      if (s[i]>s[badi])
		mingreater=min(mingreater,(int)(s[i]-'0'));
	    }
	  nums[mingreater]--;

	  for (int i=0; i<badi; i++)
	    cout << s[i];
	  cout << (char)(mingreater+'0');
	  for (int i=0; i<10; i++)
	    {
	      for (int j=0; j<nums[i]; j++)
		cout << i;
	    }
	}

      cout << endl;
    }

  return 0;
}
