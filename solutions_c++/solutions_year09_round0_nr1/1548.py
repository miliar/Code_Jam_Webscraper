#include<fstream>
#include<iostream>
#include<vector>
#include<set>
#include<string>
using namespace std;

ifstream fin("A-small-attempt2.in");
ofstream fout("aout.txt");

/*struct node{
	char ch; int next, son;
	node(char ch='\0', int next=-1, int son=-1):ch(ch), next(next), son(son){}
};

vector<node> VN;
int idx[26];

void add(string str){
	int cur = idx[str[0]-'a'];
	for(int i=0; i<str.length(); i++){
		if(
	}
}*/
vector<vector<pair<bool,int> > > T;
//pair<int,int> ---(terminate here strs, next transition idx)
vector<pair<bool,int> > ex;  
void insert(string S){
	int idx = 0;
	for(int i=0, _I(S.size()); i<_I; i++){
		if(i==S.size()-1){  //here it is.
			T[idx][S[i]-'a'].first=true; return;
		}
		if(T[idx][S[i]-'a'].second<0){ //not exist
			T.push_back(ex); 
			T[idx][S[i]-'a'].second = T.size()-1;  
			idx = T.size()-1;
		}else   //exist
			idx = T[idx][S[i]-'a'].second;
	}
}
bool find(string S){
	int idx = 0;
	for(int i=0, _I(S.size()); i<_I; i++){
		if(i==S.size()-1) return T[idx][S[i]-'a'].first;
		if(T[idx][S[i]-'a'].second<0) return false;
		idx = T[idx][S[i]-'a'].second;
	}
}
bool part(string S){
	int idx = 0;
	for(int i=0, _I(S.size()-1); i<_I; i++){
		if(T[idx][S[i]-'a'].second<0) return false;
		idx = T[idx][S[i]-'a'].second;
	}
	return true;
}

/*
Case #1: 0
Case #2: 1
Case #3: 0
Case #4: 1
Case #5: 8
Case #6: 6
Case #7: 1
Case #8: 4
Case #9: 1
Case #10: 4
*/

string chk;
int c;
void dfs(string str, int id){
	if(id>=chk.size()){
//		cout<<str<<endl;
		if(find(str)){/* cout<<str<<endl;*/ c++;}
		return ;
	}
	int x = id, e = id+1;
	if(chk[id]=='('){
		x++;  while(chk[id]!=')') id++; e = id; id++;
	}else id++;
	for(int i=x; i<e; i++){
		if(part(str+chk[i]))
			dfs(str+chk[i], id);
	}
	return;
}

int main(){
	int L, D, N;
	fin>>L>>D>>N;
	ex.resize(26, make_pair(false,-1));
	T.push_back(ex);
	for(int i=0; i<D; i++){
		string input;  fin>>input;
		insert(input);
	}
	for(int i=1; i<=N; i++){
		c = 0;
		string input;  fin>>input;
		chk = input;
//		cout<<"begin:"<<endl;
		dfs("", 0);
		fout<<"Case #"<<i<<": "<<c<<endl;
	}
}