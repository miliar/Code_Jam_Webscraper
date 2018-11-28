#include <iostream>
#include <vector>

using namespace std;

int abs(int x) 
{
   return (x > 0) ? x : -x;
}

int main() {
  int cases, buttons, n;
  char r;
  
  cin >> cases;
  
  for(int c = 1; c <= cases; c++) {
    cin >> buttons;
    
    int opos = 1, bpos=1, spas=0;
    int dist;
    
    vector<int> ovec, bvec;
    vector<pair<char,int> > input;
    
    for(int b = 0; b < buttons; b++) {
      cin >> r >> n;
      input.push_back(make_pair(r,n));
      if(r == 'O') 
	ovec.push_back(n);
      else
	bvec.push_back(n);
    }
    
    if(ovec.empty())
      ovec.push_back(1);
    if(bvec.empty())
      bvec.push_back(1);
    
    vector<int>::iterator oit = ovec.begin(), bit = bvec.begin();
    for(vector<pair<char,int> >::iterator it = input.begin(); it != input.end(); it++) {
      r = it->first;
      n = it->second;
      
      while(true) {
	if(r == 'O') {
	  
	  dist = *bit - bpos;
	  if(dist > 0)
	    bpos++;
	  else if(dist < 0)
	    bpos--;
	  
	  spas++;
	  
	  dist = n - opos;
	  if(dist != 0){
	    if(dist < 0)
	      opos--;
	    else
	      opos++;
	    
	  } else {
	    oit++;
	    break;
	  }
	  
	  
	} else {
	  spas++;
	  dist = *oit - opos;
	  if(dist > 0)
	    opos++;
	  else if(dist < 0)
	    opos--;
	  
	  dist = n - bpos;
	  if(dist != 0){
	    if(dist < 0)
	      bpos--;
	    else
	      bpos++;
	  } else {
	    bit++;
	    break;
	  }
	 
	}
	
      }
      //cout << spas << ", "<< opos << ", " << bpos << endl;
    }
    cout << "Case #" << c << ": "<< spas << endl;
  }
  
  return 0;
}