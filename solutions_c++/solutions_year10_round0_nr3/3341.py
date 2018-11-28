#include <vector>
#include <stdio.h>

using namespace std;

vector<int> line;
vector<int> roller;

int b; //number of boarded people
int r; //rides
int k; //size of rollercoaster
int n; //number of groups
int t; //number of tests
int total;

int board()
{
  if(line.empty()) return 0;
  if(b + line.front() > k) return 0;
  else 
  {
//    printf("boarded: %d\n", line.front());
    b+=line.front();
    total+=line.front();

    roller.insert(roller.begin(), line.front());
    line.erase(line.begin());
    return 1;
  }
}

void unboard()
{
  int size = roller.size();
  for(int i=0; i<size; i++)
  {
//    printf("unboarded(%d) : %d\n", roller.size(), roller.back());
    line.push_back(roller.back());
    roller.pop_back();
  }
}

int main()
{
  total=0;
  scanf("%d\n", &t);
  for(int i=0; i<t; i++)
  {
    total=0;
    line.clear();

    scanf("%d %d %d\n", &r, &k, &n);
    for(int j=0; j<n; j++)
    {
      int group;
      scanf("%d", &group);
      line.push_back(group);
    }
    
//    for(int j=0; j<line.size(); j++)
//    {
//      printf("%d ", line.at(j));
//    }

    for(int j=0; j<r; j++)
    {
      b=0;
      while(board()){
      }
      unboard();
    }
    printf("Case #%d: %d\n", i+1, total);
  }
}
