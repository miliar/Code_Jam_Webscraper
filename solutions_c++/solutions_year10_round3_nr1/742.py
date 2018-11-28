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
typedef pair<int,int> ii;
int cmp(ii a,ii b) {
	return a.second<b.second;
}
int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin >> t;
	for (int c=0;c<t;c++) {
		int n;
		cin >> n;
		vector <ii> v,b;
		int aa,bb;
		for (int i=0;i<n;i++) {
			scanf("%d %d",&aa,&bb);
			v.push_back(ii(aa,bb));
		}
		int res=0;
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				if (v[i].first>v[j].first && v[i].second<v[j].second) res++;
				if (v[i].first<v[j].first && v[i].second>v[j].second) res++;
			}
		}
		cout << "Case #" << c+1 << ": ";
		cout << res/2;
		cout << endl;
	}
}