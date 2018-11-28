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


int main(int argc, char* argv[])
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int mx = 200;  
	char line[200];
	fin.getline(line, mx);
	int noc = to<int>(string(line));
	for(int i = 1; i <= noc; i ++) {
		string num;
		getline(fin, num);
		int nm = to<int>(num);
		string a, b;
		getline(fin, a);
		getline(fin, b);
		vector<int> aa = vs2vi(split(a, ' '));
		vector<int> bb = vs2vi(split(b, ' '));
		sort(aa.begin(), aa.end());
		sort(bb.begin(), bb.end());
		vector<long long> ax(aa.begin(), aa.end());
		vector<long long> bx(bb.begin(), bb.end());

		long long r = 0;
		for(int j = 0; j < ax.size(); j ++) {
			r += ax[j] * bx[nm - j - 1];
		}
		fout<<"Case #"<<i<<": "<<r<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

