#include <iostream>
using namespace std;
int main(){
	long long n;
	long long v[40],ind;
	long long numb[100];
	cin>>n;
	long long base,acc;
	long long val;
	string word;
	
	for(int q=1;q<=n;q++){
		cin>>word;
		base=0;
		val=1;
		for(int i=0;i<40;i++)v[i]=-1;
		
		for(int i=0;i<word.length();i++){
			if(word[i]<='9')ind=word[i]-'0';
			else ind=word[i]-'a'+10;
		
			if(v[ind]==-1){
				base++;
				v[ind]=val;
				if(val==1)val=0;
				else if(val==0)val=2;
				else val++;
			}

		}
		val = 0;
		acc = 1;
		if(base==1)base=2;
		for(int i=word.length()-1;i>=0;i--){
			if(word[i]<='9')ind=word[i]-'0';
			else ind=word[i]-'a'+10;
			val+=acc*v[ind];
			acc*=base;
		}
		cout<<"Case #"<<q<<": "<<val<<endl; /*
		cout<<word<<" "<<base<<endl;
		for(int i=0;i<word.length();i++){
			if(word[i]<='9')ind=word[i]-'0';
			else ind=word[i]-'a'+10;
			cout<<v[ind];
		}
		cout<<endl<<"-----------------"<<endl;*/
	}
}
