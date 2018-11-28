#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <queue>
#include <sstream>
using namespace std;
int t;
string i2s(int x){
	stringstream ss;
	ss << x;
	return ss.str();
}
int s2i(string str){
	stringstream ss (str);
	int res;
	ss>>res;
	return res;
}
int gg;
void rec(int a) {
	if (a==1) gg++; 
	if (a<2)return;
	gg++;
	int fp;
	if ((a-1)%2) fp=(a-1)/2+1; else fp=(a-1)/2;
	rec(fp);
}
int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin >> t;
	for (int c=0;c<t;c++) {
		int l,p,C;
		cin >> l >> p >> C;
		vector <int> v;
		v.push_back(C*l);
		int res=0;
		if (v.back()<p) {
			int nb=1;
			while (v.back()<p) {
				v.push_back(v.back()*C);
				nb++;
			}
			//cout << v.size();
			gg=0;
			rec(v.size()-1);
			res=gg;
			if (c==3) {
			int fff=666;
			}
		}
		cout << "Case #" << c+1 << ": ";
		cout << res;
		cout << endl;
	}
}