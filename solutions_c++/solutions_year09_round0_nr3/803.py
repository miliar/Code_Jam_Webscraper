#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

unsigned long long SUM[500][20];
char buf[1000];
unsigned long long ALL;

char *s = "welcome to code jam";

void debug(int len) {
    for(int i = 0; i < 20; i++) {
        for(int j = 0; j < len; j++) {
            cout << SUM[j][i] << ' ';
        }
        cout << endl;
    }
}

int main(int ac, char **av)
{
  if(ac != 2) {
      cout << av[0] << " input.txt" << endl;
      return -1;
  }

  ifstream in( av[1] );
  int n;
  in.getline(buf, sizeof buf);
  sscanf(buf, "%d", &n);
  int m = strlen(s);
  int last = m-1;

  for(int i=0;i<n;i++) {
    int len;
    int prefix=0;
    int prev = -1;
    in.getline(buf, sizeof buf);
    len = strlen(buf);
    memset(SUM, 0, sizeof(SUM));
    for(int j = 0; j < len; ++j) {
        if(buf[j]==s[0]){
            SUM[j][0] = 1;
            if(prev<0) prev=j;
        }
    }
    for(int k = 1; k < m; ++k) {
        int new_prev = -1;
        for(int j = prev+1; j < len; ++j) {
            if(buf[j] == s[k]) {
                if(new_prev<0) new_prev = j;
                for(int x = j-1; x>=0; --x) {
                    if(SUM[x][k-1] != 0) {
                        SUM[j][k] += SUM[x][k-1];
                        SUM[j][k] %= 10000;
                    }
                }
            }
        }
        if(new_prev==-1)
            break;  // no end
        prev = new_prev;
    }
    //debug(len);
    ALL=0;
    for(int j=0; j<len; ++j) {
        if(SUM[j][last] != 0) ALL += SUM[j][last];
    }
    ALL %= 10000;
    printf("Case #%d: %04d\n", i+1, ALL);
  }

  return 0;
}
