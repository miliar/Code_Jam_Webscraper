#include<iostream>
#include<string>
#include<vector>

using namespace std;

vector<string> A,B;

int main() {
    int t,T,N,M,m,cnt,i,j;
    cin>>T;
    for(t=1;t<=T;t++) {
		A.clear();B.clear();
		cin>>N>>M;
		string s;
		cnt=0;
		while(N--) {cin>>s;A.push_back(s);}
		while(M--) {cin>>s;B.push_back(s);}
		while(!B.empty()) {
			s = B.back();
			B.pop_back();
			m=0;
			for(i=0;i<A.size();i++) {
				for(j=0;A[i][j] == s[j] && j<A[i].size() && j<s.size();j++) {
					if(A[i][j]=='/' && j-1 > m) m = j-1;
				}
				if(j<A[i].size() && A[i][j] != '/') continue;
				if(j<s.size() && s[j] != '/') continue;
				if(j-1>m) m=j-1;
			}
			for(i=m;i<s.size();i++) if(s[i]=='/') cnt++;
			A.push_back(s);
		}
		cout<<"Case #"<<t<<": "<<cnt<<endl;
    }
    return 0;
}
