/*
ID: Plagapong
LANG: C++
TASK: A
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#define INF 999999999

using namespace std;
ifstream fin;
ofstream fout;

int gcd(int x, int y) {return (y == 0 ? x : gcd(y, x % y));}

long long n;
int pd, pg;

void clearVars() {
  // Clear variables
  
}

void process() {
  // Code here!
  fin >> n >> pd >> pg;
  int pd1 = pd / gcd(pd, 100);
  int pd2 = 100 / gcd(pd, 100);
  if ((long long)pd2 > n) {
	fout << "Broken";
	return;
  }
  if ((pg == 100 && pd != 100) || (pg == 0 && pd != 0)) {
	fout << "Broken";
	return;
  }
  fout << "Possible";
  return;
}

int main(int argc, const char* argv[]) {
  if (argc != 3) {
	cout << "Please indicate input and output" << endl;
	exit(0);
  }
  fin.open(argv[1]);
  fout.open(argv[2]);
  int times;
  fin >> times;
  for (int i = 1; i <= times; i++) {
	fout << "Case #" << i << ": ";
	clearVars();
	process();
	fout << endl;
  }
  fin.close();
  fout.close();
  return 0;
}
