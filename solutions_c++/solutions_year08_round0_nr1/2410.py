#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <iostream>
#include <sstream>
#include <cassert>

using namespace std;

#define output(i,x) cout << "Case #" <<i+1 << ": "<<x << endl;

vector<string> engine;
vector<string> query;
int S;
int Q;

class SavingUniverse {
private:

  int C[101][1001];
  bool ST[101][1001];
  int D[101][1001];

public:
  string clean(string x) {
    int start =0;
    int endt = x.length()-1;
    while ((start<x.length())&&(isspace(x[start]))) start++;
    while ((endt >=0)&& (isspace(x[endt]))) endt--;
    string temp;
    for (int i=start;i<=endt;i++) {
      temp+=x[i];
    }
    return temp;
  }
  int memC(int i, int j) {
    //cout << "i = " << i << " j = " << j << endl;
    //assert(j>=0);
    if (j<0) return Q+1;
    if (ST[i][j]) return C[i][j];
    //cout << "Here!" << endl;
    if (j==0) {
      if (engine[i]==query[0]) {
	C[i][0] = Q+1; D[i][0]=-1;
      } else {C[i][0]=0; D[i][0] = i;}
      ST[i][0] = true;
      return C[i][0];
    } else {
      //cout << "Here ***" << endl;
      //cout << "i = " << i << "j = " << j << endl;
      //cout << "i" << i << " j " << j << endl;
      //cout << query.size() << endl;
      //cout << engine.size() << endl;
      //cout << engine[i] << "=?" << query[j] << endl;
      if (engine[i]==query[j]){ 
	C[i][j] = Q+1; 
	D[i][j]=-1;
      } else {
	//cout << "I'm here!!" << endl;
	int min = memC(i,j-1);
	int mini = i;
	//cout << "min = " << min << "S = " << S << endl;
	for (int k=0;k<S;k++) {
	  if (k!=i) {
	    int t = memC(k,j-1)+1;
	    //cout << "t = " << t << endl;
	    if (t <=Q) {
	      if (t < min) {
		min=t;
		mini=k;
	      }
	    }
	  }
	}
	//cout << "i =" << i << "j = " << j << "min = " << min << "mini= " <<mini << endl;
	D[i][j] = mini;
	C[i][j] = min;
      }
      ST[i][j]=true;
      return C[i][j];
    }
  }
  int final(int S1,int Q1) {
	    // Infinity = Q + 1
    if (Q1==0) return 0;
    for (int i=0;i<S1;i++) {
      for (int j=0;j<Q1;j++) {
	ST[i][j]=false;
	C[i][j] = Q+100;
	D[i][j] = -1;
      }
    }
    int min = memC(0,Q1-1);
    int mini=0;
    //cout << "***" << min << " " << S1 << endl;
    for (int i=1;i<S1;i++) {
      int t = memC(i,Q1-1);
      //cout << t << endl;
      if (t<min) {
	min=t;
	mini = i;
      }
    }
    //cout << "Mini = " << mini << endl;
    /* list<string> use_engines;
    int place = mini;
    for (int k=Q-1;k>=0;k--) {
      use_engines.push_front(engine[place]);
      place=D[place][k];
      //cout << "place " <<place << " k = " << k << endl;
      assert(place >=0);
    }
    list<string>::iterator p;
    p = use_engines.begin();
    for (int i=0;i<Q;i++) {
      //cout << "Query = " << query[i] << "Engine = " << *p << endl;
      assert(query[i]!=*p);
      ++p;
      } */

    return min;
  }
};
int main() {
	SavingUniverse  tester;

	int n;
	string temp1;
	//vector<string> engine;
	//vector<string> query;
	cin >> n;
	getline(cin,temp1);
	for (int i=0;i<n;i++) {
	  //int S;
	  //int Q;
	  engine.clear();
	  query.clear();
	  cin >> S;
	  getline(cin,temp1);
	  string temp2;
	  for (int j=0;j<S;j++) {
	    getline(cin,temp2);
	    engine.push_back(tester.clean(temp2));
	    //cout << "U : " << temp2 << endl;
	  }
	  cin >> Q;
	  getline(cin,temp1);
	  for (int j=0;j<Q;j++) {
	    getline(cin,temp2);
	    query.push_back(tester.clean(temp2));
	    //cout << "Q : " << tester.clean(temp2) << endl;
	  }

	  // Read the input here
	  //cout << "S= " << S << "Q= " << Q << endl;
	  cout <<"Case #"<<i+1<<": " << tester.final(S,Q) << endl;
	}

}
