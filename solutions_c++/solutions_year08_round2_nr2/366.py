#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <math.h>
#include <set>

using namespace std;

void merge(vector<int> a[], int i, int j);
bool share(int a, int b, int P);

template <class T>
std::vector<T> prime_factors(T n){
  std::vector<T> factors;
  T last = (T)sqrt(n) + 1, i;

  while(n % 2 == 0){
    factors.push_back(2);
    n /= 2;
  }

  for(i = 3 ; i <= last ; i += 2)
    while(n % i == 0){
      factors.push_back(i);
      n /= i;
    }

  if(n > 1)
    factors.push_back(n);

  return factors;
}


int main(){

  int test = 1, C, count, i, j, r, s, A, B, P, n;
  vector<int> sets[1001];
  bool m;

  cin >> C;

  while(C--){

    cin >> A >> B >> P;

    count = 0;

    for(i = A ; i <= B ; i++)
      sets[i].push_back(i);

    m = true;

    while(m){
      m = false;

      for(i = A ; i <= B ; i++)
	for(j = i + 1 ; j <= B ; j++){

	  if(sets[i].empty() || sets[j].empty())
	    continue;

	  for(r = 0 ; r < sets[i].size() ; r++)
	    for(s = 0 ; s < sets[j].size() ; s++){
	      
	      if(share(sets[i][r], sets[j][s], P)){
		merge(sets, i, j);
		m = true;
		goto finish;
	      }
	      
	    }
	finish:;
	}
    }

    n = 0;
    
    for(i = A ; i <= B ; i++)
      if(!sets[i].empty()){
	//cout << sets[i][0] << endl;
	n++;
      }
    /*
    cout << "----------" <<endl;

    for(i = A ; i <= B ; i++){
      for(j = 0 ; j < sets[i].size() ; j++)
	cout << sets[i][j] << " " ;
      cout << endl;}

    cout << "-"<<endl;
    */
    cout << "Case #" << test++ << ": " << n << endl;

    for(i = A ; i <= B ; i++)
      sets[i].clear();
  }
}

void merge(vector<int> a[], int i, int j){

  a[i].insert(a[i].end(), a[j].begin(), a[j].end());
  a[j].clear();
}

bool share(int a, int b, int P){

  vector<int> x = prime_factors(a);

  for(int i = 0 ; i < x.size() ; i++)
    if(x[i] >= P && b % x[i] == 0)
      return true;

  return false;
}
