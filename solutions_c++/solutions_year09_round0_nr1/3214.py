#include<iostream>
#include<string>
#include<map>
#include<set>
#include<sstream>
#include<vector>
using namespace std;

set<string> Set;
int res;
int L,N,D;
void doit(vector<vector<char> > v, int n, string s){
	if(n==L){
		res++;
		return;
	}
	for(int i=0; i<v[n].size(); i++){
		if(Set.find(s+v[n][i])!=Set.end()){
			doit(v, n+1, s+v[n][i]);
		}
	}
}


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt.","w",stdout);

	scanf("%d%d%d",&L,&D,&N);
	string s;
	for(int i=0; i<D; i++){
		cin>>s;
		for(int j=1; j<=L; j++){
			Set.insert(s.substr(0,j));
		}
	}
	for(int Test=1; Test<=N; Test++){
		cin>>s;
		vector<vector<char> >vs(L, vector<char>());
		int pos=0;
		for(int i=0; i<L;i++){

			if(s[pos]=='('){
				do{
					vs[i].push_back(s[pos]);
				}while(s[++pos]!=')');
				pos++;
			}
			else{
				vs[i].push_back(s[pos++]);
			}
		}
			res=0;
			doit(vs,0,"");
			printf("Case #%d: %d\n",Test,res);
	}
//while(1);
}