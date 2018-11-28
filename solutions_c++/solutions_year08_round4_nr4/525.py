#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <utility>
#include <algorithm>
#include <fstream>

using namespace std;

string itoa(int val) {stringstream ss;ss << val;return ss.str();}
typedef vector<int> vi;
typedef pair<int,int> pi;
vi parseInt(string s) {stringstream ss(s);vi ans;while (!ss.eof()) {int temp; ss >> temp; ans.push_back(temp); } return ans;}
#define COPY(x,y) y.resize(x.size());copy(x.begin(),x.end(),y.begin())
#define pb push_back
#define SWAP(t,x,y) t temp=x;x=y;y=temp;
#define ll long long

string str;
string str2;
int k;
int x[10];
bool used[10];
int best;

void calc() {
	str2 = str;
	for(int i=0;i<str.size();i+=k) {
		for(int j=0;j<k;j++) {
			str2[i+j] = str[i+x[j]-1];
		}
	}
	int ans = 0;
	for(int i=1;i<str2.size();i++) {
		if (str2[i]!=str2[i-1]) ans++;
	}
	if (ans<best)
		best = ans;
}

void perm(int pos) {
	if (pos==k) {
		calc();
		return;
	}
	for(int i=1;i<=k;i++) {
		if (!used[i]) {
			used[i] = true;
			x[pos] = i;
			perm(pos+1);
			used[i] = false;
		}
	}
}

int main() {
	int testcases;
	cin >> testcases;
	for(int i=1;i<=testcases;i++) {
		best = 1000000000;
		cin >> k;
		cin >> str;
		memset(used,0,sizeof(used));
		perm(0);
		cout << "Case #" << i << ": " << best+1 << endl;
	}
	return 0;
}
