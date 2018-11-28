#include <iostream>
#include <string>
#include <fstream>
using namespace std;
#define cin fin
#define cout fout
char map[30];
int main(){
    ifstream fin ("a.in");
	ofstream fout ("a.out");
	string a[3]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string b[3]={"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
	for(int i=0;i<3;i++){
		for(int j=0;j<a[i].size();j++){
			if(a[i][j]!=' '){
				map[a[i][j]-'a']=b[i][j];
				//cout<<a[i][j]<<" "<<b[i][j]<<endl;
			}
		}
	}
	map['z'-'a']='q';
	map['q'-'a']='z';
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	for(int i=1;i<=t;i++){
		getline(cin,s);
		string ans;
		for(int j=0;j<s.size();j++){
			if(s[j]!=' ')
				ans+=map[s[j]-'a'];
			else
				ans+=' ';
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
