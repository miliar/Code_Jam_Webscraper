#include<iostream>
#include<map>
#include<string>
#include<fstream>

using namespace std;

int main(){
	ifstream ifile("input.txt");
	ofstream ofile("out.txt");

	int t,i =0;
	ifile>>t;
	while(i++<t){
		string str;
		ifile>>str;
		//str = "11111";
		map<char , long long> m;
		map<char , long long> value;
		map<char , int> presence;

		int count = 0;
		for(int i = 0 ; i < str.length() ;i++){
			m[str[i]] +=1;
		}
		long long base = m.size();
		if(base==1) base = 2;
		long long temp = 0;

		value[str[0]] = 1;
		presence[str[0]] = 1;

		for(int i = 0 ; i < str.length() ; i++){
			if(presence[str[i]]==0){
				value[ str[i] ] = temp;
				presence[str[i]] = 1;
				if(temp==0) temp+=2;
				else temp++;
			}
		}
		
	//	for(map<char,long long>::iterator it = value.begin() ; it != value.end() ; it++)
	//		cout<<(*it).first<<" "<<(*it).second<<"\n";
	//	cout<<"-------\n";
		long long res = 0,factor=1;
		for(int i = str.length()-1 ; i >= 0 ; i--){
	//		cout<<value[str[i]]<<" * "<<factor<<"\n";
			res += value[str[i]]*factor;
			factor*=base;
		}
	//	cout<<"Case #"<<i<<": "<<res<<"\n";
		ofile<<"Case #"<<i<<": "<<res<<"\n";
	}
}