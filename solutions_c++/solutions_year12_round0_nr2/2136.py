#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

// can you get t total points, best score at least p?
// 2 -> yes, with no surprising
// 1 -> yes, with surprising
// 0 -> no
int check(int t, int p) {
  if(p == 0)
	return 2;

  if((p) + (p-1) + (p-1) <= t)
	return 2;

  if(p == 1)
	return 0;

  if((p) + (p-2) + (p-2) <= t)
	return 1;
  
  return 0;
}

int main()
{
  int T;
  cin >> T;
  for(int C=1;C<=T;C++) {
	int N, S, p;
	cin >> N >> S >> p;
	vector<int> t(N);
	for(int i=0;i<N;i++)
	  cin >> t[i];

	int y = 0;
	int ourY = 0;
	int ourS = 0;
	for(int i=0;i<N;i++) {
	  int v = check(t[i], p);
	  if(v == 2)
		ourY++;
	  else if(v == 1)
		ourS++;
	}

	if(ourS <= S)
	  y = ourY + ourS;
	else
	  y = ourY + S;

	cout << "Case #" << C << ": " << y << "\n";
  }
}
