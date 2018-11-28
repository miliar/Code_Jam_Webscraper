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

void solveCase(){
	int N = read(int), L = read(int), H = read(int);
	vector<int> O(N);
	
	cin >> O;
	
	for(int f=L; f<=H; f++){
		int n;
		for(n=0;n<N;n++){
			if(f%O[n] && O[n]%f)
				break;
		}
		if(n==N){
			cout << f << endl;
			return;
		}
	}
	cout << "NO" << endl;
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
