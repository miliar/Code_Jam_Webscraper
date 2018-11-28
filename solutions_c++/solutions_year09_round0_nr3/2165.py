#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main(){
	int n; cin >> n>>ws;
	string wel("welcome to code jam");
	for(int i=0 ; i<n ;i++){
		string s; getline(cin,s);
		int table[19][550];
		for(int j=0 ; j<19 ; j++) fill_n(table[j],s.length(),0);
		table[0][0]= (s[0]=='w');
		for(int j=1 ; j<s.length() ; j++){
			table[0][j]=table[0][j-1]+(s[j]=='w');
		}
		for(int j=1 ; j<19 ; j++){
			for(int k=1 ; k<s.length() ; k++){
				table[j][k]=table[j][k-1]+ (wel[j]==s[k] ? table[j-1][k-1] : 0);
				table[j][k]%=10000;
			}
		}
		printf("Case #%d: %04d\n",i+1,table[18][s.length()-1]);

	}
		
	return 0;

}