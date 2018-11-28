#include<string>
#include<map>
#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

string solve(string s,map<string,char> rep,map<char,char> op) {
	string r;
	r.push_back(s[0]);
	for(int i=1;i<s.size();i++) {
		bool add=1;
		if(r.size()>0) {
			string t;
			t.push_back(r[r.size()-1]);
			t.push_back(s[i]);
			if(rep.find(t)!=rep.end()) {
				add=0;
				r[r.size()-1]=rep[t];
			}
			else {
				reverse(t.begin(),t.end());
				if(rep.find(t)!=rep.end()) {
					add=0;
					r[r.size()-1]=rep[t];
				}
			}
		}
		if(add && op.find(s[i])!=op.end() && r.size()>0) {
			char opuesto=op[s[i]];
			for(int i=0;i<r.size();i++)
				if(opuesto==r[i])
					add=0;
			if(!add)
				r.clear();
		}
		if(add)
			r.push_back(s[i]);
	}
	return r;
}

void salida(string s) {
	if(s.size()==0) {
		printf("[]\n");
		return;
	}
	printf("[");
	for(int i=0;i<s.size()-1;i++)
		printf("%c, ",s[i]);
	printf("%c]\n",s[s.size()-1]);
}

int main() {
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++) {
		map<string,char> rep;
		map<char,char> op;
		int c;
		scanf("%d",&c);
		string tt;
		while(c--) {
			cin>>tt;
			rep[tt.substr(0,2)]=tt[2];
		}
		scanf("%d",&c);
		while(c--) {
			cin>>tt;
			op[tt[0]]=tt[1];
			op[tt[1]]=tt[0];
		}
		scanf("%d",&c);
		cin>>tt;
		printf("Case #%d: ",caso);
		salida(solve(tt,rep,op));
	}
	return 0;
}
