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

int vis[200][200];
int mp[200][200];
int hh;
int ww;

int get(int x, int y) {
	if((x <= 0)) return 0;
	if((y <= 0)) return 0;
	if((x == 1) && (y == 1)) return 1;
	if(mp[x][y] == 1) return 0;
	if(vis[x][y] != -1) return vis[x][y];
	int r = get(x - 1, y - 2)+ get(x - 2, y - 1);
	r %= 10007;
	return vis[x][y] = r;
};

int main(int argc, char* argv[])
{
	ifstream fin("A.in");
	ofstream fout("A.out");
	int mx = 200;  
	char line[200];
	fin.getline(line, mx);
	int noc = to<int>(string(line));
	for(int i = 1; i <= noc; i ++) {
		string kk;
		getline(fin, kk);
		vector<int> t = vs2vi(split(kk, ' '));
		memset(vis, -1, sizeof(vis));
		memset(mp, 0, sizeof(mp));
		hh = t[0];
		ww = t[1];
		for(int j = 0; j < t[2]; j ++) {
			string hole;
			getline(fin, hole);
			vector<int> hs = vs2vi(split(hole, ' '));
			mp[hs[0]][hs[1]] = 1;
		}
		int r = get(t[0], t[1]);
		fout<<"Case #"<<i<<": "<<r<<endl;
		
			//		if(ar == A) {
			//			fout<<"Case #"<<i<<": "<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<' '<<x3<<' '<<y3<<endl;
			//			bl = true;
			//			break;
			//		}
			//	}
			//}
			//if(!bl) {
			//}
	}
	fin.close();
	fout.close();
	return 0;
}


