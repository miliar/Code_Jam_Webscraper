#include	<iostream>
#include	<cstring>
#include	<vector>
#include	<numeric>
using namespace std;

#define		ArrSize		1000

int main(){
	int i, j, temp, l, ll, lt, m;
	int t, r, k, n;
	int gi[ArrSize];
	vector <int> loc, val;
	int result;
	cin >> t;
	for(i = 1; i <= t; ++i){
		cin >> r >> k >> n;
		memset(gi, 0, sizeof(gi));
		loc.clear();
		val.clear();
		for(j = 0; j < n; ++j)
			cin >> gi[j];
		result = 0;
		l = 0;
		for(j = 0; j < r; ++j){
			temp = 0;
			ll = l;
			while(temp <= k){
				temp += gi[l++];
				if(l >= n)
					l %= n;
				if(ll == l)
					break;
			}
			if(temp > k){				
				--l;
				if(l < 0)
					l = n - 1;
				temp -= gi[l];
			}
			lt = -1;
			for(m = 0; m < loc.size(); ++m)
				if(loc.at(m) == ll){
					lt = m;
					break;
				}
			
			if( -1 == lt){
				loc.push_back(ll);
				val.push_back(temp);
			}
			else
				break;
		}	
		if(j == r){
			result = accumulate(val.begin(), val.end(), 0);
		}
		else{
			result += accumulate(val.begin(), val.begin() + lt, 0);
			l = val.size() - lt;
			temp = (r - lt) / l;
			result += temp * accumulate(val.begin() + lt, val.end(), 0);
			temp = (r - lt) % l;
			result += accumulate(val.begin() + lt, val.begin() + lt + temp, 0);
		}
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}
