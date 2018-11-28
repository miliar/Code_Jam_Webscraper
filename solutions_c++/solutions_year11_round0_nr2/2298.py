#include <map>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <set>

using namespace std;
bool chkopp(string ans,set<int> opp){
	int flag=0;
	for(int i=0;i<(int)ans.size();i++){
		char c=ans[i];
		if(opp.find(c)==opp.end()) flag++;
		else return true;
	}
	if (flag==(int)ans.size()) return false;
	else	return true;
	}

string solve(string str1){
	stringstream s(str1);
	map<string,char> comb;
	map<char,set<int> > opp;
	int C;
	s>>C;
	//cout<<C;
	for(int i=0;i<C;i++){
		string str;
		s>>str;
		char t2=str[2];
		string t1=str.substr(0,2);
		comb[t1]=t2;
		reverse(t1.begin(),t1.end());		
		comb[t1]=t2;
	}
	int D;
	s>>D;
	//cout<<D;
	for(int i=0;i<D;i++){
		string str;
		s>>str;
		opp[str[0]].insert(str[1]);
		opp[str[1]].insert(str[0]);
	}
	int N;
	s>>N;
	//cout<<N;
	string el;
	s>>el;
	//cout<<el;
	string ans="";
	for(int i=0;i<N;i++){
		char ine=el[i];
		int len=ans.size();
		string com="";
		com+=ans[len-1];
		com+=ine;
		//cout<<com<<endl;
		if(len==0) {
			ans.push_back(ine);
		}
		else if (comb[com]!='\0'){
			ans[ans.size()-1]=comb[com];
			//cout<<ans<<" "<<comb[com]<<endl;
		}
		else if (chkopp(ans,opp[ine])){
			ans.clear();
		}
		else {
			ans.push_back(ine);
		}
		//cout<<ans<<endl;
	}
	//cout<<ans<<endl;
	string temp="[";
	if(ans.size()==0) return "[]";
	for(int i=0;i<(int)ans.size()-1;i++){
		temp+=ans[i];
		//cout<<temp<<endl;
		temp+=", ";
	}
	temp+=ans[ans.size()-1];
	temp+="]";
   return temp;
}	

int main(){
	int T;
	fstream ps("statement.txt");
	fstream output("output.txt",fstream::trunc | fstream::out);
	ps>>T;
	int i=1;
	while(i!=T+1){
		string str;
		do {
			getline(ps,str);
		}while(str=="");
		output<<"Case #"<<i<<": "<<solve(str)<<endl;
		//cout<<"Case #"<<i<<": "<<solve(str)<<endl;
		i++;	
	}		
	return 0;
}	
