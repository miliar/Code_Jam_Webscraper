#include <iostream>
#include <set>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

void all_string (vector<string>& all, vector<vector<char> > input, int index,
                 const int len, string temp)
{
  if (index >= len) {
    if (temp.length() == len)
      all.push_back(temp);
    return;
  }
  else {    
    for (size_t i = 0; i < input[index].size(); i++) {      
      all_string(all, input, index + 1, len, temp + input[index][i]);      
    }
    
  }
}
int caclu(vector<string> dict, string temp, int len)
{
  int j = 0;
  bool in;
  int result = 0;
  vector<vector<char> > input;
  for (int i = 0; i < len; i++) {
    vector<char> temp;
    input.push_back(temp);
  }
  in = false;
  for (size_t i = 0; i < temp.length(); i++) {
    
    if (temp[i] == '(') {
      in = true;
    }
    if (!in && temp[i] <= 'z' && temp[i] >= 'a') {
      input[j].push_back(temp[i]);
      j++;
    }
    if (in && temp[i] <= 'z' && temp[i] >= 'a') {
      input[j].push_back(temp[i]);
    }
    if (in && temp[i] == ')') {
      in = false;
      j++;
    }

  }
  // vector<string> all;
  // all_string(all, input, 0, len, "");
  bool mat;
  for (vector<string>::iterator beg = dict.begin();
    beg != dict.end(); beg++) {
      string temp = *beg;
      mat = true;
      for (int i = 0; i < len; i++) {
        vector<char>::iterator res = find(input[i].begin(), input[i].end(), temp[i]);
        if (res == input[i].end())
          mat = false;
      }
      if (mat == true)
        result++;
  }
  return result;
}

int main()
{
  int l, d ,n;
  cin >> l >> d >> n;

  vector<string> dict;
  int result;
  // vector<string> input;
  for (int i = 0; i < d; ++i) {
    string temp;
    cin >> temp;
    dict.push_back(temp);
  }

  for (int i = 0; i < n; ++i) {
    result = 0;
    string temp;
    cin >> temp;
    result = caclu(dict, temp, l);
    printf("Case #%d: %d\n", i + 1, result);    
  }
}