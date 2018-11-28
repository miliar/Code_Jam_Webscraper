#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
using namespace std;

string w="welcome to code jam";

int main()
{
	int n;
	cin >> n;
	int dp[20][501];
	string in;
	int i,j,k;
	getline(cin,in);
	for(i=0;i<n;i++){
//		cin >> in;
		getline(cin,in);
//		cout << in << endl;
		for(j=0;j<20;j++) for(k=0;k<501;k++) dp[j][k]=0;
		for(k=0;k<in.size();k++) if(in[k]=='m') dp[18][k]=1;
		for(j=17;j>=0;j--){
			int s=0;
			for(k=in.size()-1;k>=0;k--){
				if(w[j]==in[k]) dp[j][k]=s;
				s = (s+dp[j+1][k]) % 10000;
			}
		}
/*		
		for(j=0;j<20;j++){
			for(k=0;k<in.size()-1;k++){
				cout << dp[j][k] << " ";
			}
			cout << endl;
		}
*/		
		int s=0;
		for(j=0;j<in.size();j++){
			s=(s+dp[0][j])%10000;
		}
		printf("Case #%d: %04d\n",i+1,s);
	}
	return 0;
}
