#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std ;
int f(vector<int> &p , string &s){
	string s2 = s ;
	for(int i = 0 ; i < s.size() ; i++){
		int a , b ;
		a = i % p.size() ;
		b = i - a ;
		s2[i] = s[b + p[a]] ;
	}

	char c = s2[0] ;
	int x = 0 ;
	int len = 0 ;
	for(int i = 0 ; i < s2.size() ; i++){
		if(s2[i] == c) x++ ;
		else{
			len++ ;
		//	if(x != 1) len ++ ;
		//	while(x /= 10) len++ ;
			c = s2[i] ; x = 1 ;
		}
	}
	len++ ;
	//if(x != 1) len++ ;
	//while(x/= 10) len++ ;
	//cout << s2 << ' ' << len << endl ;
	return len ;
}

int main(){
	int tc ;
	cin >> tc ;
	for(int t = 1 ; t <= tc ; t++){
		int k ;
		string s , s2;
		cin >> k >> s ;
		vector<int> p(k) ;
		for(int i = 0 ; i < k ; i++){
			p[i] = i ;
		}
		int minv = f(p,s) ;
		while(next_permutation(p.begin(),p.end())){
			minv <?= f(p,s) ;
		}
		cout << "Case #" << t << ": " ;
		cout << minv << endl ;
	}
}
