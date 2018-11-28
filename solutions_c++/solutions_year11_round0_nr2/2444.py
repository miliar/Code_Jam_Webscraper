#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

#define X first
#define Y second
int casen=1;
#define caseout cout<<"Case #"<<casen++<<": "
typedef pair<int,int> pii;

void doCombine(vector<char> &v,vector<string> c){
	if(v.size() < 2) return;
	int did_something;
	do {
		did_something=0;
		for(int i=0;i<c.size();i++){
			if( (v[v.size()-1] == c[i][0] && v[v.size()-2] == c[i][1]) || 
					(v[v.size()-2] == c[i][0] && v[v.size()-1] == c[i][1]) ) {
				v.pop_back();
				v.pop_back();
				v.push_back(c[i][2]);
				did_something++;
				break;
			}
		}
	} while(did_something);
}
bool contains(vector<char> v,char c){
	for(int i=0;i<v.size();i++)
		if(v[i] == c) return true;
	return false;
}
void doOppose(vector<char> &v,vector<string> o){
	if(v.size() < 2)return;
	for(int i=0;i<o.size();i++)
		if(contains(v,o[i][0]) && contains(v,o[i][1])) v.clear();
}
void func(){
	int C;
	cin>>C;
	string s;
	vector<string> combine;
	for(int i=0;i<C;i++){
		cin>>s;
		combine.push_back(s);
	}
	int D;
	cin>>D;
	vector<string> oppose;
	for(int i=0;i<D;i++){
		cin>>s;
		oppose.push_back(s);
	}
	cin>>s; cin>>s;
	vector<char> final;
	for(int i=0;i<s.length();i++){
		final.push_back(s[i]);
		doCombine(final,combine);
		doOppose(final,oppose);
	}
	string ret = "[";
	for(int i=0;i<final.size();i++) {
		ret+=final[i];
		if(i!=final.size()-1)ret+=", ";
	}
	ret+="]";
	caseout<<ret<<endl;
}

int main(){
	int T;
	cin>>T;
	for(int iT=0;iT<T;iT++) func();
	return 0;
}
