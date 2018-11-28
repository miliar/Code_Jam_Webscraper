#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <sstream>

#define dbg(a) cout << #a << " == " << a << endl
#define print(a) cout << a << endl

using namespace std;

int l, d, n;
char palavra[6000];

struct no{
	int filhos[30];
	bool fim;
} nos[100000];

int nnos;
int casos = 1;

void inserir(){
	int ind = 0;
	int i = 0;
	while(palavra[i]){
		if(nos[ind].filhos[palavra[i]-'a'] != -1){
			ind = nos[ind].filhos[palavra[i]-'a'];
			i++;
		} else {
			nos[ind].filhos[palavra[i]-'a'] = nnos;
			memset(nos[nnos].filhos, -1, sizeof(nos[nnos].filhos));
			nos[nnos].fim = false;
			i++;
			ind = nnos;
			nnos++;
		}
	}
	
	nos[ind].fim = true;
}

int inicios[30];

int busca(int letra, int no){
	int ret = 0;
	
	if(nos[no].fim) return 1;
	
	for(int i = inicios[letra]; i < inicios[letra+1] && palavra[i] != ')' && palavra[i] != '('; i++){	
		if(nos[no].filhos[palavra[i]-'a'] != -1){
			ret += busca(letra+1, nos[no].filhos[palavra[i]-'a']);
		}
	}
	
	return ret;
}

void process(){
	int res = 0;
	int pos = 0;
	
	for(int i = 0; palavra[i]; i++){
		if(palavra[i] == '(') {
			inicios[pos] = ++i;
			while(palavra[i] != ')') i++;
		} else inicios[pos] = i;
		
		pos++;
	}
	
	inicios[pos] = strlen(palavra);
	
	res = busca(0, 0);
	
	printf("Case #%d: %d\n", casos++, res);
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	memset(nos[0].filhos, -1, sizeof(nos[0].filhos));
	nnos = 1;
	nos[0].fim = false;
	
	scanf("%d %d %d", &l, &d, &n);
	for(int i = 0; i < d; i++){
		scanf("%s", palavra);
		inserir();
	}
	
	for(int i = 0; i < n; i++){
		scanf("%s", palavra);
		process();
	}
	
	return 0;
}
