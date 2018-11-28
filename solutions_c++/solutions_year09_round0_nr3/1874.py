#include <cstring>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

#define MAX 1000

const  char welcome[]	= "welcome to code jam";
const int  welcome_size = 19;
int   P[welcome_size][MAX];

int solve(const char *line, int linesize)
{
  for (int j=0; j<linesize; ++j) {
    for (int i=0; i<welcome_size; ++i)
      P[i][j] = 0;
    if (line[j] == welcome[0])
      P[0][j] = 1;
  }
  //
  for (int i=1; i<welcome_size; ++i)
    for (int j=i; j<linesize; ++j)
      if (line[j] == welcome[i])
	for (int k=0; k<j; ++k)
	  P[i][j] = (P[i][j] + P[i-1][k]) % 10000;
  // sumamos la ultima
  int ret = 0;
  for (int k=0; k<linesize; ++k)
    ret += P[welcome_size-1][k];
  
  return ret;
}

int main()
{
  int N;
  cin >> N;
  getchar();
  char line[MAX];
  for (int i=1; i<=N; ++i) {
    fgets(line, MAX, stdin);
    line[strlen(line)-1]='\0';
    printf ("Case #%d: %04d\n", i, solve(line, strlen(line)));
  }
}
