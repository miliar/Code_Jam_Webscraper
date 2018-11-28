#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>
#include<set>

using namespace std;
int main(){
	int T, N, M;
	cin>>T;
	for(int i=0; i<T; i++){
		//cin>>wrds[i]; 
		cin>>N>>M;
		vector<string> expa(N);
		vector<string> newpa(M);
		for(int j=0; j<N; j++) cin>>expa[j];
		for(int j=0; j<M; j++) cin>>newpa[j];
		set<string> ss; ss.clear();
		for(int j=0 ; j<N; j++){
			string tmp;
			int pos=1;
			while((pos=expa[j].find('/', pos))!=string::npos){
//			cout<<expa[j]<<" "<<pos<<" ";
				tmp=expa[j].substr(0, pos);
				ss.insert(tmp);
				pos++;
			}
			ss.insert(expa[j]);
		}
		int start=ss.size();
		for(int j=0; j<M; j++){
//			cout<<j;
			string tmp;
			int pos=1;
			while((pos=newpa[j].find('/', pos))!=string::npos){
//			cout<<newpa[j]<<" "<<pos<<" ";
				tmp=newpa[j].substr(0, pos);
				ss.insert(tmp);
				pos++;
			}
			ss.insert(newpa[j]);
		}
		int res=ss.size()-start;
		cout<<"Case #"<<i+1<<": " <<res<<"\n";
	}
	
}
