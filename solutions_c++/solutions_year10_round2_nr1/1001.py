#include<iostream>
#include<vector>
#include<string.h>
#include<map>
#define FOR(a,b) for(int a=0; a<b; a++)
using namespace std;


int ttt,n,m,sol,aa;
string aux;
vector< vector< string > >  root;
vector< string > check;
 
vector< string > tokens(string& s){
	vector< string > sol = vector< string >();
	int i = 1,j;
	for(j = 1; j<s.length() ; j++){
		if(s[j]=='/'){
			sol.push_back(s.substr(i,j-i));
			i=j+1;
		}
	}
	sol.push_back(s.substr(i,s.size()-i));
	return sol;
}

int notIn(vector<string>& s){
	int sol = s.size(), solP;
	FOR(i,root.size()){
		int j = 0;
		while( j < s.size() && j < root[i].size() && s[j] == root[i][j]){
			j++;
		}
		if(j==s.size())
			return 0;
		solP = s.size() - j;
		sol = min(sol, solP);
	}
	return sol;
}

int main(){
	cin >> ttt;
	for(int tt = 1; tt <= ttt ; tt++){
		cin >> n >> m;
		root.clear();
		sol = 0;
		FOR(i,n){
			cin >> aux;
			root.push_back(tokens(aux));
		}

		FOR(i,m){
			cin >> aux;
			check = tokens(aux);
			aa = notIn(check);
			if(aa!=0){
				sol+=aa;
				root.push_back(check);
			}
		}

		cout << "Case #" << tt << ": " << sol << endl;;
	}
}
