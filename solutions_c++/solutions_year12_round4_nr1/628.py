#include <cmath>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long Int;

vector<Int> D;
vector<Int> L;
vector<Int> highest;

int main()
{
  int T;
  cin >> T;
  for(int c=1;c<=T;c++) {
	int N;
	cin >> N;
	D.resize(N+1);
	L.resize(N+1);
	for(int i=0;i<N;i++) {
	  Int d, l;
	  cin >> d >> l;
	  D[i] = d;
	  L[i] = l;
	}
	int d;
	cin >> d;
	D[N] = d;
	L[N] = 0;

	highest.clear();
	highest.resize(N+1, 0);
	for(int i=N-1;i>=0;i--) {
	  for(int j=i+1;j<=N;j++) {
		const Int dist = D[j] - D[i];
		if(dist > L[i])
		  break;

		if(highest[j] == 0 && j != N)
		  continue;

		if(dist >= highest[j]) {
		  if(highest[i] == 0 || highest[i] > dist)
			highest[i] = dist;
		}
	  }
	}
	//	for(int i=0;i<N;i++)
	//	  cout << highest[i] << " ";
	//	cout << "\n";
	const bool canReach = (highest[0] > 0 && highest[0] <= D[0]);

	printf("Case #%d: %s\n", c, (canReach ? "YES" : "NO"));
  }

  return 0;
}
