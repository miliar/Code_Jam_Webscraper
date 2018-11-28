#include <sstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <numeric>
#include <bitset>
#include <fstream>
using namespace std;
long long gcd(long long a,long long b){if(a<b)swap(a,b);if(a%b==0) return b;return gcd(a%b,b);};
vector<string> split(string a,char c){int st=0;string t;vector<string> r;a.push_back(c);for(int i=0;i<a.size();i++){
if(a[i]==c){r.push_back(t);t=string();st=i+1;}else{t.push_back(a[i]);}}return r;};
template<class Ty,class Tx> Ty to(Tx x){Ty y;stringstream ss("");ss<<x;ss.seekg(0);ss>>y;return y;};
template<class Ty,class Tx> vector<Ty> to(vector<Tx> x) {vector<Ty> r;for(int i=0;i<x.size();i++)r.push_back(to<Ty>(x[i]));return r;};
vector<int> vs2vi(vector<string> v){vector<int> r;for(int i=0;i<v.size();i++)if(v[i].size()>0)r.push_back(to<int>(v[i]));return r;};
bool isleap(int y){return!(y%4)&&(y%100)||!(y%400);};

int gate[10002];
int able[10002];
int bt[10002][2];

int ct(string k) {
	int r = 1;
	for(int i = 1; i < k.size(); i ++) {
		if(k[i] != k[i - 1]) r ++;
	}
	return r;
};

int main(int argc, char* argv[])
{
	ifstream fin("D-small.in");
	ofstream fout("D-small.out");
	int mx = 200;  
	char line[200];
	fin.getline(line, mx);
	int noc = to<int>(string(line));
	for(int i = 1; i <= noc; i ++) {
		string kk;
		getline(fin, kk);
		int k = to<int>(kk);
		string ss;
		getline(fin, ss);
		vector<int> e(k, 0);
		for(int j = 0; j < k; j ++)
			e[j] = j;
		sort(e.begin(), e.end());
		int r = ss.size();
		do {
			string sp = ss;
			for(int j = 0; j < sp.size(); j += k) {
				string st = sp.substr(j, k);
				for(int m = 0; m < k; m ++) {
					sp[j + m] = st[e[m]];
				}
			}
			r = min(r, ct(sp));
		}while(next_permutation(e.begin(), e.end()));
		fout<<"Case #"<<i<<": "<<r<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

