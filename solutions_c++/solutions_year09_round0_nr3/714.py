#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int testcase;
	cin >> testcase;
	char source[] = "welcome to code jam";
	//char source[] = "abc";
	char temp[1000];
	cin.getline(temp,1000);
	for(int t=0; t< testcase ;t++) {
		char input[1000];
		cin.getline(input,1000);
		int inputsize = strlen(input);
		int sourcesize = strlen(source);

		vector< vector<int > > DP(inputsize, vector<int>(sourcesize,0));
		for(int i=0;i < inputsize;i++) {
			for(int j=0;j < sourcesize; j++) {
				if ( input[i] == source[j] ) {
					if ( i-1 >= 0 )
						DP[i][j] += DP[i-1][j];
					if ( i-1 >=0 && j-1 >=0 ) {
						DP[i][j] += DP[i-1][j-1] ;
					}
					if ( j == 0 )
						DP[i][j]++;
				} else {
					if ( i-1 >= 0 )
						DP[i][j] = DP[i-1][j];
				}
				DP[i][j] = DP[i][j] % 10000;
			}
		}
		cout << "Case #" << t+1<< ": " ;
		if ( DP[inputsize-1][sourcesize-1] < 1000 )
			cout <<'0';
		if ( DP[inputsize-1][sourcesize-1] < 100 )
			cout <<'0';
		if ( DP[inputsize-1][sourcesize-1] < 10 )
			cout <<'0';
		cout << DP[inputsize-1][sourcesize-1] <<endl;

	}
}