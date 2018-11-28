#include <string.h>
#include <stdio.h>


char combine[26][26];
unsigned int oppose[26];


int main() {


  int T;
  scanf("%d", &T);

  for(int i = 0; i < T; ++i) {
    memset(combine, 0, 26*26);
    for(int j = 0; j < 26; ++j) oppose[j] = 0;
    
    int c,d,n;

    scanf("%d", &c);

    //printf("Input is: %d ", c);
    for(int j = 0; j < c; ++j) {
      char buf[1024];
      scanf("%s", buf);
      //printf("%s ", buf);
      combine[buf[0]-'A'][buf[1]-'A'] = buf[2];
      combine[buf[1]-'A'][buf[0]-'A'] = buf[2];
    }

    scanf("%d", &d);
    //printf("%d ", d);
    for(int j = 0; j < d; ++j) {
      char buf[1024];
      scanf("%s", buf);
      //printf("%s ", buf);
      oppose[buf[0]-'A'] |= 1 << (buf[1]-'A');
      oppose[buf[1]-'A'] |= 1 << (buf[0]-'A');
    }

    scanf("%d", &n);
    char input[1024];
    scanf("%s", input);

    //printf("%d %s\n", d, input);

    char output[1024];
    int pos = 0;

    int count[26];
    for(int j = 0; j < 26; ++j) count[j] = 0;

    for(int j = 0; input[j] != '\0'; ++j) {
      output[pos++] = input[j];
      ++count[input[j]-'A'];
      while(pos >= 2 && combine[output[pos-2]-'A'][output[pos-1]-'A']) {
	--count[output[pos-1]-'A'];
	--count[output[pos-2]-'A'];
	output[pos-2] = combine[output[pos-2]-'A'][output[pos-1]-'A'];
	++count[output[pos-2]-'A'];
	pos -= 1;
      }

      for(int k = 0; k < 26; ++k) {
	if (oppose[output[pos-1]-'A'] & (1<<k) && count[k]) {
	  pos = 0;
	  for(int l = 0; l < 26; ++l) count[l] = 0;
	  break;
	}
      }

      output[pos] = '\0';
      //printf("%d %c %s\n", j, input[j], output);
    }

    printf("Case #%d: [", 1+i);
    for(int j = 0; j < pos; ++j) {
      printf("%c", output[j]);
      if(j != pos-1) {
	printf(", ");
      }
    }
    printf("]\n");
  }


  return(0);
}
