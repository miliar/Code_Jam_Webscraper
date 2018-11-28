#include<vector>
#include<string>
#include<map>
#include<set>
#include<utility>
#include<algorithm>
#include<cmath>
#include<iostream>
#include<cstdio>

using namespace std;

#define FOR(A,B) for(int A;A<B.size();++A)
#define X first
#define Y second
#define LI size()-1
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tt=0;tt<t;++tt){
		int n,l,h;
		cin >> n >> l >> h;
		vector<int> s(n);
		for(int i=0;i<n;++i){
			cin >> s[i];
		}
		sort(s.begin(),s.end());
		bool ok=true;
		int res=0;
		for(int i=l;i<=h;++i){
			ok = true;
			for(int j=0;j<s.size() && ok;++j){
				if ( i % s[j] !=0 && s[j] % i !=0) ok = false;
			}
			if (ok){
				res=i;
				break;
			}
		}
		cout << "Case #"<< tt+1 << ": ";
		if(ok){
			cout << res << endl;
		} else {
			cout << "NO" << endl;	
		}
	}
	return 0;
}