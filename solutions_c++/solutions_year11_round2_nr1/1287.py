#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;

#define INPUTFILE "A-large.in"
#define OUTPUTFILE "text.out"


int main() {
  int nTest;
  ifstream fi(INPUTFILE);
  ofstream fo(OUTPUTFILE);
  fi >> nTest;
  for (int test = 1; test <= nTest; test ++) {
    int n;
    int a[200][200];
    double wp[200], owp[200], oowp[200];
    double win[200], match[200];
    string s;
    fi >> n;
    getline(fi, s);
    for (int i = 0; i < n; i ++) {
      getline(fi, s);
      match[i] = 0;
      win[i] = 0;
      for (int j = 0; j < s.length(); j ++) {
	if (s[j] == '.') a[i][j] = -1;
        else if (s[j] == '1') a[i][j] = 1;
        else if (s[j] == '0') a[i][j] = 0;
	if (a[i][j] != -1) {
	  match[i] += 1;
	  if (a[i][j] == 1) win[i] += 1;
	}
      }   
    }
    //cout << match[0] << " " << win[0] << endl;
    //solve
    for (int i = 0; i < n; i ++) {
      wp[i] = win[i] / match[i];
      owp[i] = 0;
      oowp[i] = 0;
      for (int j = 0; j < n; j ++)
	if (a[i][j] != -1) {
	  if (a[i][j] == 1)
	    owp[i] = owp[i] + win[j] / (match[j] - 1);
	  else if (a[i][j] == 0)
	    owp[i] = owp[i] + (win[j] - 1) / (match[j] - 1);
	}
      owp[i] = owp[i] / match[i];
    }
    for (int i = 0; i < n; i ++) {
      for (int j = 0; j < n; j ++)
	if (a[i][j] != -1)
	  oowp[i] += owp[j];
      oowp[i] = oowp[i] / match[i];
    }
    //cout << owp[1] << " " << owp[2] << endl;
    fo << "Case #" << test << ":" << endl;
    for (int i = 0; i < n; i ++) {
      double ans = 0;
      ans = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
      fo << setprecision(12) << ans << endl;
    }
  }
  fi.close();
  fo.close();
  return 0;
}
