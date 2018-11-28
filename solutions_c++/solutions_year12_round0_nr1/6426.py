#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#define max 1001
using namespace std;

int main(){
	
	
	freopen("in.txt", "r", stdin);
    freopen("output.txt", "w+", stdout);
	int i,j,k,T;
	char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	string kk;
	//getline(cin,T);
	cin>>T;
	getline(cin, kk);
	int cnt =0;
	while(T -- >0){
		string G;
		string temp;
		getline(cin,G);
		int len = G.length();
		  cout<<"Case #"<<++cnt<<": ";
		for(i=0;i<len;i++){
			 if(G[i]!=' '){
				temp[i]=map[G[i]-'a'];
				cout<<temp[i];
				}else{
					cout<<G[i];
				}
		}
		cout<<endl;
	}
return 0;
}