#include<iostream>
#include<set>
#include<vector>
#include<map>

using namespace std;
map<string, int> name;
set<string> ok;
string se[101];
string q[1001];



int main()
{
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int n,m,t;
  cin >> t;
  for (int ti = 0; ti < t; ti++)
  {
    cin >> n;
    string temp;
    getline(cin,temp);
    ok.clear();
    name.clear();
    for (int i = 0; i < n; i++)
    {
      getline(cin,se[i]);
//      cout << se[i] << endl;
      ok.insert(se[i]);
    }
    cin >> m;
//    cout << n << " " << m << endl;
    getline(cin,temp);
    for (int i = 0; i < m; i++)
    {
      getline(cin,q[i]);
    }
    int p = 0;
    int sum = 0;
    bool is_zero = false;
    while (p < m)
    {
      name.clear();
      for (int i = 0; i < n; i++)
        name[se[i]] = 0;
      for (int i = p; i < m; i++)
      {
        if (ok.find(q[i]) != ok.end())
        { 
          if (name[q[i]] == 0)
            name[q[i]] = i+1;
//          cout << "---- " << q[i] << endl;
        }
      }
      
      int maxi = 0;
      bool zero = false;
      for (int i = 0; i < n; i++)
      {
        if (maxi < name[se[i]])
          maxi = name[se[i]];
        if (name[se[i]] == 0)
          zero = true;
      }
      if (zero)
        break;
      else
      {
        p = maxi-1;
        sum++;
      }
    }
    cout << "Case #" << ti+1 << ": " << sum << endl;
  } 
  return 0;
}
