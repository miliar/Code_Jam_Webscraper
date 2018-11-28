#include<cstdio>
#include<cmath>
#include<iostream>
#include<string>

using namespace std;

#define MOD 10000
int nsub[32];

int main(){
	int N; cin >> N; 
	string wel="welcome to code jam";
	string str;
	getline(cin,str);
	for(int k=0; k<N; k++){
		getline(cin, str);
		memset(nsub,0,sizeof(nsub));

		nsub[0]=(wel[0]==str[0]);
		for(int i=1; i<str.size(); i++)
			for(int j=0; j<wel.size(); j++)
				if(wel[j]==str[i]){
					nsub[j]+=(j?nsub[j-1]:1);
					nsub[j]%=MOD;
				}
		int res=nsub[wel.size()-1];

		cout << "Case #" << (k+1) << ": " << (res/1000) << ((res%1000)/100) << ((res%100)/10) << (res%10) << "\n";
	}
}
