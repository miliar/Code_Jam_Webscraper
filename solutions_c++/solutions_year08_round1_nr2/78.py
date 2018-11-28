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
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int mx = 200;  
	char line[200];
	fin.getline(line, mx);
	int noc = to<int>(string(line));
	for(int i = 1; i <= noc; i ++) {
		string num;
		getline(fin, num);
		int flavor = to<int>(num);
		string cust;
		getline(fin, cust);
		int customer = to<int>(cust);
		vector<int> fla(customer + 1, 0);
		vector<vector<int> > nof(customer + 1, vector<int>());
		for(int j = 0; j < customer; j ++) {
			string tmp;
			getline(fin, tmp);
			vector<int> tp = vs2vi(split(tmp, ' '));
			for(int k = 0; k < tp[0]; k ++) {
				if(tp[k * 2 + 2] == 0) {
					nof[j + 1].push_back(tp[k * 2 + 1]);
				} else {
					fla[j + 1] = tp[k * 2 + 1];
				}
			}
		}
		vector<int> res(flavor, 0);
		fla.erase(fla.begin());
		nof.erase(nof.begin());
		set<int> hb;
		while(true) {
			set<int> cs;
			for(int j = 0; j < customer; j ++) {
				if((fla[j] != 0) && (nof[j].size() == 0)) {
					cs.insert(fla[j]);	
				}
			}
			for(int j = 0; j < customer; j ++) {
				for(int k = (int) nof[j].size() - 1; k >= 0; k --) {
					if(cs.find(nof[j][k]) != cs.end()) {
						nof[j].erase(nof[j].begin() + k);
					}
				}
			}
			int sz = hb.size();
			hb.insert(cs.begin(), cs.end());
			if(hb.size() == sz) break;
		}
		vector<int> kk(hb.begin(), hb.end());
		for(int j = 0; j < kk.size(); j ++)
		res[kk[j] - 1] = 1;
		bool bl = false;
		for(int j = 0; j < customer;j ++) {
			if(fla[j] == 0) {
				bool bk = false;
				for(int k = 0; k < nof[j].size(); k ++) {
					if(hb.find(nof[j][k]) == hb.end()) {
						bk = true;
						break;
					}
				}
				if(!bk) {
					bl = true;
					break;
				}
			}
		}
		if(bl) {
			fout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		} else {
			fout<<"Case #"<<i<<": ";
			for(int j = 0; j < res.size(); j ++) {
				fout<<res[j];
				if(j != (int) res.size() - 1) {
					fout<<' ';
				}
			}
			fout<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}

