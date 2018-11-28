#include <iostream>
#include <string>
#include <cstring>
using namespace std;

const int MAXL = 500;
const char* WELCOME = "welcome to code jam";
const int L = 19;
const int MOD = 10000;

int ans[MAXL+1][L+1];

int main(int argc, char* args[]){
	if (argc < 3){
		cout << "lack of args" << endl;
		return 0;
	}
	freopen(args[1], "r", stdin);
	freopen(args[2], "w", stdout);
	int N;
	cin >> N;
	string temp;
	getline(cin, temp);
	for(int ic=0; ic<N; ic++){
		string line;
		getline(cin, line);
		int l = line.size();
		memset(ans, 0, sizeof(ans));
		ans[0][0] = 1;
		for(int i=1; i<=l; i++){
			ans[i][0] = 1;
			for(int j=1; j<=L; j++){
				ans[i][j] = ans[i-1][j];
				if (WELCOME[j-1] == line[i-1]){
					ans[i][j] += ans[i-1][j-1];
					ans[i][j] %= MOD;
				}
			}
		}
		printf("Case #%d: %.04d\n", ic+1, ans[l][L]);
	}
}

