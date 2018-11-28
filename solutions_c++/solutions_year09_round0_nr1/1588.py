#include <assert.h>
#include <stdio.h>
#include <string.h>


const int MAXLEN = 16;
const int MAXWORDS = 10000;

int len;
int nwords;
char word[MAXWORDS][MAXLEN];
int ncases;

int main() {

  scanf("%d %d %d", &len, &nwords, &ncases);

  for(int i = 0; i < nwords; ++i) {
    scanf("%s", word[i]);
  }

  for(int caseNum = 0; caseNum < ncases; ++caseNum) {
    char pat[1024];
    scanf("%s", pat);
    int p = 0;
    bool options = false;
    
    bool good[MAXWORDS];
    memset(good, true, nwords);

    bool works[MAXWORDS];
	memset(works, false, nwords);

    for(int i = 0; pat[i] != '\0'; ++i) {
      if(pat[i] == '(') {
	options = true;
	memset(works, false, nwords);
      } else if(pat[i] == ')') {
	for(int j = 0; j < nwords; ++j) {
	  good[j] = good[j] && works[j];
	}
	++p;
	options = false;
	memset(works, false, nwords);
      } else {
	assert(p < len);
	for(int j = 0; j < nwords; ++j) {
	  if(word[j][p] == pat[i]) {
	    works[j] = true;
	  }
	}
	if(!options) {
	  for(int j = 0; j < nwords; ++j) {
	    good[j] = good[j] && works[j];
	  }
	  ++p;
	  options = false;
	  memset(works, false, nwords);
	}
      }
    }
    
    assert(p == len);

    int count = 0;
    for(int i = 0; i < nwords; ++i) {
      if(good[i]) ++count;
    }

    printf("Case #%d: %d\n", caseNum+1, count);
  }

  return(0);
}
