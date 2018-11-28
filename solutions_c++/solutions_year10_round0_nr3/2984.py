#include<queue>
#include<map>
#include<iostream>
#include<fstream>

using namespace std;

// memoization!

int solve(int R, int k, int N, int * g)
{
     int head = 0;
     int sum = 0;
     int ppl = 0;
     int groups_used = 0;
     for (int i = 0; i < R; ++i) {
	  //cout << "iteration " << i << "." << endl;
	  groups_used = 0;
	  ppl = 0;
	  while (groups_used < N && (ppl + g[head]) <= k) {
	       ppl += g[head];
	       groups_used++;
	       head = (head + 1) % N;
	  }
	  //cout << "  used " << groups_used << " groups." << endl;
	  //cout << "    =  " << ppl << " people." << endl;
	  sum += ppl;
     }

     return sum;
}

int main(int argc, char ** argv)
{
     if (argc != 2) {
	  cout << "usage: " << argv[0] << " <fname>" << endl;
	  return 0;
     }
     
     ifstream file;
     file.open(argv[1]);
     int n;
     file >> n;
     int g[1000] = {0};
     for (int i = 0; i < n; ++i) {
	  int R, k, N;
	  file >> R >> k >> N;
	  for (int j = 0; j < N; ++j) {
	       file >> g[j];
	  }
	  int soln = solve(R, k, N, g); //int, int, int, int *
	  cout << "Case #" << (i + 1) << ": " << soln << endl;
     }

     return 0;
}


