#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int cambios,N,S,Q,i,a,o,validos,anterior;
vector<bool> valido;
vector<string> engine,query;
string buffer;

int main(){
cin >> N;
for(i=0;i<N;i++){
	cambios=0;
	cin >> S;
	engine.resize(S);
	getline(cin,buffer);
	for(o=0;o<S;o++) getline(cin,engine[o]);

	cin >> Q;
	query.resize(Q);
	getline(cin,buffer);
	for(o=0;o<Q;o++) getline(cin,query[o]);

	validos=S;
	valido.resize(S);
	for(a=0;a<S;a++) valido[a]=1;

	for(o=0;o<Q;o++){
		for(a=0;a<S;a++) 
			if(engine[a]==query[o]&&valido[a]==1){
				valido[a]=0; 
				validos--; 
				if(validos==0) anterior=a;
				}

		if(validos==0){
//		cout << o << ": " /*<< engine[a] << "==" << query[o] << " && " << valido[a]*/ << endl;
		
			cambios++;
			validos=S-1;
			for(a=0;a<S;a++) if(a!=anterior) valido[a]=1;
		}
	}
	cout << "Case #" << i+1 << ": " << cambios << endl;
}
}
