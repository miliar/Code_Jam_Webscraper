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
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");
	int mx = 200;  
	char line[200];
	fin.getline(line, mx);
	int noc = to<int>(string(line));
	for(int i = 1; i <= noc; i ++) {
		string kk;
		getline(fin, kk);
		vector<int> t = vs2vi(split(kk, ' '));
		int N = t[0];
		int M = t[1];
		int A = t[2];
		vector<pair<int, int> > vm;
		vm.push_back(make_pair(0, 0));
		vm.push_back(make_pair(0, M));
		vm.push_back(make_pair(N, 0));
		vm.push_back(make_pair(N, M));
		int r = (N + 1) * (M + 1);
		int bl = false;
		for(int j = 0; (!bl) && (j < r); j ++)
			for(int s = j + 1; (!bl) && (s < r); s ++) {
				for(int m = 0; (!bl) && (m < 4); m ++) {
					int x1 = vm[m].first;
					int y1 = vm[m].second;
					int x2 = j / (M + 1);
					int y2 = j % (M + 1);
					int x3 = s / (M + 1);
					int y3 = s % (M + 1);
					int ar = -x2 * y1 + x3 * y1 + x1 * y2 - x3 * y2 - x1 * y3 + x2 * y3;
					ar = abs(ar);
					if(ar == A) {
						fout<<"Case #"<<i<<": "<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<' '<<x3<<' '<<y3<<endl;
						bl = true;
						break;
					}
				}
			}
			if(!bl) {
				fout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
			}
	}
	fin.close();
	fout.close();
	return 0;
}

