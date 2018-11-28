#include <iostream>
#include <set>

using namespace std;

int main()
{
  int N;
  cin >> N;
  for (int caso=1;caso<=N;caso++)
  {
    int S;
    cin >> S;
    cin.ignore();
    string s;
    for (int i=0;i<S;i++)
    {
      getline(cin,s);
    }
    int Q;
    cin >> Q;
    cin.ignore();
    int sum=0;
    set <string> lt;
    while (Q--)
    {
      getline (cin,s);
      if (lt.empty())
        lt.insert(s);
      else
      {
        lt.insert(s);
        if (lt.size()==S)
        {
            lt.clear();
            lt.insert(s);
            sum++;
        }
      }
    }
    cout << "Case #" << caso << ": " << sum << endl;
  }
}
