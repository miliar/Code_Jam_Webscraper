#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>

using namespace std;

  int c, d, n;
  vector<string> convert;
  vector<string> opposite;
  string str;
  string newstr = "";
  map<char, int> was;


inline void Solve(int TestNumber)
{
  convert.clear();
  opposite.clear();
  str.clear();
  newstr.clear();
  was.clear();
  c = d = n = 0;
  
  for (char ch = 'A'; ch <= 'Z'; ch++)
    was[ch] = 0;
  
  scanf("%d", &c);
  convert.resize(c);
  for (int i=0; i<c; i++)
    cin >> convert[i];

  scanf("%d", &d);
  opposite.resize(d);
  for (int i=0; i<d; i++)
    cin >> opposite[i];
  
  scanf("%d", &n);
  cin >> str;
  
  for (int i=0; i<n; i++)
  {
    newstr.push_back(str[i]);
    was[str[i]]++;
    
    bool waschange = true;
    while (waschange)
    {
      waschange = false;
      
      for (int j=0; j<c; j++)
	if (newstr.size() >= 2 && ((newstr[newstr.size()-1] == convert[j][0] && newstr[newstr.size()-2] == convert[j][1])
			       ||  (newstr[newstr.size()-1] == convert[j][1] && newstr[newstr.size()-2] == convert[j][0])))
	{
	  waschange = true;
	  was[newstr[newstr.size()-1]]--;
	  was[newstr[newstr.size()-2]]--;
	  was[convert[j][2]]++;
	  newstr.erase(newstr.size()-2, 100);
	  newstr.push_back(convert[j][2]);
	  break;
	}
	
      if (waschange)
	continue;
      
      for (int j=0; j<d; j++)
	if (was[opposite[j][0]]>0 && was[opposite[j][1]]>0)
	{
	  waschange = true;
	  newstr.clear();
	  was.clear();
	  for (char ch = 'A'; ch <= 'Z'; ch++)
	    was[ch] = 0;
	  break;
	}
    }
  }
  
  printf("Case #%d: [", TestNumber+1);
  for (int i=0; i<newstr.size(); i++)
    if (i != newstr.size()-1)
      printf("%c, ", newstr[i]);
    else
      printf("%c", newstr[i]);
  printf("]\n");
}

int main()
{
  freopen("input.txt","r", stdin);
  freopen("output.txt","w", stdout);
  
  int NumberOfTests;
  scanf("%d\n", &NumberOfTests);
  for (int i=0; i<NumberOfTests; i++)
    Solve(i);
}