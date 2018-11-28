#include<stdio.h>
#include<string.h>
#include <iostream>
using namespace std;

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	cin>>n;
	char sentense[100];
	char translate[100];
	char a[30]="yhesocvxduiglbkrztnwjpfmaq";

	int i,j;
	int num;
	char temp;
	getchar();
	for(int i = 1 ; i <= n; i++){
		j = 0;
		temp=getchar();
		while(temp!='\n'){

			sentense[j] = temp;
			j++;
			temp = getchar();
		}
		sentense[j] = '\n';
//		cin>>j;
		j=0;
		while(sentense[j]!='\n'){
			temp = sentense[j];
			if(temp<='z' && temp>='a'){
				sentense[j] = a[temp-'a'];
			}
			j++;
		}
		
		cout<<"Case #"<<i<<": ";
		j=0;
		while(sentense[j]!='\n'){		
			printf("%c",sentense[j]);
			j++;
		}
		cout<<endl;
//		printf("%s\n",sentense);
			
	}

//	cin>>j;
//	p23();
	return 0;

	
}