#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

string line;
int N;
string s;
int mem[600][25];

int rek(int a, int b){
	if( mem[a][b] != -1 ) return mem[a][b];
	int sol = 0;
	if(b == (int)s.length()) return 1;
	if(a == N) return 0;
	if( line[a] == s[b] ) sol = (sol + 1 * rek(a+1,b+1) % 10000) % 10000;
	sol = (sol + 1 * rek(a+1,b) % 10000) % 10000;
	return mem[a][b] = sol;
}

int main(){
	s = "welcome to code jam";
	int n;
	scanf("%d",&n);
	for(int x = 0;x<n;++x){
		memset(mem, -1, sizeof(mem));
		getline(cin, line);
		N = (int)line.length();
		printf("Case #%d: %04d\n",x+1, rek(0,0)%10000);
	}
	return 0;
}