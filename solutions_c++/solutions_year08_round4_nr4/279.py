#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>


using namespace std;



int m[6],p[6],best;

string s;

string uppl(string s,int k){
	string ss = s;

	for (int i = 0;i < k; ++i)
		ss[i] = s[p[i]];
	return ss;
}

int calc(int k){
	string res;
	
	int i=0;

	while (i < s.size()){			
		res += uppl(s.substr(i,k),k);
		i += k;
	}

	int ans = 1;
	
	for (int i = 1;i < res.size(); ++i)
		if (res[i] != res[i-1])
			++ans;
	return ans;
}

void rec(int i,int n){
	if (i >= n) {
		best = min(best,calc(n));		
		return;
	}
	for (int j = 0;j < n; ++j)
		if (m[j] == 0){
			m[j] = 1;
			p[i] = j;
			rec(i+1,n);
			m[j] = 0;
		}	
}


int solve(string s,int k){
	best = s.size();

	memset(m,0,sizeof(m));
	rec(0,k);
	return best;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int test;
	cin >> test;

	for (int t = 1;t <= test; ++t){
		int k;
		cin >> k;		
		cin >> s;
		best = s.size()+10;
		cout << "Case #"<<t<<": "<< solve(s,k) <<endl;	
	}

	return 0;
}