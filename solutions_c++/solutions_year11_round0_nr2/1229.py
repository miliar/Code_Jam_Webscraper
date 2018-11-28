#include <string>
#include <iostream>
#include <map>
using namespace std;
int numComb;
int numOp;
int len;
map<char, char> opposed;
map<char, char> combine;
map<pair<char, char>, char> result;
string spell;
void scanInput(void){
	opposed.clear();
	combine.clear();
	result.clear();
	spell="";
	cin>>numComb;
	for(int i=0;i<numComb;++i){
		string s;
		cin>>s;
		combine[s[0]]=s[1];
		combine[s[1]]=s[0];
		result[make_pair(s[0], s[1])]=s[2];
		result[make_pair(s[1], s[0])]=s[2];
	}
	cin>>numOp;
	for(int i=0;i<numOp;++i){
		string s;
		cin>>s;
		opposed[s[0]]=s[1];
		opposed[s[1]]=s[0];
	}
	cin>>len;
	cin>>spell;
}

void printOutput(string &s, int c){
	cout<<"Case #"<<c+1<<": [";
	for(unsigned i=0;i<s.size();++i){
		cout<<s[i];
		if(i<s.size()-1){
			cout<<", ";
		}
	}
	cout<<"]"<<endl;
}


void update(string &s){
	bool changed=true;
	while(changed){
		int n=s.size();
		changed=false;
		if(n>1){
			if(combine[s[n-1]]==s[n-2]){
				s[n-2]=result[make_pair(s[n-2], s[n-1])];
				s.erase(s.begin()+(n-1));
				//changed=true;
			}else if(s.find(opposed[s[n-1]])!=string::npos){
				s="";
			}
		}
	}
}
string processSpell(void){
	string sol;
	for(unsigned i=0;i<spell.size();++i){
		sol+=spell[i];
		update(sol);
	}
	return sol;
}

int main(int argc, char *argv[]){
	int numCases;
	cin>>numCases;
	for(int c=0;c<numCases;++c){
		string sol;
		scanInput();
		sol=processSpell();
		printOutput(sol,c);
	}
	return 0;
}
