#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

char buffer[128];

int first[1024];
int sec[1024];

int f = 0;
int s = 0;

int main(int argc, char* argv[])
{
  ifstream ifs("A-small.in");

  memset(buffer, 0, sizeof(buffer));
  ifs.getline(buffer, 128);
  int numCases = atoi(buffer);

  for(int i = 0; i < numCases; ++ i){
    memset(buffer, 0, sizeof(buffer));
    ifs.getline(buffer, 128);
    int numNumbers = atoi(buffer);

    f = 0; 
    s = 0;

    for(int j = 0; j < numNumbers; ++ j){
      ifs>>first[f];
      ++ f;
    }

    for(int j = 0; j < numNumbers; ++ j){
      ifs>>sec[s];
      ++ s;
    }

    ifs.getline(buffer, 128);

    sort(first, first+f, less<int>());
    sort(sec, sec+s, greater<int>());

    int sum = 0;

    for(int x = 0; x < f; ++ x){
      sum += first[x] * sec[x];
    }

    printf("Case #%d: %d\n", i+1, sum);

  }

  return 0;
}
