#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
typedef vector<int>::iterator VIp;

#define pi acos(-1.)
#define eps 1e-7

int main(){
	char fname[]="C:\\Documents and Settings\\A-large.in";
	//char fname[]="C:\\Documents and Settings\\A-small2.in";
	//char fname[]="C:\\Documents and Settings\\inputA.txt";
	ifstream fin(fname);	
	if(!fin){
		cout << "Error.Can't open input data file."<< endl;
		exit(1);
	}

	int N,Sn,Qn;
	string S[100];
	string Q;
	string tmp;
	int ch[100];
	int ct;
	int ans;

	getline(fin,tmp);
	N=atoi(tmp.c_str());
	REP(x,N){
		getline(fin,tmp);
		Sn=atoi(tmp.c_str());
		CLEAR(S,0x00);
		REP(i,Sn){
			getline(fin,S[i]);
		}
		getline(fin,tmp);
		Qn=atoi(tmp.c_str());
		ct=0;
		ans=0;
		CLEAR(ch,0x00);
		if(Qn!=0){
			REP(k,Qn){
				getline(fin,Q);
				REP(j,Sn){
					if(Q==S[j]){
						if(ch[j]!=1){
							if(ct==Sn-1){
								CLEAR(ch,0x00);
								ct=0;
								ans++;
							}
							ch[j]=1;
							ct++;	
						}
						break;
					}
				}
			}
		}
		cout<<"Case #"<< x+1 <<": ";
		cout<< ans <<endl;
	}
	return 0;	
}
