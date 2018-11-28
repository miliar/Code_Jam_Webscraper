#include<iostream>
#include<stdio.h>
using namespace std;
int main() {
	char mapping[27]="yhesocvxduiglbkrztnwjpfmaq";
	int T;
	char text_g[101],flush;
	scanf("%d",&T);
	scanf("%c",&flush);
	for(int i=0;i<T;i++) {
		scanf("%[^\n]s",text_g);
		scanf("%c",&flush);
		cout<<"Case #"<<i+1<<": ";
		for(int j=0;text_g[j]!='\0';j++) {
			if(text_g[j]==' ')
				cout<<" ";
			else
				cout<<mapping[text_g[j]-'a'];
		}
		cout<<"\n";
		}
	return 0;
}
