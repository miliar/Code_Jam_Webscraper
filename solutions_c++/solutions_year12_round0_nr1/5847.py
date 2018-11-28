#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;



int main()
{
	freopen("sam.txt","r",stdin);
	freopen("ram.txt","w",stdout);
	int n,i,j;
	string str;
	string replace="yhesocvxduiglbkrztnwjpfmaq";
	scanf("%d\n",&n);
	for(i=0;i<n;i++){
		printf("Case #%d: ",i+1);
		getline(cin,str);
		for(j=0;j<str.length();j++){
			if(str[j]>='a' && str[j]<='z'){
				cout<<replace[str[j]-97];
			}
			else cout<<str[j];
		}
		cout<<endl;
	}
	return 0;
}