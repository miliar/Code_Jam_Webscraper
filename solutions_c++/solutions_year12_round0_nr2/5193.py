//#include <cstdlib>
#include<iostream>
#include <stdio.h>
//#include <conio.h>
#include <vector>
using namespace std;

int main() {
	int n,t,s,p,j=1,ti,sup,q;
	string o;
	//FILE *f=freopen("B-small-attempt0.in","r",stdin);
	//FILE *g=freopen("B.out","w",stdout);
	cin>>t;
	//getline(cin,str);
	//cout<<t<<endl;
	do{
		sup=0,q=0;
		cin>>n>>s>>p;
		//cout<<n<<' '<<s<<p<<endl;
		for(int i=0;i<n;++i){
			cin>>ti;
			if(ti>=3*p-2)
				++q;
			else if(ti>=3*p-4&&ti>2)
				++sup;
			//cout<<ti<<endl;
		}
		//cout<<"Case #"<<j<<": "<<q<<"+"<<sup<<"s"<<s<<endl;
		cout<<"Case #"<<j<<": "<<(q+((sup<s)?sup:s))<<endl;
	}while(++j<=t);
	//_getch();
	return 0;
}

