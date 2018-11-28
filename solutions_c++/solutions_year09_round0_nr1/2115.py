#include<iostream>
#include<vector>
#include<string>
using namespace std;
int L,D,N;
vector<string> dic;
int count(string& s){
	vector<string> vs(L);
	int p=0,result=0;
	for(int i=0 ; i<L ; i++){
		if(s[p]=='('){
			for(p++; s[p]!=')' ; p++){
				vs[i]+=s[p];
			}
		}else{
			vs[i]+=s[p];
		}
		p++;
	}
	for(int i=0 ; i<D ; i++){
		int j;
		for(j=0 ; j<L ; j++){
			if(vs[j].find(dic[i][j])==string::npos) break;
		}
		if(j==L) result++;
	}
	return result;
}

		
int main(){
	cin >> L >> D >> N;
	dic.resize(D);
	for(int i=0 ; i<D ; i++){
		cin >> dic[i];
	}
	for(int i=0 ; i<N ; i++){
		string s;
		cin >> s;
		int n=count(s);
		cout <<"Case #"<<i+1<<": " << n << endl;
	}
	return 0;
}