#pragma warning(disable:4996)

#include <iostream>
#include <map>
#include <list>

using namespace std;

map<pair<char, char>, char> cmb;
map<char, char> opp;
list<char> inv;

void push(char c){
	if(!inv.empty() && cmb.find(pair<char, char>(*inv.rbegin(), c)) != cmb.end()){
		c = cmb[pair<char, char>(*inv.rbegin(), c)];
		inv.pop_back();
		push(c);
	}
	else{
		inv.push_back(c);
	}
}

void process(){
	int n, i;
	char a, b, c;
	list<char> ::iterator it, jt;
	scanf("%d ", &n);
	for(i = 0; i < n; i++){
		scanf("%c%c%c ", &a, &b, &c);
		cmb[pair<char, char>(a, b)] = cmb[pair<char, char>(b, a)] = c;
	}
	scanf("%d ", &n);
	for(i = 0; i < n; i++){
		scanf("%c%c ", &a, &b);
		opp[a] = b;
		opp[b] = a;
	}
	scanf("%d ", &n);
	for(i = 0; i < n; i++){
		scanf("%c", &a);
		push(a);
		for(it = inv.begin(); it != inv.end(); it++){
			for(jt = it; jt != inv.end(); jt++){
				if(opp[*it] == *jt){
					break;
				}
			}
			if(jt != inv.end()){
				break;
			}
		}
		if(it != inv.end()){
			inv = list<char>();
		}
	}
}

int main(){
	int i, t;
	freopen("input.txt", "r", stdin);
	freopen("outout.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; i++){
		cmb = map<pair<char, char>, char>();
		opp = map<char, char>();
		process();
		printf("Case #%d: [", i + 1);
		for(; !inv.empty(); inv.pop_front()){
			printf("%c", *inv.begin());
			if(1 < inv.size()){
				printf(", ");
			}
		}
		printf("]\n");
	}
	fcloseall();
	return 0;
}