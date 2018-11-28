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

int get(int a, int tar) {
	if(bt[a][tar] != -1) return bt[a][tar];
	int res = 1000000;
	if(able[a] == 0) {
		if(tar == 0) {
			if(gate[a] == 0) {
				res = min(res, get(a * 2, 0) + get(a * 2 + 1, 0));
			} else {
				res = min(res, min(get(a * 2, 0), get(a * 2 + 1, 0)));
			}
		} else {
			if(gate[a] == 0) {
				res = min(res, min(get(a * 2, 1), get(a * 2 + 1, 1)));
			} else {
				res = min(res, get(a * 2, 1) + get(a * 2 + 1, 1));
			}
		}
	} else {
		if(tar == 0) {
			if(gate[a] == 0) {
				res = min(res, get(a * 2, 0) + get(a * 2 + 1, 0));
				res = min(res, 1 + min(get(a * 2, 0), get(a * 2 + 1, 0)));
			} else {
				res = min(res, get(a * 2, 0) + get(a * 2 + 1, 0) + 1);
				res = min(res, min(get(a * 2, 0), get(a * 2 + 1, 0)));
			}
		} else {
			if(gate[a] == 0) {
				res = min(res, get(a * 2, 1) + get(a * 2 + 1, 1) + 1);
				res = min(res, min(get(a * 2, 1), get(a * 2 + 1, 1)));
			} else {
				res = min(res, get(a * 2, 1) + get(a * 2 + 1, 1));
				res = min(res, 1 + min(get(a * 2, 1), get(a * 2 + 1, 1)));
			}
		}
	}
	return bt[a][tar] = res;
};

int total;

int main(int argc, char* argv[])
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int mx = 200;  
	char line[200];
	fin.getline(line, mx);
	int noc = to<int>(string(line));
	for(int i = 1; i <= noc; i ++) {
		memset(gate, -1, sizeof(gate));
		memset(able, -1, sizeof(able));
		memset(bt, -1, sizeof(bt));
		string num;
		getline(fin, num);
		vector<int> t = vs2vi(split(num, ' '));
		total = t[0];
		for(int j = 1; j <= (total - 1) / 2; j ++) {
			string e;
			getline(fin, e);
			vector<int> ee = vs2vi(split(e, ' '));
			gate[j] = ee[0];
			able[j] = ee[1];
		}
		for(int j = (total - 1) / 2 + 1; j <= total; j ++) {
			string e;
			getline(fin, e);
			int ee = to<int>(e);
			if(ee == 0) {
				bt[j][0] = 0;
				bt[j][1] = 1000000;
			} else {
				bt[j][1] = 0;
				bt[j][0] = 1000000;
			}
		}
		int res = get(1, t[1]);
		if(res >= 1000000) {
			fout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		} else {
			fout<<"Case #"<<i<<": "<<res<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}

