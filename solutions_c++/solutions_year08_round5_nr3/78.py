#include <vector>
#include <iostream>
#include <algorithm>
#include <utility>
#include <map>
#include <cmath>

using namespace std;
int rsz, csz;

int memo[10][1<<10][1<<10];
bool n2[10][10];

int doit(int currow, int bitmask0, int bitmask1)
{
  if(currow >= rsz) return 0;
  int& retVal = memo[currow][bitmask0][bitmask1];
  if(retVal != -1) return retVal;
  retVal = 0;

  for(int i = 0; i < csz; i++)
  {
      if(bitmask0 & (1<<i)) continue;

      int bitmask2 = bitmask0, bitmask3 = bitmask1;
      if(i >= 1) bitmask2 |= 1<<(i-1), bitmask3 |= 1<<(i-1);
      if(i <= csz - 2) bitmask2 |= 1<<(i+1), bitmask3 |= 1<<(i+1);
      bitmask2 |= 1<<i;

      if(n2[currow][i]) continue;
      retVal = max(retVal, 1 + doit(currow, bitmask2, bitmask3));
  } 
     
     retVal = max(retVal, doit(currow + 1, bitmask1, 0));
     return retVal;
}

int main()
{
    int n;
    cin >> n;
    
    for(int z = 0; z < n; z++)
    {
	memset(memo, -1, sizeof memo);
	int retVal = 0;

	cin >> rsz >> csz;

	for(int i = 0; i < rsz; i++)
	    for(int j = 0; j < csz; j++)
	    {
		char c; cin >> c;
		n2[i][j] = (c == 'x');
	    }


	cout << "Case #" << z + 1 << ": " << doit(0, 0, 0) << endl;
    }
}
