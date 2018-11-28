#include<iostream>
#include<map>
#include<set>
#include<vector>
using namespace std;

map<pair<char,char>,char> combine;
set<pair<char,char> > oppose;
int T,C,D,N;
string S,st;
char c,d;

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		combine.clear(); oppose.clear();
		cin>>C;
		for(int i=0;i<C;i++) {
			cin>>S;
			combine[make_pair(S[0],S[1])]=S[2];
			combine[make_pair(S[1],S[0])]=S[2];
		}
		cin>>D;
		for(int i=0;i<D;i++) {
			cin>>S;
			oppose.insert(make_pair(S[0],S[1]));
			oppose.insert(make_pair(S[1],S[0]));
		}
		cin>>N;
		cin>>st; S="";
		for(int i=0;i<st.length();i++) {
			c=st[i];
			S=S+c;
			while(S.length()>1&&combine.find(make_pair(S[S.length()-2],S[S.length()-1]))!=combine.end()) {
				c=combine[make_pair(S[S.length()-2],S[S.length()-1])];
				S=S.substr(0,S.length()-2);
				S=S+c;
			}
			c=S[S.length()-1];
			for(int j=S.length()-2;j>=0;j--) {
				d=S[j];
				if(oppose.find(make_pair(c,d))!=oppose.end()) {
					S=""; break;
				}
			}
		}
		cout<<"Case #"<<tc<<": ";
		cout<<"[";
		for(int i=0;i<S.length();i++) {
			if(i>0) cout<<", ";
			cout<<S[i];
		}
		cout<<"]"<<endl;
	}
}
