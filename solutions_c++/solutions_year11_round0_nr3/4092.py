#include <cstdio>
#include <vector>
#include <set>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int t,a,n,res;
	bool b;
	scanf("%d",&t);
	for (int q=1; q<=t; q++) {
		scanf("%d",&n);
		vector<int> v;
		for (int i=0; i<n; i++) {
			scanf("%d",&a);
			v.push_back(a);
		}
		res=0;
		for (int i = 1; i < (1 << v.size()); ++i) {
			vector<int> left, right;
			for (int j = 0; j < v.size(); ++j) {
				if ((i >> j) & 1)
					left.push_back(v[j]);
				else
					right.push_back(v[j]);
			}
			if (left.size()==0||right.size()==0) continue;
			int s1=0,s2=0;
			for (int i=0; i<left.size(); i++) s1^=left[i];
			for (int i=0; i<right.size(); i++) s2^=right[i];
			if (s1==s2) {
				s1=0,s2=0;
				for (int i=0; i<left.size(); i++) s1+=left[i];
				for (int i=0; i<right.size(); i++) s2+=right[i];
				if (res<max(s1,s2)) res=max(s1,s2);
			}

		}
		if (res==0) {
			printf("Case #%d: NO\n",q);
		} else {
			printf("Case #%d: %d\n",q,res);
		}
	}
}