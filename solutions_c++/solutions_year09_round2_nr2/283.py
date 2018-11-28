#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <queue>
#include <algorithm>
#include <list>
#include <sstream>

using namespace std;

#define f(i,j,k) for(int i = j; i < k; i++)
#define fd(i,j,k) for(int i = j; i >= k; i--)
#define pb push_back
#define sz size
#define all(a) (a).begin(), (a).end()
#define vs vector<string>
#define vi vector<int>

template <typename T>
void printv(vector<T>& v){
	int n = v.sz();
	printf("[");
	for(int i = 0; i < n; i++){
		cout << v[i] << ", ";
	}
	printf("]\n");
}

vs split(const string& s, const string delim){
	vs res;
	string at;
	int n = s.sz();

	for(int i = 0; i < n; i++){
		char c = s[i];
		if(delim.find(c) != string::npos){
			if(at.sz() > 0){
				res.pb(at);
			}
			at = "";
		} else {
			at.pb(c);
		}
	}
	if(at.sz() > 0){
		res.pb(at);
	}

	return res;
}

template <typename S, typename T>
T convert(const S var){
	T res;
	stringstream ss;
	ss << var;
	ss >> res;

	return res;

}

int main(void){
	int T;
	cin >> T;
	for(int p = 0; p < T; p++){
		string s;
		cin >> s;
		string ss = s;
		if(!next_permutation(all(s))){
			sort(all(s));

			int nz=0;
			while(s[nz] == '0') nz++;
			char cnz = s[nz];
			fd(i,nz,1){
				s[i] = s[i-1];
			}
			s[0] = cnz;

			s.pb('0');
			fd(i,s.sz()-1,2){
				s[i] = s[i-1];
			}
			s[1] = '0';

		}
		printf("Case #%d: %s\n", p+1, s.c_str());
	}
	return 0;
}
