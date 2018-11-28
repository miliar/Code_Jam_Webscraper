#include<iostream>
#include<set>
#include<vector>
using namespace std;

string s;
vector<string> st;
set<char> ar[20];
int bnyk,L,D,N,i,j,x,ans,tc;
char c;
bool valid;

int main() {
	cin>>L>>D>>N;
	for(i=0;i<D;i++) {
		cin>>s;
		st.push_back(s);
	}
	for(tc=1;tc<=N;tc++) {
		for(i=0;i<L;i++) {
			ar[i].clear();
			cin>>c;
			if(c=='(') {
				while(1) {
					cin>>c;
					if(c==')') break;
					ar[i].insert(c);
				}
			}
			else ar[i].insert(c);
		}
		cout<<"Case #"<<tc<<": ";
		ans=0;
		for(i=0;i<D;i++) {
			valid=1;
			for(j=0;j<L;j++) {
				if(!valid) break;
				if(ar[j].find(st[i][j])==ar[j].end()) valid=0;
			}
			if(valid) ans++;
		}
		cout<<ans<<endl;
	}
	return 0;
}
