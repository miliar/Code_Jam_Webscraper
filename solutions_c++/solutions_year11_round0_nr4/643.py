#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <stdio.h>

using namespace std;

template<class T>
string tostring(T a){stringstream ss; ss<<a; return ss.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])

string addc(char a, char b){return tostring(a)+tostring(b);}

//#define be cin

int main(){
	int t;
	ifstream be("D-large.in");
	be>>t;
	ofstream ki("ki.txt");
	FOR(tt,t){
		int n, h=0;
		be>>n;
		FOR(i,n){
			int c;
			be>>c;
			c--;
			if(c!=i)
				h++;
		}
		ki<<"Case #"<<tt+1<<": "<<h<<endl;
	}
	be.close();
	ki.close();
	return 0;
}