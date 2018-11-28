#include <iostream>
#include <fstream>
#include <string>
using namespace std;



int N;
int S,Q;
string engine[120];
char buffer[120];
string query[1020];

int work[120][2];
int index[1020];

int solve() {
  for (int i = 0; i < Q; i++) 
    for (int j = 0; j < S; j++)
      if (query[i] == engine[j]) 
	index[i] = j;

  for (int i = 0; i < Q; i++)
    cout << index[i] << " ";
  cout << endl;

  for (int i = 0; i < S; i++)  work[i][0] = 0;
  work[index[0]][0] = -1;

  int b = 1;

  for (int i = 1; i < Q; i++) {
    for (int j = 0; j < S; j++) {
      if (j == index[i]) {
	work[j][b] = -1;
	continue;
      }
      int min = 65535;
      for (int k = 0; k < S; k++)
	if (work[k][1-b] != -1) {
	  int tmp = work[k][1-b];
	  if (j != k) tmp ++;
	  if (tmp < min) min = tmp;
	}
      work[j][b] = min;
    }
    b = 1 - b;
  }
  int result = 65535;
  for (int j = 0; j < S; j++)
    if (work[j][1-b] < result && work[j][1-b] != -1) result = work[j][1-b];
  return result;
}

	  

int main() {
  string name;
  cin >> name;
  ifstream fin(name.c_str());
  ofstream fout("result.txt");
  fin >> N;
  for (int i = 0; i < N; i++) {
    fout << "Case #" << i + 1 << ": ";
    fin >> S;
    fin.getline(buffer,10);
    cout << S << endl;
    for (int j = 0; j< S; j++) {
      string tmp = "";
      char s;
      while (fin.get(s)) {
	if (s == '\n') break;
	tmp = tmp + s;
      }
      engine[j] = tmp;
      cout << engine[j] << endl;
    }
    fin >> Q;
    fin.getline(buffer,10);
    for (int j = 0; j < Q; j++) {
      fin.getline(buffer,110);
      query[j] = string(buffer);
    }
    fout << solve() << endl;
  }
  return 0;
}
