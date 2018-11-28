#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iostream>
#include <sstream>
#include <cassert>

using namespace std;

#define output(i,x) cout << "Case #" <<i+1 << ": "<<x << endl;


class MinimumSP {
private:
	
public:
};

bool lessp(const int &p1, const int &p2) {
  return (p1 > p2);
}  

int main() {
	MinimumSP  tester;

	int n;
	string temp1;

	cin >> n;
	getline(cin,temp1);
	for (int ZZ=0;ZZ<n;ZZ++) {
	  int m,v;
	  cin >> m;
	  getline(cin,temp1);
	  vector<long long> x; 
	  x.clear();
	  for (int i=0;i<m;i++) {
	    cin >> v; 
	    //cout << v << endl;
	    x.push_back(v);
	  }
	  vector<long long> y;
	  y.clear();
	  getline(cin,temp1);
	  for (int i=0;i<m;i++) {
	    cin >> v;
	    y.push_back(v);
	  }
	  getline(cin,temp1);
	  long long sum=0;
	  sort(x.begin(),x.end());
	  sort(y.begin(),y.end(),lessp);
	  for (int j=0;j<m;j++) {
	    //cout << x[j] << y[j] << endl;
	    sum+=(x[j]*y[j]);
	  }
	  
	  // Read the input here

	  cout << "Case #"<<ZZ+1<<": " << sum << endl;

	  // Print the output here


	}

}
