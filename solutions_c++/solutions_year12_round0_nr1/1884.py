#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main(){
	char mapa[256];
	string a,b, linea;
	a="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	b="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	
	for (int i=0; i<a.size(); i++)
		mapa[a[i]-' '] = b[i];		
	mapa['q'-' '] = 'z';
	mapa['z'-' '] = 'q';
	int casos;
	cin>>casos;
	getline(cin, linea);
	for (int caso=1; caso<=casos; caso++){
		printf("Case #%d: ",caso);
		getline(cin, linea);
		for (int i=0; i<linea.size(); i++)
			
			putchar(mapa[linea[i]-' ']);
		
		putchar('\n');
	}
	
	return 0;
}
