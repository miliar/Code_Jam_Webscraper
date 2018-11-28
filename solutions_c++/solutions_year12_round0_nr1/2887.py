#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<list>
#include<sstream>
#include<string>
#include<cstring>
#include<cstdlib>
#include<set>
#include<map>
#include<vector>
using namespace std;

string lett = "abcdefghijklmnopqrstuvwxyz";
string letm = "yhesocvxduiglbkrztnwjpfmaq";

int test_case;
char in[ 1000 ];


int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &test_case);
	scanf("%*c");
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		gets( in ) ;
		stringstream ss ( in );
		string s;
		printf("Case #%d:", caseId );
		while( ss >> s ) {
			int n = s.size();
			string res = "";
			for( int i = 0; i < n; i ++ ) {
				res += letm[ s[ i ] - 'a' ];
			}

			cout<< " " << res ;
			
		}

		printf("\n");

	}
	return 0;
}