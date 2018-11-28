#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<set>
#include<map>
#include<cstring>
#include<cctype>
using namespace std;
string tree;
int ind;
const char* str;
void skip(){
	while(1){
		if(str[ind]!=' '&&str[ind]!='\n') break;
		ind++;
	}
}
void skipnum(){
	while(isdigit(str[ind])||str[ind]=='.'){
		ind++;
	}
	//cout << "skipnum:"<<str[ind]<<endl;
}
void skipparen(){
	while(str[ind]!='('){
		ind++;
	}
	ind++;
	int par=1;
	while(par!=0){
		if(str[ind]=='(') par++;
		else if(str[ind]==')') par--;
		ind++;
	}
	ind++;
}
void next(){
	while(str[ind]!='('){
		ind++;
	}
	ind++;
}
void solve(int cnum){
	int ln;
	cin >> ln >> ws;
	tree.clear();
	for(int i=0 ; i<ln  ;i++){
		string s;
		getline(cin,s);
		tree+=s;
	}
	cout <<"Case #"<<cnum+1<<":"<<endl;
	int num;
	cin >> num;
	str=tree.c_str();
	for(int i=0 ; i<num ; i++){
		vector<string> feat;
		string name;
		cin >> name;
		int l; cin >> l;
		
		for(int j=0 ; j<l ; j++) {
			cin >> name; feat.push_back(name);
		}
		ind=1;
		double p=1.0;
		while(1){
			skip();
			double temp;
			sscanf(&str[ind],"%lf",&temp);
			//cout << "scanf:"<<temp<<endl;
			p*=temp;
			skipnum();skip();
			if(str[ind]==')') break;
			skip();
			char buf[100];
			sscanf(&str[ind],"%s",buf);
			string ss(buf);
			
			//cout <<"scanf,str:"<< ss << endl;

			vector<string>::iterator it=find(feat.begin(),feat.end(),ss);
			if(it==feat.end()){
				skipparen();
			}
			next();
		}
		printf("%.7f\n",p);
	}
}
int main(){
	
	int n;
	cin >> n;
	for(int i=0 ; i<n ; i++){
		solve(i);
	}
	
	return 0;
}