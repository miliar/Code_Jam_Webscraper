#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <sstream>
using namespace std;

string change(const string& s, const vector<int>& p, int k)
{
  string ret(s.size(), '-');
  for(int i=0;i<s.size();i++) {
    ret[i/k*k+p[i%k]] = s[i];
  }
  return ret;
}

int runlen(const string& s)
{
  int cnt = 1;
  char pre = s[0];
  for(int i=1;i<s.size();i++) {
    if(s[i] != pre) {
      cnt++;
      pre = s[i];
    }
  }
  return cnt;
}

int main()
{
  string s;
  int t;
  cin >> s;
  istringstream iss(s);
  iss >> t;
  for(int ii=0;ii<t;ii++) {
    cin >> s;
    istringstream iss2(s);
    int k;
    iss2 >> k;
    cin >> s;

    vector<int> v;
    for(int i=0;i<k;i++)
      v.push_back(i);

    int mini = 0xFFFFFF;

    do {
      string news = change(s, v, k);
      int cnt = runlen(news);
      if(cnt < mini)
	mini = cnt;
    }while(next_permutation(v.begin(), v.end()));
    
    cout << "Case #" << ii+1 << ": " << mini << endl;
  }

  return 0;
}
