
/* Aishvarya Vishvesh
   Singh */

#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<vector>
#include<cstring>
#include<stack>
#include<sstream>

using namespace std;

int ans;
int dig;
string a,b;

bool check(string cp) {
	if (cp[0]=='0')
		return false;
	int ind=0;
	int flag1=0;
	while (ind<dig) {
		if (cp[ind]<b[ind]) {
			flag1=1;
			break;
		}
		if (cp[ind]>b[ind])
			return false;
		ind++;
	}
	flag1=1;
	ind=0;
	while (ind<dig) {
		if (cp[ind]>a[ind]) {
			if (flag1)
				return true;
		}
		if (cp[ind]<a[ind])
			return false;
		ind++;
	}
	return true;
}

int func(string cur) {
	int res=0;
	string cp=cur;
	cp=cp+cp[0];
	cp.erase(0,1);
	while (cp!=cur) {
		if (check(cp) && cp!=cur)
			res++;
		cp=cp+cp[0];
		cp.erase(0,1);
	}
	return res;
}

int main() {
	int t;
	cin >> t;
	for (int cas=1;cas<=t;cas++) {
		cin >> a >> b;
		dig=a.size();
		ans=0;
		string cur=a;
		while (cur!=b) {
			ans+=func(cur);
			for (int i=dig-1;i>=0;i--) {
				if (cur[i]!='9') {
					cur[i]++;
					break;
				}
				else {
					while (cur[i]=='9') {
						cur[i]='0';
						i--;
					}
					cur[i]++;
					break;
				}
			}
		}
		ans+=func(cur);
		cout << "Case #" << cas << ": " << ans/2 << endl;
	}
	return 0;
}
