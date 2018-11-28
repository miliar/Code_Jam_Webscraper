#include<map>
#include<iostream>
#include<string>
#include<vector>

using namespace std;
map<string , bool> M;
vector<string> letras;
vector<string> pos;
vector<bool> valid(100,false);
vector<vector<int > > sub(30 , vector<int>(30,0));

int numero(string s , int L, int lac){
	if(!M[s])
		return 0;
	if(lac == L){
		if(M[s])
			return 1;
		else
			return 0;
	}
	int res = 0;
	for(int i = 0 ; i < pos[lac].size() ; i++)
			res+=numero(s+pos[lac][i],L,lac+1);		
	return res;
}
int fun(string s , int L)
{	
	int res = 0;
	pos.clear();
	pos.resize(L);
	int j = 0;
	bool wan = false;
	for(int i = 0 ; i < s.size() ; i++){
		if(j > L)
			wan = true;
		if(s[i] == '('){
			i++;
			while(s[i] != ')'){
				if(pos[j].find(s[i]) == string::npos && (valid[s[i]-'a']))
					pos[j]+=s[i];
				i++;
			}
			j++;
		}
		else{
			pos[j]+=s[i];
			j++;
		}
	}
	if(j != L)
		wan = true;
	if (wan)
		return 0;
	string pal = "";
	for(int i = 0 ; i < pos[0].size() ; i++){
		res+=numero(pal+pos[0][i],L,1);
	}
	return res;	
}
int main(){

	int L , D , N;
	string s;
	cin>>L>>D>>N;
	for(int i = 0 ; i < D ; i++){
		cin>>s;
		for(int j = 1 ;j <= s.size() ; j++){
			M[s.substr(0,j)] = true;}
		for(int j = 0 ; j< s.size() ; j++){
			valid[s[j]-'a'] = true;
		}
	}
	
	for(int i = 0 ; i < N ; i++){
		cin>>s;		
		cout<<"Case #"<<i+1<<": "<<fun(s, L)<<endl;
	}
	return 0;
}
