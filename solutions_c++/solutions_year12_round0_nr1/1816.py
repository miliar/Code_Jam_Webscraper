#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <functional>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
using namespace std;

char decoding[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(){
	int T;
	string s;
	cin>>T;
	cin.ignore();
	for(int X = 1; X <= T; X++){
		string ans;
		getline(cin,s);
		for(int i = 0,l = s.size(); i < l; i++){
			int c = s[i] - 'a';
			if(0<=c && c<=26) c = decoding[c];
			else c += 'a';
			ans += c;
		}
		printf("Case #%d: ",X);
		cout<<ans<<endl;
	}
	return 0;
}