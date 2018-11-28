#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <set>

using namespace std;

#define D 5000
#define L 15
#define MSG_MAX 1000

int n;
int l,d;

char msg[MSG_MAX];
vector<string> words;

void read_words(){
	words.resize(d);
	for(int i=0; i < d; i++){
		cin >> words[i];
	}
	cin.getline(msg,MSG_MAX);
}

void read_test(){
	cin.getline(msg,MSG_MAX);
}

set<int> consistent;

void solve_test(){
	consistent.clear();
	for(int i=0; i < words.size(); i++)
		consistent.insert(i);
	
	int j=0;
	for(int i=0; i < l; i++){
		set<char> symbols;
		if (msg[j] != '(')
			symbols.insert(msg[j++]);
		else{
			j++;
			do{		
				symbols.insert(msg[j++]);
			} while (msg[j] != ')');
			j++;
		}
		set<int> to_erase;
		for(set<int>::iterator it = consistent.begin(); it != consistent.end(); it++)
			if (symbols.count(words[*it][i]) == 0)
				to_erase.insert(*it);
		for(set<int>::iterator it = to_erase.begin(); it != to_erase.end(); it++)
			consistent.erase(*it);
	}
}

void dump_sol(int i){
	cout << "Case #" << i << ": " << consistent.size() << endl;
}

int main(){
	cin >> l >> d >> n;
	cin.getline(msg,1);
	read_words();
	for(int i=0; i < n; i++){
		read_test();
		solve_test();
		dump_sol(i+1);
	}
}
