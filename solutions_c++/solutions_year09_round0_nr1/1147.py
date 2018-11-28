#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <set>

using namespace std;

typedef vector<set<char> > Pattern;

Pattern parse_pattern(const string &str)
{
  enum { Letter, Set } state = Letter;
  set<char> current_set;
  Pattern pat;
  for (int i=0; i<str.length(); i++)
  {
    if (str[i]=='(')
    {
      current_set.clear();
      state = Set;
    }
    else if (str[i]==')')
    {
      pat.push_back(current_set);
      state = Letter;
    }
    else
    {
      if (state==Set)
        current_set.insert(str[i]);
      else // state==Letter
      {
        current_set.clear();
        current_set.insert(str[i]);
        pat.push_back(current_set);
      }
    }
  }
  return pat;
}

bool match(const string &str, const Pattern &pat)
{
  for (int i=0; i<str.length(); i++)
    if (pat[i].count(str[i])==0)
      return false;
  return true;
}

int main()
{
  int l, d, n;
  scanf("%d %d %d\n", &l, &d, &n);

  vector<string> words(d);
  for (int i=0; i<d; i++)
    getline(cin, words[i]);

  vector<Pattern> patterns(n);
  string pat_str;
  for (int i=0; i<n; i++)
  {
    getline(cin, pat_str);
    patterns[i] = parse_pattern(pat_str);
  }

  for (int i=0; i<n; i++)
  {
    int count = 0;
    for (int j=0; j<d; j++)
      if (match(words[j], patterns[i]))
        count++;
    printf("Case #%d: %d\n", i+1, count);
  }

  return 0;
}

