#include<vector>
#include<string>
#include<iostream>
#include<iomanip>
using namespace std;
const char PATTERN[] = "welcome to code jam";
int solve(const char*input){
	vector<int> count(strlen(PATTERN)+1);
	count[0]=1;
	for(;*input;++input){
		for(int i=0;PATTERN[i];++i){
			if(PATTERN[i]==*input){
				count[i+1] = (count[i+1]+count[i])%10000;
			}
		}
	}
	return count[strlen(PATTERN)];
}
int main(){
	string line;
	getline(cin,line);
	int n = atoi(line.c_str());
	for(int i=1;i<=n;++i){
		getline(cin,line);
		cout << "Case #"<<i<<": " << setfill('0') << setw(4) << solve(line.c_str()) << endl;
	}
}
