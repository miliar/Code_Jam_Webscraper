#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

string se[101];
string qs[1002];
int dp[1002][101];
string line;

int main() {
	int n;
	stringstream sin;
	getline(fin,line);
	sin.clear();
	sin<<line;
	sin>>n;
	int t,s,q,i,j,k;
	int minn;
	string query;
	for(t=1;t<=n;t++) {
		getline(fin,line);
		sin.clear();
		sin<<line;
		sin>>s;
		for(i=0;i<s;i++){getline(fin,se[i]);}
		getline(fin,line);
		sin.clear();
		sin<<line;
		sin>>q;
		for(i=0;i<q;i++){getline(fin,qs[i]);}
		//for(i=0;i<q;i++)cout<<qs[i]<<endl;
		for(i=0;i<s;i++)dp[0][i]=0;
		//if(se[1]==qs[0]){cout<<"hello"<<endl;}
		for(i=1;i<=q;i++) {
			minn=-1;
			for(j=0;j<s;j++) if(dp[i-1][j]!=-1) {
				if(minn==-1 || minn>dp[i-1][j])minn=dp[i-1][j];
			}
			minn++;
			for(j=0;j<s;j++)dp[i][j]=minn;
			query=qs[i-1];
			for(j=0;j<s;j++) {
				if(query==se[j]){dp[i][j]=-1;}
				else {
					if(dp[i-1][j]!=-1 && dp[i-1][j]<dp[i][j])dp[i][j]=dp[i-1][j];
				}
			}
		}
		minn=-1;
		for(j=0;j<s;j++) if(dp[q][j]!=-1) {
			//cout<<"--- "<<dp[q][j]<<endl;
			if(minn==-1 || minn>dp[q][j])minn=dp[q][j];
		}
		fout<<"Case #"<<t<<": "<<minn<<endl;
		//for(j=0;j<s;j++) {
		//	for(i=0;i<=q;i++)cout<<dp[i][j]<<"    ";
		//	cout<<endl;
		//}
	}
	return 0;
}