#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <stack>
#include <map>
#pragma comment(linker, "/STACK:165777216")
using namespace std;

char mp[256];
void init(){
	string str="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz";
	string s="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq";
	for(int i=0; i<str.length(); i++){
		mp[str[i]]=s[i];
	}
}
int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int n;
	init();
	cin>>n;
	string str;
	getline(cin,str);
	for(int i=0; i<n; i++){
		getline(cin,str);
		cout<<"Case #"<<i+1<<": ";
		for(int j=0; j<str.length(); j++){
			if(str[j]==' '){
				cout<<" ";
			}else{
				cout<<mp[str[j]];
			}
		}
		cout<<endl;
	}
	return 0;
}