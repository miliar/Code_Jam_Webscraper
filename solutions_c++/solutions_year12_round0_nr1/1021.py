#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <complex>
#include <algorithm>

using namespace std;

const int kBufferSize = 1 * 1024;

char buffer[kBufferSize];

// Predefined methods
char* read_line() 
{
  int ch, size = 0;
  while ((ch = getchar()) != '\n') buffer[size++] = ch;
  buffer[size] = '\0';
  return buffer;
}


int main(int argc, char *argv[])
{
  int t, i, j, length;
  char map[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
  
  scanf("%d\n", &t);

  for (i = 1; i <= t; i++) {
    length = strlen(read_line());
    for (j = 0; j < length; j++)
      if (buffer[j] != ' ')
        buffer[j] = map[buffer[j] - 'a'];
    printf("Case #%d: %s\n", i, buffer);
  }
  return EXIT_SUCCESS;
}

