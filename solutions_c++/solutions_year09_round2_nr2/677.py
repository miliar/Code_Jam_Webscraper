#include <iostream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)n; i++)

int n, t;
int d[20], d1[20];
string s;

void calc()
{
  int c = s[n-1]-'0';
  int mini = 10;
  memset(d, 0, sizeof(d));
  
  for(int i = n-1; i >= 0; i--)
    if (s[i]-'0' >= c)
      c = s[i]-'0';
     else
      {
        
        forn(j, i)
          cout << s[j];

        for(int j = i; j < n; j++)
          d[s[j]-'0']++;

        for(int j = i; j < n; j++)
          if (s[j]-'0' > s[i]-'0' &&
              s[j]-'0' < mini)
            mini = s[j]-'0';

        cout << mini;

        d[mini]--;

        for(int j = 0; j <= 9; j++)
          forn(k, d[j])
            cout << j;

        cout << endl;
        return;
      }

  for(int i = 0; i < n; i++)
    d[s[i]-'0']++;
  
  forn(i, n)
    if (s[i]-'0' < mini && s[i]-'0' != 0)
      mini = s[i]-'0';

  cout << mini;
  cout << "0";
  d[mini]--;
        for(int j = 0; j <= 9; j++)
          forn(k, d[j])
            cout << j;

        cout << endl;
        return;


  
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);

  forn(tt, t)
  {
  	cin >> s;
  	n = s.length();
  	
  	printf("Case #%d: ", tt+1);
  	calc();
  }
}