#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;

int i,j,k,T;

bool intersect(int x1,int x2,int y1,int y2) {
	if (x2>=x1) {
		if (y2<x2 && y1>x1) return true;
	}
	if (x1>x2) {
		if (y1<x1 && y2>x2) return true;
	}
	return false;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin >> T;
	for (int ii=0;ii<T;ii++) {
		int n;
		cin >> n;
		vector<pair<int,int> > z;
		for (i=0;i<n;i++) {
			int num1,num2;
			cin >> num1 >> num2;
			z.push_back(make_pair(num1,num2));
		}
		int res=0;
		for (i=0;i<n;i++) {
			for (j=i+1;j<n;j++)
				if (intersect(z[i].first,z[i].second,z[j].first,z[j].second) || intersect(z[j].first,z[j].second,z[i].first,z[i].second)) res++;
		}
		cout << "Case #" << ii+1 << ": " << res << endl;
	}
	return 0;
}
