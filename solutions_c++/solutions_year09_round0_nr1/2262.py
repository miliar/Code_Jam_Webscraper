#include <cstdlib>
#include <cstdio>
#include <set>

using namespace std;

int l, d, n, q;

char W[5010][25];
set<char> P[25];
char pat[400];

bool match(int w){
	for(int i=0; i<l; i++){
		if(P[i].find(W[w][i])==P[i].end()) return 0;
	}
	return 1;
}

void process_pat(){
	int i=0;
	int j=0;
	while(i<l){
		P[i].clear();
		if(pat[j]!='('){
			P[i].insert(pat[j]);
			i++;
			j++;
			continue;
		}
		j++;
		while(pat[j]!=')'){
			P[i].insert(pat[j]);
			j++;
		}
		i++;
		j++;
	}
}

int main(){
	scanf("%d %d %d\n", &l, &d, &n);
	for(int i=0; i<d; i++){
		scanf("%s", W[i]);
	}
	for(int i=0; i<n; i++){
		scanf("%s", pat);
		process_pat();
		q=0;
		for(int j=0; j<d; j++) if(match(j)) q++;
		printf("Case #%d: %d\n", i+1, q);
	}
}

