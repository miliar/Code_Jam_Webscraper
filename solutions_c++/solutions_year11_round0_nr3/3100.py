#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out","w",stdout);
	int tests,i,cur,n,j,k;
	cin >> tests;
	vector<int> v;
	int res,max;
	for(i=1;i<=tests;i++){
		v.clear();
		max=0;
		cin >> n;
		for(j=0;j<n;j++){
			if(j==0){
				cin >> res;
				v.push_back(res);
			}
			else{
				cin >> cur;
				v.push_back(cur);
			}
			if(j!=0) res=res^cur;
		}
		if(res!=0) cout << "Case #" << i <<": NO" << endl;
		else{
			sort(v.begin(),v.end());
			for(k=1;k<v.size();k++){
				max+=v[k];
			}
			cout << "Case #" << i << ": " <<max << endl;
		}
	}
	return 0;
}