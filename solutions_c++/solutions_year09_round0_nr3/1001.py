#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

string wel = "welcome to code jam";
string s;

const int nmax = 505;
const int nn = 30;
const int mod = 10000;

int f[nmax][nn];

int rec(int i,int j){
	if (j == wel.size()) return 1;
	if (i == s.size()) return 0;
	if (f[i][j] > -1) return f[i][j];

	int ans = rec(i+1,j);
	if (s[i] == wel[j]) ans = (ans + rec(i+1,j+1)) % mod;
	f[i][j] = ans;
	return ans;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	

	int ntest;
	scanf("%i\n",&ntest);

	for (int test = 1;test <= ntest; ++test){
		getline(cin,s);
		memset(f,-1,sizeof(f));
		int ans = rec(0,0);
		int t[4];
		for (int i = 0;i < 4; ++i){
			t[i] = ans % 10;
			ans /= 10;
		}
		printf("Case #%i: ",test);
		for (int i = 3; i >= 0; --i) printf("%i",t[i]);
		printf("\n");
	}


	
	return 0;
}