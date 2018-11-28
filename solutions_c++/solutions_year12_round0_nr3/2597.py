#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstdlib>
#include <cstdio>
using namespace std;

/*
Google CodeJam 2012 - Problem C
Guillermo Croppi (Argentina)

Crazy problem.... i just did pairs.. that's all... good luck understanding...

*/

void rotate(string &s) {
	for (int i = 1; i < s.size(); i++)
		swap(s[i-1], s[i]);
}

string rotateString(string a, int times) {
	int aux = times;
	string s = a;
	while(aux--){
	for (int i = 1; i < s.size(); i++)
		swap(s[i-1], s[i]);
	}
	return s;
}

bool palindrome(string s){
	string::iterator inicio = s.begin(), final = s.end()-1;
	bool flag;
	if(s.length() > 2){
		while ( *inicio == *final && inicio != final ){ ++inicio; --final;}
		flag = (inicio == final);
	} else {
		flag = (*inicio==*final);
	}
	return flag;
}

int main(int argc, char *argv[]) {
	int bottom, top;
	int cases;
	int casesCount = 1;
	unsigned long cuenta;
	char aux[10], sBottom[10], sTop[10];
	bool flag;
	set<int> possibilities;
	set< set<int> > pares;
	set<int> a;
	set<int>::iterator it;
	set< set<int> >::iterator it2;

	string s, original;
	string::iterator inicio, final;
	
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	scanf("%d",&cases);
	while(cases--){
		scanf("%d %d", &bottom, &top);
		cuenta = 0;
		sprintf(sBottom,"%d",bottom);
		sprintf(sTop,"%d",top);
		possibilities.clear();
		pares.clear();
		for(int i=bottom; i<=top; i++) possibilities.insert(i);
		for(it=possibilities.begin(); it!=possibilities.end(); it++){
			sprintf(aux,"%d",*it);
			s.assign(aux); 
			original.assign(aux);
			for(int  j=0; j<s.length()-1; j++){
				a.clear();
				rotate(s);
				if(atoi(s.c_str())>=bottom && atoi(s.c_str())<=top && !palindrome(original)){
					a.insert(atoi(original.c_str())); a.insert(atoi(s.c_str()));
					pares.insert(a);
				}
					
				/*
				if(auxset.find(atoi(s.c_str()))==auxset.end()){
					rotate(s);
					if(atoi(s.c_str())>=bottom && atoi(s.c_str())<=top){
						if(!palindrome(s)) {
							cout << s << " ";
							auxset.insert(atoi(s.c_str()));
							cuenta++;
						}
					} else cout << s << " es chico | " ;
				} else cout << s << " ya entro | " ;
				*/
				
				
				
				/*
				rotate(s);
				cout << s << " ";
				*/
				
				
				/*
				rotate(s);
				if(atoi(s.c_str())>=bottom && atoi(s.c_str())<top){
				cout << s << " ";
				*/
				/*
				rotate(s);
				if(atoi(s.c_str())>=bottom && atoi(s.c_str())<top){
					inicio=s.begin(); final=s.end()-1;
					if(s.length() > 2){
						while ( *inicio == *final && inicio != final ) ++inicio, --final;
					}
					flag = (inicio == final);
					if(!flag) {cout << s << " "; pez.insert(atoi(s.c_str())); cuenta++;}
				}
				*/
			}
		}
		for(set< set<int> >:: iterator it1 = pares.begin(); it1!= pares.end(); it1++){
			if( (*it1).size() == 2) cuenta++;
		}
		printf("Case #%d: %ld\n",casesCount++ ,cuenta);
	}
	
	return 0;
}

