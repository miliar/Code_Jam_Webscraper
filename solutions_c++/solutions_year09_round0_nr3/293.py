#include<iostream>
#include<vector>
#include<string>
#include <iomanip>

using namespace std;

int main(){
	int N;
	cin>>N;
	vector<string> lines(N);
	vector<vector<int>  > dp(550, vector<int >(550, 0));
	getline(cin, lines[0]);
	string p = "welcome to code jam";
	int pl = p.length();
	for(int i=0; i<N; i++){
		//cin>>wrds[i]; 
		getline(cin, lines[i]);
		int res=0;
		string s = lines[i];
		if(p[0]==s[0]){
			dp[0][0]=1;
		} else{
			dp[0][0]=0;
		}
		for(int j=1; j<=s.length(); j++){
			for(int k=0; k<=j && k<=pl; k++){
				dp[j][k] = dp[j-1][k];
				if(k==0 && s[j]==p[k])dp[j][k]++;
				else
				if(s[j]==p[k])dp[j][k]+=dp[j-1][k-1];
				dp[j][k]%=10000;
			}
		}
		res = dp[s.length()][pl];
		cout<<"Case #"<<i+1<<": "<<setfill('0') << setw(4) <<res<<"\n";
	}
	
}
