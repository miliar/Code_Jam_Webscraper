#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <iostream>

using namespace std;

char M[1000];

string solve( string s ){
	string ans = s;
	for( int i = 0; i < s.size(); ++i ){
		ans[i] = M[s[i]];
	}

	return ans;
}

void input_output(){
	int N;
	char buf[205];
	scanf( "%d\n", &N );
	for( int t = 1; t <= N; ++t ){
		gets( buf );
		string s( buf );
		printf("Case #%d: %s\n", t, solve(s).c_str() );
	}
}

int build_map(){
	vector<string>inp;
	inp.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	inp.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	inp.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");

	vector<string>outp;
	outp.push_back("our language is impossible to understand");
	outp.push_back("there are twenty six factorial possibilities");
	outp.push_back("so it is okay if you want to just give up");

	for( int i = 0; i < inp.size(); ++i ){
		for( int j = 0;j < inp[i].size(); ++j ){
			M[inp[i][j]] = outp[i][j];
		}
	}

	M['q'] = 'z';
	M['z'] = 'q';

	int cnt = 0;

	for( int i = 0; i < 1000; ++i ){
		if( M[i] )
			cnt++;
	}

	M[' '] = ' ';

	return cnt;
}

int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	build_map();
	input_output();

	return 0;
}