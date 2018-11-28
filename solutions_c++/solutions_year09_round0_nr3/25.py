#include <iostream>
#include <string>
using namespace std;

int main() {
	int N;
	char toCompare[100] = "welcome to code jam";
	int len = 19;
	
	cin >> N;
	string thisString;
	getline(cin, thisString);
	for (int i = 0; i < N; i++) {
		getline(cin, thisString);
		int len2 = thisString.length();
		
		int dp[100];
		for (int k = 1; k <= len; k++) dp[k] = 0;
		dp[0] = 1;
		for (int k = 0; k < len2; k++)
			for (int j = len-1; j >= 0; j--)
				if (thisString[k] == toCompare[j]) dp[j+1] = (dp[j+1]+dp[j])%10000;
		cout << "Case #" << (i+1) << ": ";
		if (dp[len] < 10) cout << 0;
		if (dp[len] < 100) cout << 0;
		if (dp[len] < 1000) cout << 0;
		cout << dp[len] << endl;
	}
}
