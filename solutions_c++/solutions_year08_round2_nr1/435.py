#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

int main(){

  int test = 1, N, i, j, k, m;
  long long n, A, B, C, D, xo, yo, M, x, y, x1, x2, x3, y1, y2, y3, c;
  vector< pair<long long, long long> > trees;

  cin >> N;

  while(N--){
    cin >> n >> A >> B >> C >> D >> xo >> yo >> M;

    x = xo;
    y = yo;

    trees.push_back(pair<long long, long long>(x, y));

    for(i = 1 ; i <= n - 1 ; i++){
      x = (A * x + B) % M;
      y = (C * y + D) % M;
      trees.push_back(pair<long long, long long>(x, y));
    }

    c = 0;

    for(i = 0 ; i < trees.size() ; i++)
      for(j = i + 1 ; j < trees.size() ; j++)
	for(k = j + 1 ; k < trees.size() ; k++){
	  x1 = trees[i].first;
	  y1 = trees[i].second;
	  x2 = trees[j].first;
	  y2 = trees[j].second;
	  x3 = trees[k].first;
	  y3 = trees[k].second;
	  
	  x = x1 + x2 + x3;
	  y = y1 + y2 + y3;

	  if(x % 3 == 0 && y % 3 == 0)
	    c++;

	  /*for(m = 0 ; m < trees.size() ; m++){
	    x = trees[m].first;
	    y = trees[m].second;

	    if(3 * x == x1 + x2 + x3 &&
	       3 * y == y1 + y2 + y3){
	      c++;
	      break;
	    }
	    }*/
	}

    cout << "Case #" << test++ << ": " << c << endl;

    trees.clear();
  }
}
