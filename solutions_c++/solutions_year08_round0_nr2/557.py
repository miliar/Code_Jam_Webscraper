#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int toint(char x) {
  return int(x-'0');
}

int tomin(string time) {
  return (600*toint(time[0]) + 60*toint(time[1]) +
	  10*toint(time[3]) + toint(time[4]));
}

int main() {
  int N, T, NA, NB;
  int minA, minB;
  int curA, curB;
  string s;
  vector<int> Astart, Aend, Bstart, Bend;
  cin >> N;
  for (int test = 0; test < N; test++) {
    cin >> T >> NA >> NB;
    Astart.resize(NA);
    Aend.resize(NA);
    Bstart.resize(NB);
    Bend.resize(NB);
    for (int i = 0; i < NA; i++) {
      cin >> s;
      Astart[i] = tomin(s);
      cin >> s;
      Aend[i] = tomin(s);
    }
    for (int i = 0; i < NB; i++) {
      cin >> s;
      Bstart[i] = tomin(s);
      cin >> s;
      Bend[i] = tomin(s);
    }

    minA = minB = 0;
    curA = curB = 0;
    for (int i = 0; i < 24*60; i++) {
      for (int j = 0; j < NA; j++) {
	if (Astart[j] == i) 
	  curA--;
	if (Aend[j]+T == i) 
	  curB++;
      }
      for (int j = 0; j < NB; j++) {
	if (Bstart[j] == i)
	  curB--;
	if (Bend[j]+T == i) 
	  curA++;
      }
      if (curA < minA)
	minA = curA;
      if (curB < minB)
	minB = curB;
    }
    
    cout << "Case #" << (test+1) << ": " << -minA << " " << -minB << endl;
  }

  return 0;
}
