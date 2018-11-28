#include<iostream>
#include<cstring>
#include<iomanip>
using namespace std;

const int maxn = 100;
const int maxl = 500;
const string samp = "welcome to code jam";
const int smpl = 19;
int n;
string word;
int f[maxl+4][smpl+3];

void proc()
{
  for (int i = 0; i < smpl; ++i) {
    f[0][i+1] = 0;
  }
  f[0][0] = 1;
  for (int i = 0; i < word.length(); ++i) {
    f[i+1][0] = 1;
    for (int j = 0; j < smpl; ++j) {
      f[i+1][j+1] = f[i][j+1];
      if (word[i] == samp[j]) {
	f[i+1][j+1] += f[i][j];
      }
      f[i+1][j+1] %= 10000;
    }
  }
}

int main()
{
  cin >> n;
  getline(cin, word);
  for (int i = 0; i < n; ++i) {
    getline(cin, word);
    cout << "Case #" << i+1 << ": ";
    proc();
    cout.width(4);
    cout.fill('0'),
    cout << fixed << f[word.length()][smpl] << endl;
  }
  return 0;
}
