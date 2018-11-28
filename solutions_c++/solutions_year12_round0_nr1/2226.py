#include<iostream>
using namespace std;
int main(){
	string translate ="yhesocvxduiglbkrztnwjpfmaq";
	int t;
	cin>>t; cin.ignore();
	for(int i=1;i<=t;i++){
		char input[101];
		cin.getline(input,101);
		cout<<"Case #"<<i<<": ";
		for(int j=0;input[j]!='\0';j++){
			if(input[j]==' ') cout<<" ";
			else cout<<translate[input[j]-'a'];
		}
		cout<<endl;
	}
	return 0;
}
