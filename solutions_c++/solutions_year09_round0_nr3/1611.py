#include<fstream>
#include<iostream>
#include<vector>
#include<string>
#include<iomanip>
using namespace std;

ifstream fin("C-large.in");
ofstream fout("C.out");

string input;
int mod = 10000;
string pat = "welcome to code jam";
int dp[21][501];

int main(){
	int N;  fin>>N;
	for(int i=1; i<=N; i++){
		getline(fin, input, '\n');
		while(input.length()==0)  getline(fin, input, '\n');
//		cout<<input<<endl<<endl;
		memset(dp, 0, sizeof(dp));
		int L = input.length();
		for(int x=1; x<=19; x++){
			for(int y=1; y<=L; y++){
				if(input[y-1]==pat[x-1]){
					if(x==1) dp[x][y]=dp[x][y-1]+1;
					else dp[x][y] = dp[x-1][y-1] + dp[x][y-1];
				}
				else dp[x][y] = dp[x][y-1];
				dp[x][y] %= mod;
				//cout<<dp[x][y]<<" ";
			}
			//cout<<endl;
		}
		fout<<"Case #"<<i<<": ";
		fout<<setw(4)<<setfill('0')<<dp[19][L]<<endl;
	}
}