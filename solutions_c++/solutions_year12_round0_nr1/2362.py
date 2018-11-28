#include <iostream>
#include <string>
#include <cassert>
using namespace std;

#define uchar unsigned char

const string g1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
const string g2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
const string g3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

const string s1 = "our language is impossible to understand";
const string s2 = "there are twenty six factorial possibilities";
const string s3 = "so it is okay if you want to just give up";

uchar mapa[255];

void aprender(const string& a, const string& b) {
	assert( a.size() == b.size() );
	for(unsigned int i=0; i<a.size(); i++)
		mapa[ a[i] ] = b[i];
}

void imprimirMapa() {
	for(uchar a='a'; a<='z'; a++)
		cout<<a<<" -> "<<mapa[a]<<endl;
}

void controlarMapa() {
	for(uchar a='a'; a<='z'; a++) {
		for(uchar b='a'; b<='z'; b++) {
			if(a==b) continue;
			if( mapa[a] == mapa[b] )
				cout<<a<<" - "<<b<<endl;
		}
	}
	for(uchar a='a'; a<='z'; a++) {
		if(mapa[a]==a)
			cout<<a<<endl;
	}
}

void construirMapa() {
	for(uchar i=0; i<255; i++)
		mapa[i] = i;
	mapa['y'] = 'a';
	mapa['e'] = 'o';
	mapa['q'] = 'z';
	mapa['z'] = 'q';
	aprender(g1, s1);
	aprender(g2, s2);
	aprender(g3, s3);
}

string traducir(const string& g) {
	string r( g.size(), 0 );
	for(unsigned int i=0; i<g.size(); i++)
		r[i] = mapa[ g[i] ];
	return r;
}
	
int main(int argc, char *argv[]) {
	construirMapa();
//	controlarMapa();
//	imprimirMapa();
	int T;
	char aux[256];
	cin>>T;
	cin.ignore();
	for(int X=1; X<=T; X++) {
		cin.getline(aux, 256);
		string G(aux);
		cout<<"Case #"<<X<<": "<<traducir(G)<<endl;
	}
	return 0;
}

