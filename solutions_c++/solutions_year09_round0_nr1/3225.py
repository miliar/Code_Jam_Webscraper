#include<fstream>
#include<iostream>
#include<vector>
#include<set>
#include<string>
using namespace std;

ifstream fin("A-large.in");
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

string chk;
int c, L;
void dfs(string str, int idx, int id){
//	cout<<str<<" "<<idx<<" "<<id<<endl;
	int x = id, e = id+1;
	int cur = str.length();
	if(chk[id]=='('){
		x++;  while(chk[id]!=')') id++; e = id; id++;
	}else id++;
	for(int i=x; i<e; i++){
		if(cur==L-1){
			if(T[idx][chk[i]-'a'].first){/* cout<<str<<endl;*/ c++;}
		}else if(T[idx][chk[i]-'a'].second>0)
			dfs(str+chk[i], T[idx][chk[i]-'a'].second, id);
	}
	return;
}

int main(){
	int D, N;
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
		dfs("", 0, 0);
		fout<<"Case #"<<i<<": "<<c<<endl;
	}
}