#include<iostream>
#include<fstream>

using namespace std;

int main(){
  ifstream in("C-large.in");
  ofstream out("C-large.out");

  int nrcases;
  in>>nrcases;

  for (int T = 1; T<=nrcases; T++){
 
    int R,k,N;
    in>>R>>k>>N;
    
    int g[N];
    for (int i = 0; i<N; i++)
      in>>g[i];

    long long total = 0;
    int p = 0;
    int a[N];
    for (int j = 0; j<N; j++)
      a[j] = 0;
    
    int c[N]; // the order in which the permutations appear
    int index = 0; // for c

    while (R>0){
      int i = 0; // number of groupes
      long long s = 0; // number of people (or euros)
    
      if (a[p])
	break;
      else
	a[p] = 1;
     
      c[p] = index++;

      while ( (s+g[p] <= k) && (i+1 <= N) ){
	s += g[p];
	i++;
	p = (p+1)%N;
      }
      total += s;

      R--;
    }

    if (R > 0) {
      // find out the sum that repeats
      int x = index - c[p]; // number of permutations/situations that repeat forever
      long long total_rec = 0;

      while (x>0) {
	
	x--;
	int i = 0;
	long long s = 0;
	
	while ( (s+g[p] <= k) && (i+1 <= N) ){
	  s += g[p];
	  i++;
	  p = (p+1)%N;
	}
	total_rec += s;	
      }
      
      // cout<<total_rec<<"\n";
      x = index - c[p];
      if (x>0) {
	int y = R/x; // how many times these repeating situations will contribute to the total
	total += total_rec*y;
	R = R%x;
	// cout<<total<<" "<<R<<" "<<x<<"\n";
      }

      // add what is left from the remaining rounds
      while (R > 0) {
	
	R--;
	int i = 0;
	long long s = 0;
	
	while ( (s+g[p] <= k) && (i+1 <= N) ){
	  s += g[p];
	  i++;
	  p = (p+1)%N;
	}
	total += s;	
      }
    }
    // cout<<R<<" "<<p<<"\n";
    
    out<<"Case #"<<T<<": "<<total<<"\n";
  }
  
  in.close();
  out.close();
}
