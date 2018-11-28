#include <string>
#include <iostream>

using namespace std;

int L, D, N;

int match(int* bitset, const char* word) {
  int x;
  for(int i = 0; i < L; i++) {
	x = 1 << (word[i] - 'a');
	if( !(x & bitset[i]) ) return 0;
  }
  return 1;
}

int *make_bitset(const char* test) {

  int* ret = new int[L];
  int c = 0;
  char* p = (char*) test;

  for(c = 0; c < L; c++) {
    	ret[c] = 0;
	if(isalpha(*p)) {
	  ret[c] = 1 << (*p - 'a');
	  p++;
	} else {
	  p++;
	  while(isalpha(*p)) {
	    ret[c] ^= 1 << (*p - 'a');
	    p++;
	  }
	  p++;
	}
  }
  return ret;
}

int main(void)
{
  cin >> L >> D >> N;
  //cout << " " << L << " " << D << " " << N << endl;
  string words[D];
  string tests[N];
  int matches[N];
  int** bitsets = new int*[N];

  //extra line
  getline(cin, words[0]);
  for (int c = 0; c < D; c++) {
    getline(cin, words[c]);
  }
  for (int c = 0; c < N; c++) {
    getline(cin, tests[c]); //cout << tests[c] << endl;
  }

  for (int c = 0; c < N; c++) {
    bitsets[c] = make_bitset(tests[c].c_str());
  }

  /*
  for (int c = 0; c < N; c++) {
    printf("%d %d:", c);
    for(int i = 0; i < L; i++) {
      printf("%x ", bitsets[c][i]);
    }
    printf("%s\n", tests[c].c_str());
  }*/

  for(int c = 0; c < N; c++) {
    matches[c] = 0;
    for(int d = 0; d < D; d++) {
	matches[c] += match(bitsets[c], words[d].c_str());
    }
  }

  for(int c = 0; c < N; c++) {
    printf("Case #%d: %d\n", c+1, matches[c]);
  }

}
