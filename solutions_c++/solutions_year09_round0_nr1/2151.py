#include <cstdio>
#include <vector>
#include <cstdlib>
#include <string>
using namespace std;

struct Trie{
	int adj[26];
	int end;
};
Trie trie[1500000];
int volantes[5000];
vector<string> words;
int L, D, N;
int counter = 0;
int caso = 1;
void process(){
	char pqop[2500];
	strcpy(pqop, "");
	for(int i = 0; i < N; i++){
		//fprintf(stderr, "%d\n", i);
		scanf("%s", pqop);
		int answer = 0;
		int abrePoss = 0;
		counter = 0;
		memset(trie, 0, sizeof(trie));
		for(int t = 0; pqop[t]; t++){
			if(pqop[t] == '(')abrePoss = 1;
			else if(pqop[t] == ')'){
				abrePoss = 0;
				counter++;
			}
			else{
				if(abrePoss){
					trie[counter].adj[pqop[t]-'a'] = (counter+1);
				}else{
					trie[counter].adj[pqop[t]-'a'] = ++counter;
				}
			}
		}
		for(int i = 0; i < D; i++){
			int cara = 0;
			for(int t = 0; t < words[i].length(); t++){
				if(trie[cara].adj[words[i][t] - 'a'])cara++;
				else{
					break;
				}
			}
			if(cara == L)answer++;
		}
		printf("Case #%d: %d\n", caso++, answer);
	}
}
int main(){
	/*freopen("A-large.in", "r", stdin);
	freopen("Answer-A_large.out", "w", stdout);*/
	scanf("%d%d%d", &L, &D, &N);
	for(int i = 0; i < D; i++){
		char wd[25];
		strcpy(wd, "");
		scanf("%s", wd);
		words.push_back(string(wd));
		/*
		int dude = 0;
		
		for(int t = 0; wd[t]; t++){
			if(trie[dude].adj[wd[t]-'a'] == -1){
				trie[dude].adj[wd[t]-'a'] = ++counter;
				dude = counter;
			}else dude = trie[dude].adj[wd[t]-'a'];
		}
		trie[dude].end = 1;
		*/
	}
	process();
	return 0;
}
