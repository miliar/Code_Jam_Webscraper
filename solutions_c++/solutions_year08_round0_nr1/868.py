#include<iostream>
#include<string>
using namespace std;

string nam[104];
int que[1005];
int f[1005];
int n;
int s;
int q;


void init()
{
  string buff;
  cin >> s;
  getline(cin,buff);
  for (int i = 0; i < s; ++i) {
    getline(cin, nam[i]);
  }
  cin >> q;
  getline(cin, buff);
  for (int i = 1; i <= q; ++i) {
    string tmp;
    getline(cin, tmp);
    for (int j = 0; j < s; ++j) {
      if (nam[j] == tmp) {
	que[i] = j;
	break;
      }
    }
  }
}

void proc()
{
  int cov[105] = {0};

  f[0] = -1;
  f[1] = 0;
  for (int i = 2; i <= q; ++i) {
    f[i] = i;
    int cv = 0;
    int t = i;
    if (cov[que[t]] != i) {
      ++cv;
      cov[que[t]] = i;
    }
    while (cv < s) {
      if (f[t-1]+1 < f[i]) {
	f[i] = f[t-1]+1;
      }
      --t;
      if (t == 0) {break;}
      if (cov[que[t]] != i) {
	++cv;
	cov[que[t]] = i;
      }
    }
  }
  f[0] = 0;
}

void outp()
{
  cout << f[q] << endl;
}

int main()
{
  cin >> n;
  for (int i = 0; i < n; ++i) {
    init();
    proc();
    cout << "Case #" << i+1 << ": ";
    outp();
  }
}
