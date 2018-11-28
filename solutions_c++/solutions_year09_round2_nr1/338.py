#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <functional>
#include <algorithm>
#include <numeric>
#include <bitset>
#include <cmath>
#include <sstream>
#include <complex>
using namespace std;

#define pb push_back
#define mp make_pair
#define pii pair<int,int>

#define fo(i,n) for(int i=0; i < (n) ; ++i)
#define FO(i,a,b) for(int i=a;i<=(b);++i)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define UNIQ(v) (v).erase(unique(ALL(v)),(v).end())

#define VDebug(x)  {fo(i,(x).size()) cout<<(x)[i]<<" ";cout<<endl;}
#define VVDebug(x) {fo(j,(x).size()) VDebug(x[j])}
				     
typedef istringstream iss;
typedef ostringstream oss;
typedef long long int lint;
typedef complex<double> point;
				     
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<VS> VVS;
				     
const char eof = -123;

void printBits(unsigned int x,int end = 32,int start = 0){for(int i = end-1;i>=start;i--) if(x & (1<<i)) cout<<1<<" "; else cout<<0<<" ";}
int readInt(){	int x;if(scanf("%d",&x) != 1) return eof;return x;}
char readChar() { char c; if(scanf("%c",&c) != 1) return eof; return c;}
lint readLL(){lint x; if(cin>>x) return x; return eof;}
double readDouble(){double f;if(scanf("%lf",&f) == 1)return f;return eof;}

void globalInit();
void tcInit();
void tcEnd();

//////////// START HERE ///////////

void globalInit(){
}

void tcInit(){
}

/////////// INIT BLOCKS END ///////
char buf[88];

typedef struct Node{
	double p;
	string feature;
	Node *left;
	Node *right;
	
	Node(queue<string>& q){
		assert(q.front() == "(");
		q.pop();
		p = atof(q.front().c_str());
		q.pop();
		if(q.front() != ")"){
			feature = q.front();
			q.pop();
			left = new Node(q);
			right = new Node(q);
		}
		assert(q.front() == ")");
		q.pop();
	}

	double getProb(set<string> featureList){
		if(feature == "") return p;
		return p * (featureList.count(feature) ? left : right) -> getProb(featureList);
	}

} Node;

queue<string> tokenize(string s,string delim){
	queue<string> ret;
	for(int i=0;i<s.size();++i){
		int j = s.find_first_of(delim,i);
		if(j < 0 || j >= s.size()) j = s.size();
		if(j > i) ret.push(s.substr(i, j-i));
		i = j;
	}
	return ret;
}

string readString(){
	char buf[33];
	scanf(" %s",buf);
	return string(buf);
}
void solve(){
	int lines = readInt();
	string input = "";
	while(lines--){
		scanf(" %[^\n]",buf);
		input += string(buf);
	}
	fo(i,input.size()) if(input[i] == '(' || input[i] == ')' ){
		input = input.substr(0, i) + " " +input[i] + " " + input.substr(i+1);
		i += 2;
	}
	
	queue<string> tokens = tokenize(input," ");
	Node *root = new Node(tokens);
	assert(tokens.empty());
	int q = readInt();
	
	while(q--){
		set<string> featureList;
		string animal = readString();
		int numFeatures = readInt();
		while(numFeatures--) 
			featureList.insert(readString());
		double ret = root -> getProb(featureList);
		printf("%.7f\n",ret);
	}
}


main()
{
	globalInit();
	int cases = readInt();
	int tc = 0;
	while(cases--){
		tc++;
		printf("Case #%d:\n",tc);
		tcInit();
		solve();
		tcEnd();
	}
}

void tcEnd(){
}


