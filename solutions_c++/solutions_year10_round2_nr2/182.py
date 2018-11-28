#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>
#include<set>

using namespace std;
int main(){
	int C, N,K, B,T;
	cin>>C;
	for(int i=0; i<C; i++){
		//cin>>wrds[i]; 
		cin>>N>>K>>B>>T;
		vector<int> X(N);
		vector<int> V(N);
		vector<int> S(N);
		vector<double> tim(N);
		for(int j=0; j<N; j++) cin>>X[j];
		for(int j=0; j<N; j++) cin>>V[j];
		for(int j=0 ; j<N; j++){
			tim[j] = (double(B-X[j]))/V[j];
		}
		for(int c=0; c<N; c++){
			S[c]=0;
			if(tim[c]>T){S[c]=1000000;continue;}
			for(int j=0; j<N; j++){
				if(tim[j]<=T)continue;
				if(X[j]>X[c])S[c]++;
			}	
			
		}
		sort(S.begin(), S.end());
		if(K>0 && S[K-1]==1000000)	
			cout<<"Case #"<<i+1<<": " <<"IMPOSSIBLE"<<"\n";
		else{
			int res=0;
			for(int j=0 ; j<K; j++)res+=S[j];
			cout<<"Case #"<<i+1<<": " <<res<<"\n";
		}
	}
	
}
