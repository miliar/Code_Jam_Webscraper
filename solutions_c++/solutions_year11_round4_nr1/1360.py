#ifndef _INCLUDED_
#define _INCLUDED_
#include __FILE__ // all the defines, and functions declarations, are bellow

typedef struct {
	double B, E, s;
} walkway;

input(walkway, w){
	return i >> w.B >> w.E >> w.s;
}

output(walkway, w){
	return o << "{" << w.B << "," << w.E << "," << w.s << "}";
}

double getTime(double d, double s1, double ts1, double s2){
	if(ts1 < 0) ts1 = 0;
	if(d/s1 < ts1)
		return d/s1;
	return ts1 + ( d - ts1*s1 )/s2;
}

bool comp(walkway a, walkway b){
	return a.s < b.s;
}

void solveCase(){
	double X, S, R, t;
	int N;
	cin >> X >> S >> R >> t >> N;
	vector<walkway> W;
	
	walkway w0, w1;
	For(n, 0, N){
		if(n==0) w0.E = 0;
		
		cin >> w1;
		
		// the middle path
		walkway p;
		p.B = w0.E;
		p.E = w1.B;
		p.s = 0;
		
		// insert the middle path and the walkway
		W.pb(p);
		W.pb(w1);
		
		w0 = w1;
	}
	// the last path
	w1.B = w0.E;
	w1.E = X;
	w1.s = 0;
	W.pb(w1);
	
	sort(all(W), comp);
	
	double totalTime = 0;
	For(n, 0, W.size()){
		double lt = getTime(W[n].E - W[n].B, R+W[n].s, t, S+W[n].s);
		t -= lt; if(t < 0) t = 0;
		totalTime += lt;
	}
	
	cout << abserr(7) << totalTime << endl;
}

int main(void){
	for1(t,get(int)){
		cout << "Case #" << t << ": ";
		cerr << "Case #" << t << endl;
		solveCase();
	}
	return 0;
}

#else // all the defines, and functions declarations, are here
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
#define get(type) get_<type>()
#define abserr(n) setprecision(n) << fixed << showpoint
#define For(n,s,e) for(size_t n=(s), end__=(e); n<end__; n++)
#define forall(n,N) For(n,0,N)
#define for1(n,N) For(n,1,N+1)
#define foreach(it,v) for(auto it=v.begin(); it!=v.end(); it++)
#define all(v) v.begin(), v.end()
#define has(v,d) (find(v,d) != v.end())
#define ifhas(v,d,r) auto r=find(v,d); if(r != v.end())
#define abs(n) ((n)>=0?(n):-(n))
#define pb push_back
#define input(T, x) istream &operator>>(istream &i, T &x)
#define output(T, x) ostream &operator<<(ostream &o, const T &x)
string &trim(string &s) {
	auto p=s.size();
	for(p=0; p<s.size() && isspace(s[p]); p++); s.erase(0,p);
	for(p=s.size(); p>0 && isspace(s[p]); p--); s.erase(p);
	return s;
}
string getline(istream &i=cin){string s;while(trim(s)=="") getline(i,s);return s;}
template <class T> T get_(istream &i=cin){ T tmp; i >> tmp; return tmp; }
template <class T> T &sort(T &v){ sort(all(v)); return v; }
template <class T1, class T2> typename T1::iterator find(T1 &v, T2 &d){
	return find(all(v),d);
}
template <class T> ostream &operator<<(ostream &o, const vector<T> &v){
	o << "["; forall(n, v.size()) o << (n?", ":"") << v[n]; return o << "]";
}
template <class T> ostream &operator<<(ostream &o, const vector< vector<T> > &v){
	foreach(it, v) o << *it << endl; return o;
}
template <class T> istream &operator>>(istream &i, vector<T> &v){
	T t; if(v.size()) foreach(e, v) i >> *e;
	     else for(stringstream l(getline(i)); l >> t; v.pb(t));
	     return i;
}
#endif
