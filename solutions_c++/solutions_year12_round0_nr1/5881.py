#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <map>

using namespace std;

map<char, char> googlerese;

void init(){
	string s = "abcdefghijklmnopqrstuvwxyz";
	string s1 = "ynficwlbkuomxsevzpdrjgthaq";

	for(int i=0; i<s.size(); i++)
		googlerese[s1[i]] = s[i];
}

string solve (string str){
	string ans = str;

	for(int i=0; i<str.size(); i++)
		{
			if(googlerese.find(str[i])!=googlerese.end())
				ans[i] = googlerese[str[i]];
		}

	return ans;
}

int main(){
	int T;
	fstream ps("statement.txt");
	fstream output("output.txt",fstream::trunc | fstream::out);
	ps>>T;
	int i=1;
	init();
	while(i!=T+1){
		string str;
		do {
			getline(ps,str);
		}while(str=="");
		output<<"Case #"<<i<<": "<<solve(str)<<endl;
		//cout<<"Case #"<<i<<": "<<solve(str,str1,N)<<endl;
		i++;	
	}		
	return 0;
}	
