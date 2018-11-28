#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// typedefs
typedef vector<int> VI;
typedef vector<string> VS;

// defines
#define SWAP(x,y) (x)^=(y)^=(x)^=(y)
#define MAX(a,b)   (a)>(b)?(a):(b)
#define MIN(a,b)   (a)<(b)?(a):(b)
#define ABS(a) ((a)>0?(a):-(a))
#define STOI(s,d) istringstream(s)>>d
#define ITOS(d,s) {ostringstream t;t<<d;s=t.str();}
#define REP(i,n) for(int i=0;i<n;i++)
#define REPS(i,s) rep(i,s.length())
#define REPV(i,v) rep(i,v.size())
#define SZ(x) x.size()

// common
int GCD(int a,int b){for(int c;b;c=a,a=b,b=c%b);return a;}
int LCM(int a,int b){return a/GCD(a,b)*b;}

// parsing
template <class T>
vector<basic_string<T> > parse(const basic_string<T> &s,const basic_string<T> &delim){
  vector<basic_string<T> > ret(0);
  for (int b,e=0;;ret.push_back(s.substr(b,e-b)))
    if ((b=s.find_first_not_of(delim,e))==(e=s.find_first_of(delim,b)))
      return ret;
}
VI intparse(const string &s,const string &delim=" \t\n"){
  VS tmp=parse(s,delim);
  VI ret(0);
  for (VS::iterator i=tmp.begin();i!=tmp.end();i++)
    {int t;STOI(*i,t);ret.push_back(t);}
  return ret;
}

// my code
int main() {
	cout << "CJC 2008 Qualification Round: Saving the Universe" << endl;
	ifstream in("a-large.in", ios::in);  // declare and open
	ofstream out("a-large.out", ios::out);
	int N, S, Q;
	if (in.is_open())
  	{
		//test cases
		string line;
  		getline (in, line);
  		STOI(line, N);
  		//printf("Number of cases: %d\n", N);
		for(int i=0; i<N; ++i) {
			//search engines
	  		getline (in, line);
	  		STOI(line, S);
			VS engines(S);
			VI state(S, 1);	//initial state
			int L=S;	// how many are allowed at any time
			int sw=0;	// number of switches
			for(int j=0; j<S; ++j) {
		  		getline (in, line);
		  		engines[j] = line;
			}
			//printf("Case: %d, there are %d search engines\n", i+1, SZ(engines));
			
			//queries
	  		getline (in, line);
	  		STOI(line, Q);
			for(int q=0; q<Q; ++q) {
		  		getline (in, line);

		  		int p=0;
		  		//find this Q position in engines
		  		for(p=0; p<S; ++p) if (engines[p] == line) break;
		  		if (state[p] == 1) {
					state[p] = 0;
					if (--L==0) {
						//all off, must switch
						state.assign(S, 1);
						state[p]=0;
						L=S-1;
						sw++;
					}
				}
			}
			
			//output
     		out << "Case #" << (i+1) << ": " << sw << endl;
      		cout << "Case #" << (i+1) << ": " << sw << endl;
		}
		
    	in.close();
	}
	
	out.close();
	cin.get();
	return 0;
}
