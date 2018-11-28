#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
int numsl(string s){
	int n=0;
	for(int i=0;i<s.size();i++)
		if(s[i]=='/')
			n++;
	return n;
}
int main(){
	int c,n,m,maxlen;
	string s,z,bestdir;
	cin>> c;
	int tot;
	for(int y=1;y<=c;y++){
		set<string> v;
		cin >> n >> m;
		getline(cin,s);
		tot=0;
		for(int i=0;i<n;i++){
			getline(cin,s);
			v.insert(s);
		}
		for(int i=0;i<m;i++){
			getline(cin,s);
			maxlen=0;
			bestdir="";
			for(set<string>::iterator j=v.begin();j!=v.end();j++){
				z = *j;
				if(s.find(z)==0 and z.size()>maxlen and (s.size()==z.size() || s[z.size()]=='/')){
					maxlen=z.size();
					bestdir=z;
				}
			}
			tot+=numsl(s)-numsl(bestdir);
			for(int j=1;j<s.size();j++)
				if(s[j]=='/'){
					v.insert(s.substr(0,j));
				}
			v.insert(s);
		}
		cout<< "Case #"<<y<<": "<<tot<<endl;
	}
}
