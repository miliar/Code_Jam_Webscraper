#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

const int MAX_N = 40;
string s[MAX_N];

int main()
{
  int T;
  cin >> T; cin.ignore();
  for(int t = 1; t <= T; t++)
    {
      cout << "Case #" << t << ": ";
      int N;
      cin >> N;
      for(int n = 0; n < N; n++)
        cin >> s[n];
      int r = 0;
      for(int n = 0; n < N; n++)
        {
          int m = n;
          for(;; m++)
            {
              int i = N-1;
              while(i >= 0 && s[m][i] == '0')
                i--;
              if(i <= n)
                break;
            }
          for(int j = m; j > n; j--)
            swap(s[j], s[j-1]);
          r += m-n;
        }
      cout << r << endl;
    }
}
