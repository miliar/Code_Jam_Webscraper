#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
int main()
{
  int T; 
  int N,D;
  vector <double> d;
  vector <double> l;
  vector <int> h;
  int i,j,k;
  int flag;
  cin >> T;
  for(i=0;i<T;i++){
    cin >> N;
    for(j=0;j <N;j++){
      cin >> k;
      d.push_back(k);
      cin >> k;
      l.push_back(k);
    }
    cin >> D;
      h.push_back(d[0]);
      for(j=1;j<N;j++){
	h.push_back(0);
	for(k=0;k<j;k++){
	  if(h[k] >=  d[j] - d[k]){
	    if(h[j] < d[j] - d[k]){
	      h[j] =  min(d[j] - d[k],l[j]);
	    }
	  }
	}
      }
      flag =0;
             for(j=0;j <N;j++){
	if(h[j] >= D - d[j]){
	  flag =1;
	}
      }
      if(flag ==1){
	    cout << "Case #" << i+1 << ": YES" << endl;
      }
      if(flag ==0){
		    cout << "Case #" << i+1 << ": NO" << endl;
      }
   d.clear();
   l.clear();
   h.clear();
  }
  return 0;
}