#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void imprime(string str){
	int len=str.length();
	for(int i=0;i<len;i++){
		if(str[i]!='0'){
			cout<<str.substr(i)<<endl;
			return;
		}
	}
}
void resuelva(){
	string tmp="000000000000000000000000000000000000000000000000",str;
	cin>>str;
	tmp+=str;
	next_permutation(tmp.begin(),tmp.end());
	imprime(tmp);
}
int main(){
	int n;
	scanf("%d\n",&n);
	for(int i=1;i<=n;i++){
		printf("Case #%d: ",i);
		resuelva();
	}
}
/*
3
115
1051
6233
*/
