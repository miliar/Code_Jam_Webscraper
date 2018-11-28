#include <cstdlib>
#include<iostream>
#include <stdio.h>
#include <string>
#include <conio.h>
using namespace std;

int main() {
	string a="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string b="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	string d,o;
	int n;
	int j=1;
	char c[32],z[16];
	
	FILE *f=freopen("A-small-attempt0.in","r",stdin);
	FILE *g=freopen("A-small-attempt0.out","w",stdout);
	//if(f){
		for(char i='a';i<='z';++i){
			c[i-'a']=b[((n=a.find(i,1))==a.npos)?0:n];
		}
		c['z'-'a']='q';
		c['q'-'a']='z';
		cin>>n;
		getline(cin,d);
		do{
			getline(cin,d);
			o="Case #";
			o.append(_itoa(j,z,10));
			o.append(": ");
			for(int i=0; i<d.length(); ++i){
				if(d[i]==' ')
					o.append(" ");
				else{
					o+=c[d[i]-'a'];
				}
			}
			cout<<o<<endl;
		}while(++j<=n);
	//}
	_getch();
	return 0;
}

