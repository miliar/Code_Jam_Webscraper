
//@author Anurag Sharma
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <climits>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

#define For(I,A,B)	for(int I = (A); I < (B); ++I)
#define Rep(I,N)	For(I,0,N)
#define ALL(A)		(A).begin(), (A).end()
#define zero(a)		memset((a),0,sizeof(a))
#define pb push_back
#define MP make_pair
#define sz size()

typedef vector<string> VS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long LL;
typedef long long longlong;

VS split(string text, char delim = ' ') {
  istringstream iss(text);
  VS res;
  string token;
  while (getline(iss, token, delim))
    res.pb(token);
  return res;
}

int main(){
  freopen("B-large.in","r",stdin);
  //freopen("B-small-attempt0.in","r",stdin);
  //freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  string baseelem = "QWERASDF";
  	
  int T;
  scanf("%d", &T);
  For(tc, 1, T+1) {

    set<string> combineset;
    map<string,char> combinemap;

    int C;
    scanf("%d", &C);
    string str;
    Rep(i, C) {
      cin>>str;
      //combine array
      string comb = "";
      comb += min(str[0],str[1]);
      comb += max(str[0],str[1]);
      combineset.insert(comb);
      combinemap[comb] = str[2];
    }

    //opposed
    int D;
    set<string> opposeset;
    scanf("%d", &D);
    Rep(i, D) {
      cin>>str;
      if(str[1] < str[0])
	str = string(str.rbegin(), str.rend());
      opposeset.insert(str);
    }

    int N;
    scanf("%d", &N);
    cin>>str;
    //cout<<"fin="<<str;
    deque<char> Q;
    Q.pb(str[0]);
    For(i, 1, N) {
      //cout<<"\nchecking:"<<str[i];
      if(Q.empty()) {
	Q.pb( str[i] );
	continue;
      }
      char last = Q.back();
      //cout<<"last ="<<last;
      string comb = "";
      comb+= min(last, str[i]);
      comb+= max(last, str[i]);
      //cout<<"comb = "<<comb;
      if( combineset.find(comb) != combineset.end() ) {
	Q.pop_back();
	Q.pb( combinemap[comb] );
	//cout<<"comb found for:"<<comb<<"="<<combinemap[comb];
      }else
	Q.pb( str[i] );

      bool breakout = false;
      for(deque<char>::iterator i = Q.begin(); i!=Q.end(); i++) {
	for(deque<char>::iterator j = i+1; j!=Q.end(); j++) {
	  string op = "";
	  op += min(*i, *j);
	  op += max(*i, *j);
	  if( opposeset.find(op) != opposeset.end())  {
	    Q.clear();
	    breakout = true;
	    break;
	  }
	}
	if(breakout)  break;
      }

    }

    string fin = "";
    if( Q.empty() )
      fin = "[";
    for(deque<char>::iterator i = Q.begin(); i!=Q.end(); i++) {
      if( i == Q.begin() )
	fin += "[";
      else
	fin += ", ";
      fin += *i;

    }
    fin += ']';

    printf("Case #%d: %s\n", tc, fin.c_str());
  }
  return 0;
}

