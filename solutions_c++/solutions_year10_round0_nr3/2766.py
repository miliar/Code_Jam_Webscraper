// writing on a text file
#include <iostream>
#include <fstream>
using namespace std;


int GetNextIndex(int offset, int length)
{
	return (offset) % length;
}

int main () 
{
  string line;
  ifstream inFile("C-small.in");
  ofstream outFile("C-small.out");
  int T;
  if (inFile.is_open())
  {
    /*while (! inFile.eof() )
    {*/
      //getline (inFile,line);
      //cout << line << endl;
	  inFile >> T;
	  int R, k, N;
	  int groups[1000];
	  int last[1000];
	  int price[1000];
	  for(int i = 0; i<T; i++)
	  {
		  memset(groups, 0, sizeof(int) * 1000);
		  memset(last, 0, sizeof(int) * 1000);
		  memset(price, 0, sizeof(int) * 1000);
		  inFile >> R >> k >> N;
		  for(int j = 0; j<N; j++)
			  inFile >> groups[j];
		  for(int j = 0; j<N; j++)
		  {
			  int curGroup = 0;
			  int curInd = j;
			  while((curGroup + groups[curInd] <= k) && (GetNextIndex(curInd + 1, N) != j))
			  {
				  curGroup += groups[curInd];
				  curInd = GetNextIndex(curInd + 1, N);
			  }
			  if((GetNextIndex(curInd + 1,N) == j) && (curGroup + groups[GetNextIndex(curInd,N)] <= k))
			  {
				  curGroup += groups[curInd];
				  curInd = j;
			  }
			  price[j] = curGroup;
			  last[j] = curInd;
		  }
		  int ans = 0;
		  int ind = 0;
		  for(int kk = 0; kk<R; kk++)
		  {
			ans += price[ind];
			ind = GetNextIndex(last[ind], N);
		  }
		  outFile << "Case #" << i + 1 << ": " << ans << endl;
	  }
    //}
  }
  outFile.close();
  inFile.close();

  return 0;
}