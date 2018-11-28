#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;


int main(){
	int T;
	cin>>T;
	//int N;
	string N;
	vector<char> v;
	for(int cas=1;cas<=T;cas++){
		cin>>N;
		v.clear();
		v.push_back('0');
		/*(while (N>0){
			v.push_back(N%10);
			N/=10;
		}*/
		for(int i=0;i<N.size();i++) v.push_back(N[i]);
		next_permutation(v.begin(),v.end());
		/*int ret=0;
		for (int i=0;i<v.size();i++){
			ret*=10;
			ret+=v[i];
		}*/
		int i=0;
		N="";
		if (v[0]=='0') i++;
		for(;i<v.size();i++) N+=v[i];
 		cout<<"Case #"<<cas<<": "<<N<<"\n";
	}
}
