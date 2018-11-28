#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(){
	
	freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w+", stdout);
	int i,j,k,T;
	char hash[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	string str1;
	cin>>T;
	getline(cin, str1);
	int cnt =0;
	while(T -- >0){
		string G;
		string temp;
		getline(cin,G);
		int len = G.length();
		  cout<<"Case #"<<++cnt<<": ";
		for(i=0;i<len;i++){
			 if(G[i]!=' '){
				temp[i]=hash[G[i]-'a'];
				cout<<temp[i];
				}else{
					cout<<G[i];
				}
		}
		cout<<endl;
	}
return 0;
}