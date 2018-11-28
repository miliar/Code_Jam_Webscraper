/**
 * CodeJam 2012 Qualification Round Problem C
 *
 * @author Dennis J. McWherter, Jr.
 * @date 13 April 2012
 */

/** NOTE: Mixed C/C++ - using C++ hash map began solution in C
   but found C++ aspects useful.. probably leaks-galore */

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <string.h>

/* Truly awful to mix like this - sorry purists! Wouldn't do this
 in production code! xD */
#include <map>
#include <utility>

void itoa(int x, char* buf)
{
  if(buf == NULL)
    return;
  sprintf(buf, "%d", x);
}

char* swapStr(int end, char* buffer)
{
  char* ret = NULL;
  int i = 0;
  int pos = 0;
  int length = 0;
  
  if(end < 0 || buffer == NULL)
    return NULL;
  
  ret = (char*)malloc(8*sizeof(char));
  length = strlen(buffer);
  
  memset(ret, 0, 8);
  
  for(i = end ; buffer[i] != '\0' ; ++i, pos++)
    ret[pos] = buffer[i];
  for(i = 0 ; pos < length ; ++i, pos++)
    ret[pos] = buffer[i];
  
  ret[pos] = '\0';
  
  return ret;
}

void cleanupMemory(char** buf1, char** buf2)
{
  if(*buf1 != NULL) {
    free(*buf1);
    *buf1 = NULL;
  }
  
  if(*buf2 != NULL) {
    free(*buf2);
    *buf2 = NULL;
  }
}

int countRecycledPairs(int x, int lbound, int ubound, std::map<std::pair<int,int>, bool>& visited)
{
  char str[8]; /* Guaranteed large enough by spec */
  char* nStr = NULL;
  char* mStr = NULL;
  int pairs = 0;
  int i = 0;
  int j = 0;
  int length = 0;
  int n = x;
  int m = x;
  
  itoa(x, str);
  
  length = strlen(str);
  
  /* O(n*m) :S this is just quick and dirty */
  for(i = 0 ; i < length ; ++i) { /* n */
    cleanupMemory(&mStr, &nStr);
    
    nStr = swapStr(i, str);
    n = atoi(nStr);

    if(n < lbound || n > ubound)
      continue;
    
    for(j = 0 ; j < length ; ++j) { /* m */
      mStr = swapStr(j, str);
      m = atoi(mStr);
      
      if(m <= n || m > ubound)
        continue;
      
      // Constant time lookup/check
      std::pair<int,int> p(n, m);
      if(!visited[p]) {
        visited[p] = true;
        pairs++;
      }
    }
  }
  
  return pairs;
}

int procLine(FILE* file)
{
  int a = 0;
  int b = 0;
  int i = 0;
  int total = 0;
  
  if(file == NULL)
    return -1;
  
  fscanf(file, "%d %d\n", &a, &b);
  
  std::map<std::pair<int,int>, bool> visited;
  
  for( i = a ; i <= b ; ++i ) {
    total += countRecycledPairs(i, a, b, visited);
  }
  
  return total;
}

void procFile(FILE* file)
{
  int numCases = 0;
  int i = 0;
  int total = 0;
  
  if(file == NULL)
    return;
  
  fscanf(file, "%d\n", &numCases);
  
  for( i = 0 ; i < numCases ; ++i) {
    total = procLine(file);
    printf("Case #%d: %d\n", (i+1), total);
  }
}

int main(int argc, char** argv)
{
  FILE* file = NULL;
  
  if(argc < 2) {
    fprintf(stderr, "Usage: %s <file>\n", argv[0]);
    return 1;
  }
  
  file = fopen(argv[1], "r");
  
  if(file == NULL) {
    fprintf(stderr, "Could not open file: %s\n", argv[1]);
    return 1;
  }
  
  procFile(file);
  
  fclose(file);
  
  return 0;
}

