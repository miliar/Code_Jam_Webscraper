#include<iostream>
#include<vector>
#include<string>

using namespace std;
 int LL;

bool fits(string & w1, vector<vector<int> > & tab){
	int L=LL;
	bool res=true;
	for(int i=0; i<L; i++){
		int n1 = w1[i]-'a';
		if(!tab[i][n1]) res=false;
	}
	return res;
}
int main(){
	int L, D, N;
	cin>>L>>D>>N;
	LL=L;
	vector<string> wrds(D);
	vector<vector<vector<int> > > guess(N, vector<vector<int> >(L, vector<int>(26, 0)));
	vector<int> fitsiwords(N, 0);
	getline(cin, wrds[0]);
	for(int i=0; i<D; i++){
		//cin>>wrds[i]; 
		getline(cin, wrds[i]);
	}
	for(int i=0; i<N; i++){
		for(int j=0; j<L; j++){
			char tmp;
			cin>>tmp;
			if(tmp=='('){
				cin>>tmp;
				while(tmp!=')'){
					guess[i][j][tmp-'a']=1; cin>>tmp;
				}
			}else{
				guess[i][j][tmp-'a']=1;
			}
		}
		string tmp;
		getline(cin, tmp);
	}
	for(int i=0; i<D; i++){
		for(int j=0;j<N;j++){
			if(fits(wrds[i], guess[j])){
				fitsiwords[j]++;
			}
		}
	}
	
	for(int i=0;i<N; i++){
		cout<<"Case #"<<i+1<<": "<<fitsiwords[i]<<"\n";
	}
	
}
