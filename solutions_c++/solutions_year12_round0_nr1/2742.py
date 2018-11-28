#include "stdafx.h"

typedef map<string, string> Translate;
typedef map<char, char> Dictionary;

Translate T;
Dictionary D;

void init(){
	T["y qee"]="a zoo";
	T["ejp mysljylc kd kxveddknmc re jsicpdrysi"]="our language is impossible to understand";
	T["rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"]="there are twenty six factorial possibilities";
	T["de kr kd eoya kw aej tysr re ujdr lkgc jv"]="so it is okay if you want to just give up";
	iter(Translate, t, T){
		string key=t->first, value=t->second;
		loop(i, 0, key.length()){
			D[key[i]]=value[i];
		}
	}
}
string translate(string key){
	string value;
	loop(i, 0, key.length()){
		push(value, D[key[i]]);
	}
	return value;
}

int main(){
	init();
	D['z']='q';
	string G;
	getline(cin, G);
	int X=0;
	while(getline(cin, G)){
		X++;
		cout<<"Case #"<<X<<": "<<translate(G)<<endl;
	}
	return 0;
}
