#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;
const string FILE_NAME = "B-small-attempt0.in";

void CreateCombMap(map<string,char> & comb, ifstream & file);
void CreateCancelMap(map<char,char> & cancel, map<char,int> & flag, ifstream & file);
string Solve(map<string,char> &, map<char,char> &,map<char,int> &, string);
void Write(int,string,ofstream &);
void Initialize(map<char,int> &);

int main(){
	ifstream file;
	ofstream output;
	file.open(FILE_NAME.c_str());
	output.open("solution.txt");
	int num_lines;

	file>>num_lines;

	for (int i=0;i<num_lines;i++){
		map<string,char> rules_combining;
		map<char,char> rules_cancel;
		map<char,int> flag;
		string example_string;
		CreateCombMap(rules_combining,file);
		CreateCancelMap(rules_cancel,flag,file);

		int bla;
		file>>bla;
		file>>example_string;
		string solution=Solve(rules_combining,rules_cancel,flag,example_string);
		Write(i,solution,output);
	}
	file.close();
	output.close();
return 0;
}

void CreateCombMap(map<string,char> & comb, ifstream & file){
	int n;
	file>>n;
	for (int i=0;i<n;i++){
		string s;
		file>>s;
		char c;
		c=s[2];
		comb[string(1,s[0])+s[1]]=c;
		comb[string(1,s[1])+s[0]]=c;
	}
}

void CreateCancelMap(map<char,char> & cancel, map<char,int> & flag, ifstream & file){
	int n;
	file>>n;
	for (int i=0;i<n;i++){
		string s;
		file>>s;
		cancel[s[0]]=s[1];
		cancel[s[1]]=s[0];
		flag[s[0]]=0;
		flag[s[1]]=0;
	}
}

string Solve(map<string,char> & comb, map<char,char> & cancel,map<char,int> & flag, string example){
	string sol="";
	int l=example.length();
	int i=0;

	while (i<l){

		char c1=example[i];

		if (sol.length()>0){
			char last=sol[sol.length()-1];
			string temp=last+string(1,c1);
			if (comb.find(temp) != comb.end()){
				c1=comb[temp];
				sol=sol.substr(0,sol.length()-1);
				flag[last]--;
			}
		}

		if (cancel.find(c1) != cancel.end() && flag[cancel[c1]] > 0){
			sol="";
			Initialize(flag);
		}else{
			sol+=c1;
			flag[c1]++;
		}

		i++;
	}
	return sol;
}


void Write(int n, string s, ofstream & file){
	file<<"Case #"<<n+1<<": [";
	for (int i=0; i<s.length() ;i++){
		file<<s[i];
		if (i != s.length()-1){
			file<<", ";
		}
	}
	file<<"]"<<endl;
}

void Initialize(map<char,int> & flag){
	map<char,int>::iterator it;
	for (it=flag.begin(); it!=flag.end(); ++it) {
		it->second = 0;
	}
}

