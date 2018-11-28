#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int n, m, b, s, t, p, q, bp, op;
  char c;

  while(cin>>n && n){
    for(int u = 1; u <= n; u++){
      cin >> m;
      vector<char> vec;
      vector<int> ovec, bvec;
      t = p = q = 0;

      for(int i = 0; i < m; i++){
	cin >> c >> b;
	vec.push_back(c);
	if(c == 'O'){
	  ovec.push_back(b);
	} else {
	  bvec.push_back(b);
	}
      }
      ovec.push_back(-1);
      bvec.push_back(-1);
      bp = op = 1;

      for(int i = 0; i < m; i++){
	bool f = true;
	if(vec[i] == 'O'){
	  while(f){
	    if(bvec[q] != -1){
	      if(bp > bvec[q]){
		bp--;
	      } else if(bp < bvec[q]){
		bp++;
	      }
	    }

	    if(ovec[p] == op){
	      f = false;
	    } else if(ovec[p] > op){
	      op++;
	    } else {
	      op--;
	    }
	    t++;
	  }
	  p++;
	} else {
	  while(f){
	    if(ovec[p] != -1){
	      if(op > ovec[p]){
		op--;
	      } else if(op < ovec[p]){
		op++;
	      }
	    }

	    if(bvec[q] == bp){
	      f = false;
	    } else if(bvec[q] > bp){
	      bp++;
	    } else {
	      bp--;
	    }
	    t++;
	  }
	  q++;
	}
      }
      
      cout << "Case #" << u << ": " << t << endl;
    }
  }

  return 0;
}
