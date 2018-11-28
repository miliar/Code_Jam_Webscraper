#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <set>
#include <bitset>
#include <stack>

#define dbg(a) //cout << #a << " = " << a << endl
#define print(a) //cout << a << endl

using namespace std;

set<int> mapas[11];
int numeros[20], n;
set<int> temp;
set<int>::iterator it;

void testar(int ind, int atual){
	temp.clear();
	
	int t;
	while(atual != 1 && !temp.count(atual)){
		dbg(atual);dbg(ind);
		temp.insert(atual);
		
		t = 0;
		while(atual){
			t += (atual%ind)*(atual%ind);
			atual /= ind;
		}
		
		atual = t;
	}
	
	if(atual == 1) {
		for(it = temp.begin(); it != temp.end(); it++){
			mapas[ind].insert(*it);
		}
	}
}

int busca(){
	bool eh;
	for(int i = 2; true ; i++){
		eh = true;
		dbg(i);
		for(int j = 0; j < n && eh; j++){
			if(!mapas[numeros[j]].count(i)){
				testar(numeros[j], i);
				if(!mapas[numeros[j]].count(i)) eh = false;
			}
		}
		
		if(eh) return i;
	}
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	
	int t, casos = 1;
	char linha[100];
	
	gets(linha);
	sscanf(linha, "%d",&t);
	
	while (t--){
		gets(linha);
		stringstream s(linha);
		n = 0;
		
		while(s >> numeros[n]) n++;
		
		printf("Case #%d: %d\n", casos++, busca());
	}
    
    return 0;
}
