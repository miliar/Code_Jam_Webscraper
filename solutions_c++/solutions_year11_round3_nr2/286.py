#include <vector>
#include <list>
#include <map>
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

typedef long long huge;
inline string getline();
template <typename T> inline T get(istream &is = cin);
template <typename T> inline ostream &operator<<(ostream &os, const vector<T> &v);
template <typename T> inline istream &operator>>(istream &is, vector<T> &v);
#define read(type) get<type>()
#define abserr(n) setprecision(n) << fixed << showpoint
#define forall(n,N) for(size_t n=0, end__=(N); n<end__; n++)
#define foreach(it,v) for(auto it=v.begin(), end__=v.end(); it!=end__; it++)

bool comp(const int &h1, const int &h2){
	return h1 > h2;
}

void solveCase(){
	huge L = read(huge), t = read(huge), N = read(huge), C = read(huge);
	vector<huge> D(C); vector<int> S(N);
	
	cin >> D;
	
	foreach(d,D) *d *= 2;
	
	huge acctime = 0;
	forall(n, N){
		int delta = D[n%C];
		acctime += delta;
		if(acctime >= t){
			if(n == 0 || acctime - delta <= t){
				S[n] = acctime - t;
			}else{
				S[n] = delta;
			}
		}else{
			S[n] = 0;
		}
	}
	
	sort(S.begin(), S.end(), comp);
	
	huge saved = 0;
	for(int n=0; n<N && L; n++, L--)
		saved += S[n];
	
	cout << (acctime - saved / 2) << endl;
}

int main(int argc, char *argv[]){
	stringstream line(getline());
	unsigned int T;
	line >> T;
	forall(t, T){
		cout << "Case #" << t+1 << ": ";
		cerr << "Case #" << t+1 << endl;
		solveCase();
	}
	return 0;
}
inline string getline(){
	string tmp; getline(cin, tmp); return tmp;
}
template <typename T>
inline T get(istream &is){
	T tmp; is >> tmp; return tmp;
}
template <typename T>
inline ostream &operator<<(ostream &os, const vector<T> &v){
	forall(n, v.size()) os << (n?", ":"[") << v[n]; return os << "]";
}
template <typename T>
inline istream &operator>>(istream &is, vector<T> &v){
	foreach(e, v) is >> *e; return is;
}
