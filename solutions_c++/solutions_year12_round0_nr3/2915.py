#include "stdafx.h"

string exchange(string s){
	stringstream ss;
	ss<<s.substr(1)<<s[0];
	return ss.str();
}

int recycle(int A, int B){
	int c=0;
	iloop(n, A, B){
		set<int> C;
		string s=String(n);
		int m;
		loop(i, 1, s.length()){
			s=exchange(s);
			m=Int(s);
			if(n<m && m<=B){
				C.insert(m);
			}
		}
		c+=size(C);
	}
	return c;
}

int main(){
	int T;
	cin>>T;
	int A, B;
	loop(C, 1, T+1){
		cin>>A>>B;
		cout<<"Case #"<<C<<": "<<recycle(A, B)<<endl;
	}
	return 0;
}
