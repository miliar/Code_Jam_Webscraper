#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

int T;
//             abcdefghijklmnopqrstuvwxyz
string G, f = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
  cin >> T;
  getline(cin, G);
  for (int tc = 1; tc <= T; ++tc)
  {
    getline(cin, G);
    for (int i = 0; i < G.size(); ++i)
      if (G[i] != ' ')
	G[i] = f[G[i]-'a'];
    cout << "Case #" << tc << ": " << G << endl;
  }
}