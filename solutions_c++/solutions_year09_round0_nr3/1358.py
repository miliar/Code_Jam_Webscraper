#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

ifstream cin("C-Large.in");
ofstream cout("CLarge.out");

const string Welcome = "welcome to code jam";
int dp[25][600]={0};
//returns the numbers of occurrences of the substring of Welcome starting at i
//in the substring of s starting at j;
int f(string &s,int i,int j){
	if(i==Welcome.size()) return 1;
	if(j==s.size()) return 0;
	if(dp[i][j]!=-1) return dp[i][j];
	int retval = f(s,i,j+1);
	if(Welcome[i]==s[j]) retval+=f(s,i+1,j+1);
	retval = retval%10000;
	dp[i][j]=retval;
	return retval;
}

int main(){
	int N;
	cin >> N;
	string s;
	string zeros = "0000000";
	getline(cin,s);
	for(int i=0;i<N;i++){
		fill(&(dp[0][0]),&(dp[24][599]),-1);
		getline(cin,s);
		int ret = f(s,0,0);
		string s2;
		ostringstream oss;
		oss<<ret;
		s2=oss.str();
		s2 = zeros.substr(0,4-s2.size()) + s2;
		cout << "Case #" << i + 1 << ": "<<s2 << endl;
	}
	return 0;
}