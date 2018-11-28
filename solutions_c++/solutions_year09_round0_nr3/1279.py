#include<string>
#include<vector>
#include<algorithm>
#include<iostream>
#include<cstring>
#define MOD 10000

using namespace std;

string welcome = "welcome to code jam";
string eva;
int MEMO[50][700];
int rec(int actual , int indice){
	if(actual == welcome.size()){
		return 1;
	}
	if(MEMO[actual][indice] != -1){
		return MEMO[actual][indice];
	}
	int res = 0;
	for(int i = indice ; i < eva.size() ; i++)
		if(eva[i] == welcome[actual])
			res+=rec(actual+1,i+1)%MOD;
	MEMO[actual][indice] = res%MOD;
	return MEMO[actual][indice]; 
}
string normal(string s){
	string res = "";
	for(int i = 0 ; i < s.size() ; i++)
		if(welcome.find(s[i])!=string::npos)
			res+=s[i];
	return res;
}
string justif(int n){
	string S = "";
	while(n){
		S.insert(S.begin(),n%10+'0');
		n/=10;
	}
	while(S.size() != 4){
		S.insert(S.begin() ,'0');
	}
	return S;
}
int fun(string s){
	int res = 0;
	eva = s;
	for(int i = 0 ; i < s.size() ; i++){
		if(s[i] == 'w')
			res+=rec(1,i+1)%MOD;
	}
	return res%MOD;
}
int main(){
	int T;
	string s;
	cin>>T;
	getline(cin,s);	
	for(int t = 0 ; t < T; t++)	{
		getline(cin,s);
		memset(MEMO,-1,sizeof(MEMO));
		cout<<"Case #"<<t+1<<": "<<justif(fun(normal(s)))<<endl;
	}
	return 0;
}