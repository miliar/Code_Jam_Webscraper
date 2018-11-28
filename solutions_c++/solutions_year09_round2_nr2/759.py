#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

string borrar_ceros(string a){
   int i=0;
   while(a[i]=='0'&&i<a.size()-1)      i++;
   return a.substr(i,a.size()-i);
}


int main(){
	string s;
	int n;
	scanf("%d\n",&n);
	for(int i=1;i<=n;i++){
		getline(cin,s);
		s="00"+s;
		string aux=s;
		while(next_permutation(s.begin(),s.end()) && aux>=s);
		aux=borrar_ceros(s);
		printf("Case #%d: %s\n",i,aux.c_str());
	}
	return 0;
}

