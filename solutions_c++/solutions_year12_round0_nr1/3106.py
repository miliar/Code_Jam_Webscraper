#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;

int main(){
	string s;
	int T,k=1;
	scanf("%d\n",&T);
	char rev[]={'y','h','e', 's' ,'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f' ,'m', 'a','q'};
	while(k<=T){
		getline(cin,s);
		for(int i=0;i<s.length();i++)
			if(s[i]>='a'&&s[i]<='z')s[i]=rev[s[i]-'a'];
		cout<<"Case #"<<k<<": "<<s<<endl;
		k++;
	}
	return 0;
}
