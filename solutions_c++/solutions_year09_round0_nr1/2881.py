#include <iostream>
#include <fstream>
//#include <cstring.h>

using namespace std;

void perform (char *ns, int *l, int *s, int *c) {
  int count = 0;
  for (int i = 0; ns[i] != '\0'; i++) {
    if (ns[i] == '(') {
      //cout << "i : " << i << endl;
      s[count] = i + 1;
      while (ns[i] != ')')
	i++;
      //cout << "i = " << i << endl;
      l[count] = i - s[count];
      c[count] = 0;
      count++;
    }
    else {
      s[count] = i;
      l[count] = 1;
      c[count] = 0;
      count++;
    }
  }
}

int main (int argc, char* argv[]) {
  if (argc != 2) {
    cout << "\nWrong usage !!! \n run as: alien inputfile";
    exit(0);
  }

  int L, D, N, i, j; 
  unsigned long possibleStrings, matches;
  int length[15], start[15], counter[15];
  char DStrings[5000][15], NStrings[1000];

  fstream f (argv[1], ios::in);
  fstream fout ("output2.out", ios::out);

  if (!f) {
    cout << "\nInvalid File!!!";
    exit(0);
  }

  f >> L >> D >> N;

  for (i = 0; i < D; i++) {
    f >> DStrings[i];
    //cout << DStrings[i] << endl;
  }

  for (i = 0; i < N; i++) {
    f >> NStrings;
    cout << NStrings << endl;
    perform (NStrings, length, start, counter);
    for (j = 0, possibleStrings = 1; j < L; j++) {
      possibleStrings *= length[j];
      //cout << length[j] << " " << start[j] << " " << counter[j] << " " << endl;
    }
    cout << possibleStrings << endl;
    int count = 0;
    char newString[15];
    matches = 0;

    int flag = 0;
    for (j = 0; j < D; j++) {
      for (int k = 0; k < L; k++) {
	flag = 0;
	for (int aa = start[k]; aa < (start[k] + length[k]); aa++) {
	  if (DStrings[j][k] == NStrings[aa]) {
	    flag = 1;
	    break;
	  }
	}
	if (flag == 0)
	  break;
      }
      if (flag == 1) {
	matches++;
	//cout << "matched : " << DStrings[j] << endl;
      }
    }

    //cout << "Matches : " << matches << endl;
    fout << "Case #" << i + 1 << ": " << matches << endl; 
  }
  f.close ();    
  fout.close ();
  cout << "\n Check output.out for output" << endl;
}
