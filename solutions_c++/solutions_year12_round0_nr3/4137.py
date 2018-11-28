#include <iostream>
#include <string>
#include <sstream>
#include <map>
using namespace std;

void f (int n,string str,map<int,int>& one,int& count,int A,int B)
{
  string t;
  for (int i = str.size()-1; i >= 1; i--)
  {
    if (str[i] == '0') continue;
    for (int j = i; j < str.size(); j++)
    {
      t.push_back(str[j]);
    }
    for (int j = 0; j < i; j++)
    {
      t.push_back(str[j]);
    }
    if (t.size() == str.size() && t.size() > 0)
    {
      int m = 0;
      stringstream ss;
      ss << t;
      ss >> m;
      if (n < m && m <= B && m >= A && one[n] != m)
      {
        one[n] = m;
	++count;
      }
      ss.clear();
    }
    t.erase(t.begin(),t.end()); 
  }
}

int main ()
{
  int N = 0;
  cin >> N;
  for (int i = 0; i < N; i++)
  {
  map<int,int> one;
  int count = 0;
  int A,B;
  cin >> A >> B;
  for (int n = A; n < B; n++)
  {
    stringstream ss;
    string tmp;
    ss << n;
    ss >> tmp;
    f(n,tmp,one,count,A,B);
  }
  cout << "Case #" << i+1 << ": " << count << endl;
  }
  return 0;
}
