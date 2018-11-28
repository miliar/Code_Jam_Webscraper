#include<iostream>
#include <cstdlib>
using namespace std;

int main(){
	char gmapper[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int T;
	string c;
	getline (cin,c);
	T=atoi(c.c_str());
	int k=0;
	while(k<T){
		string str;
		getline (cin,str);
		int l=str.length();
		string str2=str;
		int i=0;
		while(i<l){
			if(str2[i]==' '){}
			else str2[i]=gmapper[(int)str[i]-97];
			i++;
		}
		cout<<"Case #"<<k+1<<": "<<str2<<endl;
		k++;
	}
	return 0;
}
