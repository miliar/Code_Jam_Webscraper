#include <fstream>
#include <string>

using namespace std;

int solve(string instr, string target){
	if(instr == target) return 1;
	if(target.size() == 0) return 1;
	if(instr.size() < target.size()) return 0;
	int i;
	for(i=0;i<instr.size();i++){
		if(instr[i] == target[0]) break;
	}
	if(i==instr.size()) return 0;
	return (solve(instr.substr(i+1), target.substr(1)) + solve(instr.substr(i+1), target))%10000; 
}
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("C-small-attempt3.in");
	fout.open("C-small3.out");
	int n;
	fin>>n;
	char input1[1];
	fin.getline(input1,1);
	for(int ci=1;ci<=n;ci++){
		char input[600];
		fin.getline(input,600);
		string instr = input;
		fout<<"Case #"<<ci<<": ";
		fout.fill('0');
		fout.width(4);
		fout<<solve(instr, "welcome to code jam")<<endl;
	}
}