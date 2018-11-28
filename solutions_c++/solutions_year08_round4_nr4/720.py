#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int t;

int size(string s)
{
  int sum = 0;
  for (int i = 1; i < s.size(); i++)
    if (s[i] != s[i-1])
      sum++;
  return sum+1;
} 


int main()
{
  freopen("d.in","r",stdin);
  freopen("d.out","w",stdout);
  
  cin >> t;
  string s;
  int k;
  for (int tt = 1; tt <= t; tt++)
  {
    cin >> k;
    vector<int> a;
    cin >> s;

    int mini = size(s);
    for (int i = 0; i < k; i++)
      a.push_back(i);

    while (next_permutation(a.begin(), a.end()))
    {
      string s1 = "";
      for (int i = 0; i < s.size(); i+=k)
      {
        string s2 = s.substr(i,k);
        string s3 = "";
        for (int j = 0; j < k; j++)
          s3+=s2[a[j]];
        s1+=s3;
      }
      if (size(s1) < mini) 
        mini = size(s1);
    }

    cout << "Case #" << tt <<": " << mini << endl;

  }

  return 0;
}