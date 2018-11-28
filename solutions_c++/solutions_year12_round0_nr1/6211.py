#include<iostream>
using namespace std;

void check(char s[102]){
	int ch,a,n;
	char ar[]="yhesocvxduiglbkrztnwjpfmaq";
	char dr[]="abcdefghijklmnopqrstuvwxyz";
	for(int i=0;s[i]!='\0';i++){
		if(s[i]==' '){
			cout<<s[i];
		}
		else{
			for(n=0;dr[n]!=s[i];n++);
			cout<<ar[n];
		}

		}
	

}

int main(){
	int t;
	char s[102];
	cin>>t;
	
		cin.getline(s,101);
	int i=0;
	while(i<t){
		i++;
			cout<<"Case #"<<i<<":";
		cin.getline(s,101);
		check(s);
		cout<<"\n";
		
	}

	return 0;
}
