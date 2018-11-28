#include<iostream>
#include<fstream>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;
int l,d,n;
string s;
typedef long long LL;
struct node{
	int next[26];
	node(){
		fill_n(next, 26, -1);
	}
};
node trie[100000];
int nn;

void add(){
	int cur=0;
	for(int i=0; i<s.size(); ++i){
		int c=s[i]-'a';
		if(trie[cur].next[c]==-1)
			trie[cur].next[c]=nn++;
		cur=trie[cur].next[c];
	}
}
LL compute(int cur, int nod){
	if(cur==s.size()){
		return 1;
	}
	if(s[cur]=='('){
		LL rtn=0;
		int next;
		for(next=cur+1; s[next]!=')'; ++next);
		++next;
		for(++cur; s[cur]!=')'; ++cur){
			int c=s[cur]-'a';
			if(trie[nod].next[c]!=-1)
				rtn+=compute(next, trie[nod].next[c]);
		}
		return rtn;
	}else{
		int c=s[cur]-'a';
		if(trie[nod].next[c]==-1)
			return 0;
		else
			return compute(cur+1, trie[nod].next[c]);
	}
}
int main(){
	ifstream fin("A-large.in");
	ofstream fout("A.out");
	fin>>l>>d>>n;
	nn=1;
	for(int i=0; i<d; ++i){
		fin>>s;
		add();
	}
	for(int cas=1; cas<=n; cas++){
		fin>>s;
		LL rtn=compute(0,0);
		fout<<"Case #"<<cas<<": "<<rtn<<endl;
	}
}
