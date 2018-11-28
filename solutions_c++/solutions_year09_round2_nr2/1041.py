#include <iostream>
#include <fstream>

using namespace std;

int main (int argc, char* argv[]) {
  fstream f (argv[1], ios::in);
  fstream w ("oout", ios::out);

  int T, i, j, k, length, nxtPos, nxtL, aa, bb;
  char str[100];
  //long long numb;

  f.getline (str, 100);
  T = atoi (str);

  //f >> T;

  i = 0;
  while (i < T) {
    f.getline (str, 100);
    length = strlen (str);
    int flag = 0;

    for (j = length - 1; j >= 0; j--) {
      nxtL = 10;
      nxtPos = 100;
      for (k = j + 1; k < length; k++) {
	//cout << str[k] << "ii ";
	if (str[k] > str[j] && (str[k] - 48) < nxtL) {
	  nxtL = str[k] - 48;
	  nxtPos = k;
	  //cout << nxtL << endl;
	}
      }
      if (nxtPos != 100) {
	char ch = str[j];
	str[j] = str[nxtPos];
	str[nxtPos] = ch;
	flag = 1;
	for (aa = j + 1; aa < length; aa++) {
	  for (bb = aa + 1; bb < length; bb++) {
	    if (str[aa] > str[bb]) {
	      char tmp = str[aa];
	      str[aa] = str[bb];
	      str[bb] = tmp;
	    }
	  }
	}

	//cout << "done" << endl;
    cout << str << endl;
    w << "Case #" << i + 1 << ": " << str << endl;
	break;
      }
    }
    //cout << flag << endl;
    if (flag == 0) {
      char str2[100];
      for (aa = 0; aa < length; aa++) {
	for (bb = aa + 1; bb < length; bb++) {
	  if (str[aa] > str[bb]) {
	    char tmp = str[aa];
	    str[aa] = str[bb];
	    str[bb] = tmp;
	  }
	}

      }
      if (str[0] == '0') {
	for (aa = 1; aa < length; aa++)
	  if (str[aa] > '0')
	    break;
	str[0] = str[aa];
	str[aa] = '0';
      }
      str2[0] = str[0];
      str2[1] = '0';
      for (aa = 1; aa < length; aa++)
	str2[aa + 1] = str[aa];
      str2[aa + 1] = '\0';
    cout << str2 << endl;
    w << "Case #" << i + 1 << ": " << str2 << endl;
    }
    i++;

  }

  f.close ();
  w.close ();
}
