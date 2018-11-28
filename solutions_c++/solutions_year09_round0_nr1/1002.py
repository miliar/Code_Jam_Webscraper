#include <iostream>

using namespace std;

int st[75001][256];
int queue[75001];
int go[20][256];

int main ()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);  
  int l, d, n;
  int states = 1;
  cin >> l >> d >> n;
  for (int i = 0; i < d; i++)
  {
    int cur = 0;
    char s[20];
    cin >> s;
    for (int j = 0; j < l; j++)
    {
      if (st[cur][s[j]] == 0)
      {
        st[cur][s[j]] = states++;
      }
      cur = st[cur][s[j]];
      st[cur][0] = j+1;
    }
  }
  for (int i = 0; i < n; i++)
  {
    char s[500];
    cin >> s;
    int let = 0;
    memset(go,0,sizeof(go));
    for (int j = 0; j < l; j++)
    {
      if (s[let] != '(')
        go[j][s[let]] = 1;
      else
      {
        for (let++; s[let] != ')'; let++)
          go[j][s[let]] = 1;
      }
      let++;
    }
    queue[0] = 0;
    int ans = 0;
    for (int qbeg = 0, qend = 0; qbeg <= qend; qbeg++)
    {
      int state = queue[qbeg];
      int dist = st[state][0];
      if (dist == l) ans++;
      for (int let = 'a'; let <= 'z'; let++)
      {
        if (go[dist][let] && st[state][let] > 0)
        {
          queue[++qend] = st[state][let];
        }
      }
    }
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  return 0;
}