#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;
#define tipo first
#define malted second
#define INF 1000000

vector<vector<pair<int,bool> > > customer;

int i,o,T,N,M,C,u;
vector<bool> batido;
bool back(int num){
batido[num]=0;
if(num!=N-1){
	if(back(num+1)==1) return 1;
}
else {
	for(o=0;o<M;o++){
		for(u=0;u<customer[o].size();u++){
			if(batido[customer[o][u].tipo-1]==customer[o][u].malted) break;
		}
		if(u==customer[o].size()) break;
	}
	if(o==M){
		cout << "Case #" << i+1 << ": " << batido[0];
		for(o=1;o<N;o++) cout << " " << batido[o];
		cout << endl;
		return 1;
	}
}

batido[num]=1;
if(num!=N-1){
	if(back(num+1)==1) return 1;
}
else {
	for(o=0;o<M;o++){
		for(u=0;u<customer[o].size();u++){
			if(batido[customer[o][u].tipo-1]==customer[o][u].malted) break;
		}
		if(u==customer[o].size()) break;
	}
	if(o==M){
		cout << "Case #" << i+1 << ": " << batido[0];	
		for(o=1;o<N;o++) cout << " " << batido[o];
		cout << endl;
		return 1;
	}
}
return 0;
}

int main(){
cin >> C;
for(i=0;i<C;i++){
	cin >> N >> M;
	batido.resize(N);
	customer.resize(M);
	for(o=0;o<M;o++){
		cin >> T;
		customer[o].resize(T);
		for(u=0;u<T;u++){
			cin >> customer[o][u].tipo >> customer[o][u].malted;
		}
	}
	if(back(0)==0) cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
}

}
