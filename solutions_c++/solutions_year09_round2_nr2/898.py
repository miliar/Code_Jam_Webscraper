#include <iostream>
#include <algorithm>
#include <string>
#include <numeric>

using namespace std;

inline bool sort_pred(char l, char r){
	if (l == '0') l = '9'+1;
	if (r == '0') r = '9'+1;
	return (l<r);
}

int main(){
	freopen("readme.txt", "r", stdin);
	freopen("out", "w", stdout);

	string s,sout;
	int T;
	cin >>T;
	for (int i = 1; i<=T; ++i){
		cin >>s;
		cout <<"Case #"<<i<<": ";
		if (next_permutation(s.begin(), s.end() )){
			cout <<s<<endl;	
		} else {
			sort(s.begin(), s.end(), sort_pred);
			cout <<s[0];
			sort(s.begin()+1, s.end());
			//minn = *lower_bound(s.begin(), s.end(), '0');
			cout <<0<<s.substr(1)<<endl;
		}
	}
}