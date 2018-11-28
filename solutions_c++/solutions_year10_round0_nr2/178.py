#define _USE_MATH_DEFINES
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <list>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <numeric>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

string mlsub(string a, string b) {
	string result;
	int bor=0;
	int maxl, minl;
	int ad, bd, tail;

	if(a.size()<b.size() || (a.size()==b.size() && a<b) || a==b) return string("0");
	maxl=a.size(); minl=b.size();
	b=string(maxl-minl, '0')+b;
	for(int i=maxl-1; i>=0; i--) {
		ad=a[i]-'0'-bor; bd=b[i]-'0';
		ad-=bd;
		if(ad<0) {ad+=10; bor=1;}
		else bor=0;
		result.push_back('0'+ad);
	}
	tail=maxl-1;
	while(result[tail]=='0' && tail>0) tail--;
	result.erase(tail+1);
	reverse(result.begin(), result.end());

	return result;
}

string mlmul(string a, string b) {
	string result;
	int al, bl;
	int ad, bd;
	string one("1"), zero("0");
	vector <int> ri;

	if(a==zero || b==zero) return zero;
	if(a==one) return b;
	if(b==one) return a;
	al=a.size(); bl=b.size();
	ri.assign(al+bl, 0);
	for(int i=al-1; i>=0; i--) {
		for(int j=bl-1; j>=0; j--) {
			ad=a[i]-'0'; bd=b[j]-'0';
			ri[(al-1-i)+(bl-1-j)]+=ad*bd;
		}
	}
	for(int i=0; i<al+bl-1; i++) {
		ri[i+1]+=ri[i]/10;
		ri[i]%=10;
	}
	bool flag=false;
	for(int i=al+bl-1; i>=0; i--) {
		if(ri[i]>0) flag=true;
		if(flag) result.push_back('0'+ri[i]);
	}
	return result;
}

string mldiv(string a, string b) {
	string result;
	string aa, tmp;
	stringstream ss;
	int bor=0;
	int maxl, minl;
	int ad, bd, q, head;

	head=0;
	while(b[head]=='0') {
		head++;
		if(head==b.size()) return string("");
	}
	if(head>0) b=b.substr(head);

	if(a.size()<b.size() || (a.size()==b.size() && a<b)) return string("0");
	maxl=a.size(); minl=b.size();
	for(int i=0; i<=maxl-minl; i++) {
		ad=a[i]-'0'; bd=b[0]-'0';
		if(i>0 && a[i-1]>'0') {ad+=(a[i-1]-'0')*10; aa=a.substr(i-1, minl+1);}
		else aa=a.substr(i, minl);
		if(aa.size()<b.size() || (aa.size()==b.size() && aa<b)) {
			if(!result.empty()) result.push_back('0'); continue;
		}
		q=min(9, ad/bd);
		ss.str(""); ss.clear(); ss << q;
		tmp=mlmul(b, ss.str());
		while(aa.size()<tmp.size() || (aa.size()==tmp.size() && aa<tmp)) {
			q--;
			ss.str(""); ss.clear(); ss << q;
			tmp=mlmul(b, ss.str());
		}
		tmp+=string(maxl-minl-i, '0');
		a=mlsub(a, tmp); a=string(maxl-a.size(), '0')+a;
		result.push_back('0'+q);
	}
	return result;
}

string mlmod(string a, string b) {
	string tmp;

	tmp=mldiv(a, b);
	if(tmp.empty()) return tmp;
	return mlsub(a, mlmul(tmp, b));
}

string mlgcd(string a, string b) {
	string x, y, tmp;

	x=a; y=b;
	while(y!=string("0")) {
		x=mlmod(x, y);
		tmp=x; x=y; y=tmp;
	}

	return x;
}

struct lessstr : public binary_function <string, string, bool> {
	bool operator() (const string a, const string b) {
		return (a.size()<b.size() || (a.size()==b.size() && a<b));
	}
};

class GCJ {
public:
	string solve(vector <string> vs) {
		string result, s;
		vector <string> vss;
		string gcds;
		
		sort(vs.begin(), vs.end(), lessstr());
		for(int i=1; i<(int)vs.size(); i++) {
			s=mlsub(vs[i], vs[i-1]);
			if(s!=string("0")) vss.push_back(s);
		}
		gcds=vss[0];
		for(int i=1; i<(int)vss.size(); i++) {
			gcds=mlgcd(gcds, vss[i]);
		}
		result=mlmod(vs[0], gcds);
		if(result==string("0")) result=string("0");
		else result=mlsub(gcds, result);

		return result;
	}
};

int main() {
	string prb[12];
	ofstream ofs("output.txt");
	string s, filename;
	char key;
	int n, k;
	GCJ gcj;
	vector <string> vs;

	for(int i=0; i<12; i++) {
		prb[i].push_back('A'+i/2);
		if(i%2) prb[i]+="-large";
		else prb[i]+="-small-attempt";
		prb[i]+=".in.txt";
		cout << (char)('a'+i) << ". " << prb[i] << endl;
	}
	do {
		cout << "Choose the input file." << endl;
		cin >> key;
	} while(key-'a'<0 || key-'a'>=12);
	filename=prb[key-'a'];
	if((key-'a'+1)&1) {
		do {
			cout << "Choose number of attempt times." << endl;
			cin >> key;
		} while(key-'0'<0 || key-'9'>0);
		filename.insert(15, 1, key);
	}
	cout << "Filename is " << filename << endl;
	ifstream ifs(filename.c_str());

	ifs >> n; ifs.ignore();
	for(int i=1; i<=n; i++) {
		ifs >> k; vs.clear();
		for(int j=0; j<k; j++) {
			ifs >> s;
			vs.push_back(s);
		}
		ofs << "Case #" << i << ": " << gcj.solve(vs) << endl;
	}
}
